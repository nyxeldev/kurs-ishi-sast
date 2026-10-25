#!/usr/bin/env python3
"""
Amaliy qism uchun diagrammalarni yasash skripti.

Ishlatish:
    python kod/tahlil/diagramma.py

Kirish:  kod/natijalar/*.json va *.sarif (hisobot.py bilan bir xil manbalar)
Chiqish: kod/natijalar/rasm-1-aniqlash-ulushi.png  (va .svg)
         kod/natijalar/rasm-2-birgalikda-qamrov.png (va .svg)

Raqamlar `hisobot.py` dagi moslashtirish mantiqidan olinadi — diagrammada
qo'lda kiritilgan qiymat yo'q. Vositalar chiqishi o'zgarsa, diagramma ham
o'zgaradi.

Rasm sarlavhasi diagramma ichiga yozilmaydi: kurs ishida rasm nomi
("3.1-rasm. ...") rasm ostida matn sifatida beriladi (CLAUDE.md, formatlash).
O'lchov nomini x o'qi yozuvi tashiydi.

Rang tanlovi
------------
Bitta o'lchov — bitta rang: 1-rasmda to'rtala panjara bir xil ko'k (#2a78d6).
2-rasmda esa gap bitta natijada (to'liq qamrov), shu sababli oxirgi panjara
ko'k, qolganlari kulrang (#898781) — urg'u naqshi. Kulrang panjaralar qator
emas, balki urg'usizlantirilgan fon: har birining qiymati panjara yonida
yozilgani uchun ma'no rangga tayanmaydi.
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path as MplPath

sys.path.insert(0, str(Path(__file__).resolve().parent))

from hisobot import (  # noqa: E402
    ETALON,
    NATIJA,
    bandit_oqish,
    codeql_oqish,
    moslashtirish,
    semgrep_oqish,
)

# --- Ranglar (dataviz qo'llanmasining tekshirilgan palitrasi, yorug' rejim) ---
SIRT = "#fcfcfb"        # rasm foni
ASOSIY_SIYOH = "#0b0b0b"  # toifa nomlari
IKKILAMCHI = "#52514e"   # qiymat yozuvlari, o'q nomi
XIRA = "#898781"         # o'q raqamlari; urg'usizlantirilgan panjara
PANJARA = "#e1e0d9"      # ingichka to'r chizig'i
ASOS = "#c3c2b7"         # nol chizig'i
KOK = "#2a78d6"          # asosiy rang (palitra 1-slot)

DPI = 300
QALAMTOSH_PX = 4 * DPI / 96   # 4 CSS piksel — panjara uchining yumaloqligi


def topilmalarni_yigish():
    """hisobot.py bilan bir xil manbalardan topilgan zaifliklarni olish."""
    manbalar = {
        "Bandit": bandit_oqish(NATIJA / "01-bandit.json"),
        "Semgrep (rasmiy)": semgrep_oqish(NATIJA / "02-semgrep.json"),
        "Semgrep (maxsus)": semgrep_oqish(NATIJA / "03-semgrep-maxsus.json"),
        "CodeQL": codeql_oqish(NATIJA / "05-codeql.sarif"),
    }
    topilgan = {}
    for nom, topilmalar in manbalar.items():
        if topilmalar:
            topilgan[nom] = set(moslashtirish(topilmalar)[0])
    return topilgan


def _yumaloq_uchli_yol(x0, x1, y_markaz, balandlik, r):
    """Chap uchi tekis, o'ng uchi yumaloqlangan gorizontal panjara yo'li.

    Nol chizig'iga tegib turgan uch tekis qoladi, ma'lumot uchi yumaloqlanadi.
    """
    y0 = y_markaz - balandlik / 2
    y1 = y_markaz + balandlik / 2
    r = max(0.0, min(r, (x1 - x0) / 2, balandlik / 2))
    k = 0.5523 * r   # aylana yoyining Bezye yaqinlashuvi

    nuqtalar = [
        (x0, y0),
        (x1 - r, y0),
        (x1 - r + k, y0), (x1, y_markaz - k), (x1, y_markaz),
        (x1, y_markaz + k), (x1 - r + k, y1), (x1 - r, y1),
        (x0, y1),
        (x0, y0),
    ]
    buyruqlar = [
        MplPath.MOVETO,
        MplPath.LINETO,
        MplPath.CURVE4, MplPath.CURVE4, MplPath.CURVE4,
        MplPath.CURVE4, MplPath.CURVE4, MplPath.CURVE4,
        MplPath.LINETO,
        MplPath.CLOSEPOLY,
    ]
    return MplPath(nuqtalar, buyruqlar)


def _r_malumot_birligida(ax):
    """4 CSS pikselni x o'qi ma'lumot birligiga aylantirish."""
    teskari = ax.transData.inverted()
    x0 = teskari.transform((0, 0))[0]
    x1 = teskari.transform((QALAMTOSH_PX, 0))[0]
    return abs(x1 - x0)


def chizish(yozuvlar, ranglar, o_q_nomi, fayl_nomi, balandlik_dyuym):
    """Gorizontal panjara diagrammasini yasab, PNG va SVG ga saqlash.

    yozuvlar: [(nom, qiymat), ...] — yuqoridan pastga tartibda
    ranglar:  har bir panjara uchun rang
    """
    jami = len(ETALON)
    fig, ax = plt.subplots(figsize=(6.5, balandlik_dyuym), dpi=DPI)
    fig.patch.set_facecolor(SIRT)
    ax.set_facecolor(SIRT)

    n = len(yozuvlar)
    y_oriniari = list(range(n - 1, -1, -1))   # birinchi yozuv tepada
    balandlik = 0.40                          # ingichka panjara

    ax.set_xlim(0, jami)
    ax.set_ylim(-0.7, n - 0.3)
    ax.set_xticks(range(0, jami + 1, 6))
    ax.set_yticks(y_oriniari)
    ax.set_yticklabels([nom for nom, _ in yozuvlar])

    # --- Chroma: ingichka, orqada turadigan to'r; ortiqcha ramka yo'q ---
    ax.set_axisbelow(True)
    ax.xaxis.grid(True, color=PANJARA, linewidth=0.6, solid_capstyle="butt")
    ax.yaxis.grid(False)
    for chekka in ax.spines.values():
        chekka.set_visible(False)
    ax.axvline(0, color=ASOS, linewidth=0.8, zorder=3)

    ax.tick_params(axis="x", colors=XIRA, labelsize=8, length=0)
    ax.tick_params(axis="y", colors=ASOSIY_SIYOH, labelsize=9, length=0)
    ax.set_xlabel(o_q_nomi, color=IKKILAMCHI, fontsize=8.5, labelpad=8)

    fig.tight_layout()
    fig.canvas.draw()                 # transData aniq bo'lishi uchun
    r = _r_malumot_birligida(ax)

    for y, (_nom, qiymat), rang in zip(y_oriniari, yozuvlar, ranglar):
        if qiymat > 0:
            ax.add_patch(
                PathPatch(
                    _yumaloq_uchli_yol(0, qiymat, y, balandlik, r),
                    facecolor=rang, edgecolor="none", zorder=2,
                )
            )
        # Tanlab to'g'ridan-to'g'ri belgilash: faqat panjara uchida
        ulush = 100 * qiymat / jami
        ax.text(
            qiymat + jami * 0.015, y,
            f"{qiymat} / {jami}  ·  {ulush:.0f}%",
            va="center", ha="left", fontsize=8.5, color=IKKILAMCHI,
        )

    fig.tight_layout()
    for kengaytma in ("png", "svg"):
        yo_l = NATIJA / f"{fayl_nomi}.{kengaytma}"
        fig.savefig(yo_l, facecolor=SIRT, bbox_inches="tight")
        print(f"  yozildi: {yo_l.name}")
    plt.close(fig)


def main():
    topilgan = topilmalarni_yigish()
    if not topilgan:
        print("XATO: natija fayllari topilmadi. Avval tahlil.sh ni ishga tushiring.")
        return

    # --- 1-rasm. Har bir vositaning aniqlash ulushi ---
    yozuvlar = sorted(
        ((nom, len(kodlar)) for nom, kodlar in topilgan.items()),
        key=lambda x: x[1],
        reverse=True,
    )
    print("1-rasm (aniqlash ulushi):")
    chizish(
        yozuvlar,
        [KOK] * len(yozuvlar),
        f"Aniqlangan zaifliklar soni (etalon to'plam: {len(ETALON)} ta)",
        "rasm-1-aniqlash-ulushi",
        2.9,
    )

    # --- 2-rasm. Vositalarni birgalikda qo'llashdagi qamrov ---
    # Ochko'z (greedy) tartib: har qadamda etalon to'plamga eng ko'p YANGI
    # zaiflik qo'shadigan vosita tanlanadi. Shu bilan "to'liq qamrovga
    # eng qisqa yo'l qanday" degan savolga javob beriladi. Hech narsa
    # qo'shmaydigan vosita diagrammaga kiritilmaydi.
    qolgan = dict(topilgan)
    yigilgan = set()
    kombinatsiyalar = []
    while qolgan:
        nom = sorted(
            qolgan,
            key=lambda k: (-len(qolgan[k] - yigilgan), -len(qolgan[k]), k),
        )[0]
        kodlar = qolgan.pop(nom)
        if kombinatsiyalar and not (kodlar - yigilgan):
            break
        yigilgan |= kodlar
        belgi = nom if not kombinatsiyalar else f"+ {nom}"
        kombinatsiyalar.append((belgi, set(yigilgan)))

    yozuvlar2 = [(nom, len(kodlar)) for nom, kodlar in kombinatsiyalar]
    # Urg'u: to'liq qamrovga erishgan kombinatsiya ko'k, qolganlari kulrang
    ranglar2 = [
        KOK if len(kodlar) == len(ETALON) else XIRA for _nom, kodlar in kombinatsiyalar
    ]
    print("2-rasm (birgalikda qamrov):")
    chizish(
        yozuvlar2,
        ranglar2,
        f"Qamrab olingan zaifliklar soni (etalon to'plam: {len(ETALON)} ta)",
        "rasm-2-birgalikda-qamrov",
        3.1,
    )


if __name__ == "__main__":
    main()
