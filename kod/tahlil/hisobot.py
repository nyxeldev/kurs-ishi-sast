#!/usr/bin/env python3
"""
Statik tahlil natijalarini normallashtirib, qiyosiy jadval va
aniqlik metrikalarini hisoblash skripti.

Ishlatish:
    python kod/tahlil/hisobot.py

Kirish:  kod/natijalar/*.json   (Bandit, Semgrep — tahlil.sh chiqishi)
         kod/natijalar/*.sarif  (CodeQL — tahlil.sh chiqishi)
Chiqish: kod/natijalar/qiyosiy-jadval.md
         kod/natijalar/metrikalar.md
         kod/natijalar/moslashtirish.md

Moslashtirish qoidasi (3.1-band, baholash mezonlari)
----------------------------------------------------
Vosita topilmasi etalon zaiflikka quyidagi hollardan biri bajarilganda
bog'lanadi:

  (a) topilma qatori etalon qatoridan TOLERANS qatordan ko'p farq
      qilmasa, yoki
  (b) topilma ham, etalon zaiflik ham ayni bir funksiya tanasida
      joylashgan bo'lsa.

(b) sharti zarur, chunki vositalar zaiflikni ba'zan cho'kma (sink)
qatorida emas, manba (source) qatorida qayd etadi: masalan Semgrep ning
`sql-injection-db-cursor-execute` qoidasi Z-02 ni so'rov tuzilgan
48-qatorda emas, kiritma olingan 43-qatorda ko'rsatadi.

Modul darajasidagi — hech bir funksiya tanasiga kirmaydigan — topilmalarga
faqat (a) sharti qo'llanadi. Aks holda fayl boshidagi `import`
ogohlantirishlari modul o'zgaruvchilaridagi zaifliklarga noto'g'ri
bog'lanib ketadi.

Bir topilma ko'pi bilan bitta etalon zaiflikka bog'lanadi, lekin bitta
etalon zaiflikni bir necha topilma tasdiqlashi mumkin. Shu sababli ayni
bir zaiflikning takroriy xabari yolg'on ijobiy natija (FP) sifatida
hisoblanmaydi — u alohida ustunda ("Takroriy") keltiriladi.

Bir qatorda bir nechta etalon zaiflik bo'lganda (Z-09 va Z-10 —
app.py:148) topilmalar ikki o'tishda taqsimlanadi: avval CWE kodi aniq
mos kelganlar, so'ngra band bo'lmagan yozuvlar bo'yicha. Shu bilan bir
qatordagi ikkita zaiflikdan faqat bittasi hisobga olinishi barataraf
etiladi.

Bir qoida bir necha CWE kodini ko'rsatishi mumkin (CodeQL ning
`py/path-injection` qoidasi beshta kodni beradi). Shu sababli har bir
topilma uchun CWE kodlari to'plami saqlanadi va mos kelish shu to'plam
bo'yicha tekshiriladi; jadvallarda esa birinchi (asosiy) kod ko'rsatiladi.

Qo'lda tekshiruv
----------------
Evristika topilmaning qaysi zaiflik HAQIDA ekanini bilmaydi — u faqat
joylashuvga va CWE kodiga qaraydi. Shu sababli ba'zi topilmalar yonidagi
etalon yozuviga noto'g'ri bog'lanishi mumkin. Bunday hollar qo'lda
tekshirilib, `TASDIQLANGAN_FP` ro'yxatiga sababi bilan kiritiladi va
to'g'ridan-to'g'ri yolg'on ijobiy natija deb hisoblanadi. Ro'yxatdagi
yozuv mos topilma topmasa, skript ogohlantirish beradi.
"""

import ast
import json
from pathlib import Path

ILDIZ = Path(__file__).resolve().parents[2]
NATIJA = ILDIZ / "kod" / "natijalar"
OBYEKT = ILDIZ / "kod" / "zaif-ilova"

# ---------------------------------------------------------------
# Etalon to'plam (ZAIFLIKLAR.md bilan sinxron saqlanishi shart)
# Format: kod -> (fayl, qator, CWE, nom)
# ---------------------------------------------------------------
ETALON = {
    "Z-01": ("app.py", 30, "CWE-798", "Qattiq kodlangan SECRET_KEY"),
    "Z-02": ("app.py", 48, "CWE-89", "SQL inyeksiyasi (%-formatlash)"),
    "Z-03": ("app.py", 64, "CWE-79", "XSS / SSTI"),
    "Z-04": ("app.py", 73, "CWE-78", "Buyruq inyeksiyasi (subprocess)"),
    "Z-05": ("app.py", 90, "CWE-502", "Xavfsiz bo'lmagan yaml.load"),
    "Z-06": ("app.py", 100, "CWE-502", "pickle.loads"),
    "Z-07": ("app.py", 110, "CWE-94", "Kod inyeksiyasi (eval)"),
    "Z-08": ("app.py", 141, "CWE-78", "Buyruq inyeksiyasi (os.system)"),
    "Z-09": ("app.py", 148, "CWE-489", "debug=True"),
    "Z-10": ("app.py", 148, "CWE-605", "0.0.0.0 ga bog'lanish"),
    "Z-11": ("auth.py", 12, "CWE-798", "Qattiq kodlangan DB_PAROL"),
    "Z-12": ("auth.py", 16, "CWE-798", "Qattiq kodlangan API_KALIT"),
    "Z-13": ("auth.py", 25, "CWE-327", "MD5 parol uchun"),
    "Z-14": ("auth.py", 34, "CWE-89", "SQL inyeksiyasi (f-satr)"),
    "Z-15": ("auth.py", 50, "CWE-330", "random moduli token uchun"),
    "Z-16": ("auth.py", 57, "CWE-327", "SHA-1"),
    "Z-17": ("auth.py", 64, "CWE-617", "assert huquq tekshiruvi uchun"),
    "Z-18": ("utils.py", 21, "CWE-22", "Yo'l bo'ylab harakatlanish"),
    "Z-19": ("utils.py", 30, "CWE-78", "Buyruq inyeksiyasi (subprocess.run)"),
    "Z-20": ("utils.py", 37, "CWE-295", "verify=False"),
    "Z-21": ("utils.py", 45, "CWE-377", "tempfile.mktemp"),
    "Z-22": ("utils.py", 54, "CWE-532", "Parol jurnalda"),
    "Z-23": ("utils.py", 60, "CWE-732", "chmod 0o777"),
    "Z-24": ("utils.py", 65, "CWE-390", "E'tiborsiz istisno"),
}

# Qator raqamidagi ruxsat etilgan farq (vositalar blok boshini ko'rsatishi mumkin)
TOLERANS = 3

# ---------------------------------------------------------------
# Qo'lda tekshiruvdan o'tgan va yolg'on ijobiy deb TASDIQLANGAN topilmalar.
#
# Moslashtirish evristikasi bu topilmalarni yonidagi etalon yozuviga bog'lab
# yuborardi (ikkalasi ham bir funksiya tanasida), holbuki ular butunlay
# boshqa zaiflik sinfi haqida da'vo qiladi. Avtomatik qoida bilan ajratib
# bo'lmaydi — faqat qo'lda tahlil bilan. Har bir yozuvning sababi
# ZAIFLIKLAR.md ning 4-bo'limida batafsil keltirilgan.
#
# Format: (fayl, qator, qoida) -> qisqa sabab
# ---------------------------------------------------------------
TASDIQLANGAN_FP = {
    ("app.py", 91, "py/reflective-xss"): (
        "Flask ko'rinishidan qaytarilgan dict application/json javobiga "
        "aylanadi; brauzer uni HTML sifatida talqin qilmaydi"
    ),
    ("app.py", 101, "py/reflective-xss"): (
        "Flask ko'rinishidan qaytarilgan dict application/json javobiga "
        "aylanadi; brauzer uni HTML sifatida talqin qilmaydi"
    ),
}

# Qaysi yozuvlar haqiqatan ishlatilgani — qator raqamlari surilib ketsa,
# jimgina e'tibordan chetda qolmasligi uchun kuzatiladi.
ISHLATILGAN_FP: set[tuple] = set()


def bandit_oqish(yo_l: Path):
    """Bandit JSON chiqishini normallashtirish."""
    if not yo_l.exists():
        return []
    d = json.loads(yo_l.read_text(encoding="utf-8"))
    return [
        {
            "fayl": Path(r["filename"]).name,
            "qator": r["line_number"],
            "cwe": f"CWE-{r['issue_cwe']['id']}" if r.get("issue_cwe") else "-",
            "cwelar": {f"CWE-{r['issue_cwe']['id']}"} if r.get("issue_cwe") else set(),
            "qoida": r["test_id"],
            "jiddiylik": r["issue_severity"],
            "xabar": r["issue_text"],
        }
        for r in d.get("results", [])
    ]


def semgrep_oqish(yo_l: Path):
    """Semgrep JSON chiqishini normallashtirish."""
    if not yo_l.exists():
        return []
    d = json.loads(yo_l.read_text(encoding="utf-8"))
    natija = []
    for r in d.get("results", []):
        meta = r["extra"].get("metadata", {})
        cwe = meta.get("cwe", "-")
        if isinstance(cwe, list):
            cwe = cwe[0] if cwe else "-"
        kod = str(cwe).split(":")[0].strip()
        natija.append(
            {
                "fayl": Path(r["path"]).name,
                "qator": r["start"]["line"],
                "cwe": kod,
                "cwelar": {kod} if kod != "-" else set(),
                "qoida": r["check_id"].split(".")[-1],
                "jiddiylik": r["extra"].get("severity", "-"),
                "xabar": r["extra"].get("message", "").strip()[:90],
            }
        )
    return natija


def codeql_oqish(yo_l: Path):
    """CodeQL SARIF chiqishini normallashtirish.

    CWE kodlari qoida teglaridan olinadi: `external/cwe/cwe-022` -> `CWE-22`
    (boshidagi nollar olib tashlanadi, SARIF ularni uch xonali yozadi).
    """
    if not yo_l.exists():
        return []
    d = json.loads(yo_l.read_text(encoding="utf-8"))
    natija = []
    for ish in d.get("runs", []):
        qoidalar = {q["id"]: q for q in ish["tool"]["driver"].get("rules", [])}
        for r in ish.get("results", []):
            joy = r["locations"][0]["physicalLocation"]
            teglar = qoidalar.get(r["ruleId"], {}).get("properties", {}).get("tags", [])
            cwelar = []
            for teg in teglar:
                if "cwe-" in teg:
                    raqam = teg.rsplit("cwe-", 1)[1]
                    if raqam.isdigit():
                        cwelar.append(f"CWE-{int(raqam)}")
            xususiyat = qoidalar.get(r["ruleId"], {}).get("properties", {})
            natija.append(
                {
                    "fayl": Path(joy["artifactLocation"]["uri"]).name,
                    "qator": joy["region"]["startLine"],
                    "cwe": cwelar[0] if cwelar else "-",
                    "cwelar": set(cwelar),
                    "qoida": r["ruleId"],
                    "jiddiylik": xususiyat.get("problem.severity", r.get("level", "-")),
                    "xabar": r["message"]["text"].strip()[:90],
                }
            )
    return natija


# ---------------------------------------------------------------
# Funksiya chegaralarini aniqlash (moslashtirishning (b) sharti)
# ---------------------------------------------------------------
_oraliq_keshi: dict[str, list[tuple[int, int]]] = {}


def funksiya_oraliqlari(fayl: str) -> list[tuple[int, int]]:
    """Fayldagi funksiya tanalarining (boshlanish, tugash) qatorlari."""
    if fayl in _oraliq_keshi:
        return _oraliq_keshi[fayl]
    oraliqlar: list[tuple[int, int]] = []
    yo_l = OBYEKT / fayl
    if yo_l.exists():
        daraxt = ast.parse(yo_l.read_text(encoding="utf-8"), filename=str(yo_l))
        for tugun in ast.walk(daraxt):
            if isinstance(tugun, (ast.FunctionDef, ast.AsyncFunctionDef)):
                oraliqlar.append((tugun.lineno, tugun.end_lineno or tugun.lineno))
    _oraliq_keshi[fayl] = oraliqlar
    return oraliqlar


def ichki_funksiya(fayl: str, qator: int):
    """Qator joylashgan eng ichki funksiya oralig'i; modul darajasida None."""
    mos = [o for o in funksiya_oraliqlari(fayl) if o[0] <= qator <= o[1]]
    return min(mos, key=lambda o: o[1] - o[0]) if mos else None


def nomzodlar(t: dict) -> list[str]:
    """Topilma bog'lanishi mumkin bo'lgan etalon yozuvlar kodlari."""
    oraliq = ichki_funksiya(t["fayl"], t["qator"])
    natija = []
    for kod, (fayl, qator, _cwe, _nom) in ETALON.items():
        if t["fayl"] != fayl:
            continue
        # (a) qator yaqinligi
        if abs(t["qator"] - qator) <= TOLERANS:
            natija.append(kod)
        # (b) ayni bir funksiya tanasi
        elif oraliq and oraliq[0] <= qator <= oraliq[1]:
            natija.append(kod)
    return natija


def moslashtirish(topilmalar):
    """Topilmalarni etalon to'plam bilan solishtirish.

    Qaytaradi: (etalon kodi -> uni tasdiqlagan topilmalar ro'yxati,
                yolg'on ijobiy topilmalar ro'yxati)
    """
    # 0-o'tish: qo'lda tasdiqlangan yolg'on ijobiy natijalar chetga olinadi
    jadval = []
    qolda_fp = []
    for t in topilmalar:
        kalit = (t["fayl"], t["qator"], t["qoida"])
        if kalit in TASDIQLANGAN_FP:
            ISHLATILGAN_FP.add(kalit)
            qolda_fp.append(t)
        else:
            jadval.append((t, nomzodlar(t)))

    topilgan: dict[str, list[dict]] = {}

    # 1-o'tish: CWE kodi aniq mos kelgan va hali band bo'lmagan yozuvlar
    qolgan = []
    for t, nomz in jadval:
        mos = [k for k in nomz if ETALON[k][2] in t["cwelar"] and k not in topilgan]
        if mos:
            kod = min(mos, key=lambda k: abs(ETALON[k][1] - t["qator"]))
            topilgan.setdefault(kod, []).append(t)
        else:
            qolgan.append((t, nomz))

    # 2-o'tish: band bo'lmagan yozuvlar, so'ngra takroriy xabarlar
    yolgon = list(qolda_fp)
    for t, nomz in qolgan:
        if not nomz:
            yolgon.append(t)
            continue
        bosh = [k for k in nomz if k not in topilgan]
        tanlov = bosh or nomz
        kod = min(tanlov, key=lambda k: abs(ETALON[k][1] - t["qator"]))
        topilgan.setdefault(kod, []).append(t)

    return topilgan, yolgon


def metrikalar(topilgan, yolgon):
    """Precision, Recall, F1 hisoblash."""
    tp = len(topilgan)
    fp = len(yolgon)
    fn = len(ETALON) - tp
    takroriy = sum(len(v) for v in topilgan.values()) - tp
    p = tp / (tp + fp) if (tp + fp) else 0.0
    r = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) else 0.0
    return {
        "TP": tp,
        "FP": fp,
        "FN": fn,
        "Takroriy": takroriy,
        "Topilma": tp + takroriy + fp,
        "Precision": p,
        "Recall": r,
        "F1": f1,
    }


def main():
    manbalar = {
        "Bandit": bandit_oqish(NATIJA / "01-bandit.json"),
        "Semgrep (rasmiy)": semgrep_oqish(NATIJA / "02-semgrep.json"),
        "Semgrep (maxsus)": semgrep_oqish(NATIJA / "03-semgrep-maxsus.json"),
        "CodeQL": codeql_oqish(NATIJA / "05-codeql.sarif"),
    }

    hisob = {}
    for nom, topilmalar in manbalar.items():
        if not topilmalar:
            continue
        topilgan, yolgon = moslashtirish(topilmalar)
        hisob[nom] = {
            "topilgan": topilgan,
            "yolgon": yolgon,
            "metrika": metrikalar(topilgan, yolgon),
        }

    if not hisob:
        print("XATO: natija fayllari topilmadi. Avval tahlil.sh ni ishga tushiring.")
        return

    # Qo'lda tasdiqlangan FP ro'yxati kodga mos kelmay qolsa — ogohlantirish.
    # (Qator raqamlari surilganda yozuv jimgina ishlamay qo'yishi mumkin.)
    ishlatilmagan = set(TASDIQLANGAN_FP) - ISHLATILGAN_FP
    for kalit in sorted(ishlatilmagan):
        print(
            f"OGOHLANTIRISH: TASDIQLANGAN_FP yozuvi mos topilma topmadi: {kalit}. "
            "Qator raqami surilgan bo'lishi mumkin — tekshiring."
        )

    NATIJA.mkdir(parents=True, exist_ok=True)

    # --- Qiyosiy jadval ---
    q = ["# Qiyosiy jadval: zaifliklarning aniqlanishi\n"]
    q.append("| Kod | Fayl:qator | CWE | Zaiflik | " + " | ".join(hisob) + " |")
    q.append("|---|---|---|---|" + "---|" * len(hisob))
    for kod, (fayl, qator, cwe, nom) in ETALON.items():
        belgilar = ["+" if kod in h["topilgan"] else "-" for h in hisob.values()]
        q.append(f"| {kod} | {fayl}:{qator} | {cwe} | {nom} | " + " | ".join(belgilar) + " |")
    q.append("\n`+` — aniqlandi, `-` — o'tkazib yuborildi\n")
    (NATIJA / "qiyosiy-jadval.md").write_text("\n".join(q), encoding="utf-8")

    # --- Metrikalar ---
    m = ["# Aniqlik metrikalari\n"]
    m.append(f"Etalon to'plamdagi zaifliklar soni: **{len(ETALON)}**\n")
    m.append("| Vosita | Topilma | TP | Takroriy | FP | FN | Precision | Recall | F1 |")
    m.append("|---|---|---|---|---|---|---|---|---|")
    for nom, h in hisob.items():
        x = h["metrika"]
        m.append(
            f"| {nom} | {x['Topilma']} | {x['TP']} | {x['Takroriy']} | {x['FP']} | "
            f"{x['FN']} | {x['Precision']:.2f} | {x['Recall']:.2f} | {x['F1']:.2f} |"
        )
    m.append(
        "\n`Topilma` — vosita bergan xabarlar soni; `TP` — tasdiqlangan etalon\n"
        "zaifliklar soni; `Takroriy` — ayni bir zaiflik haqidagi qo'shimcha\n"
        "xabarlar (metrikaga kirmaydi); `FP` — etalonda mavjud bo'lmagan joyga\n"
        "berilgan xabarlar.\n"
    )
    m.append("\n## Yolg'on ijobiy natijalar\n")
    for nom, h in hisob.items():
        m.append(f"\n### {nom} ({len(h['yolgon'])} ta)\n")
        if not h["yolgon"]:
            m.append("- yo'q")
        for y in h["yolgon"]:
            m.append(f"- `{y['fayl']}:{y['qator']}` — {y['qoida']}: {y['xabar'][:70]}")
    (NATIJA / "metrikalar.md").write_text("\n".join(m), encoding="utf-8")

    # --- Topilma-etalon moslashtirish jurnali (B ilovasi uchun) ---
    s = ["# Topilmalarning etalon to'plam bilan moslashtirilishi\n"]
    s.append(
        "Har bir vosita xabarining qaysi etalon zaiflikka bog'langani.\n"
        "`FP` — hech qaysi etalon yozuviga bog'lanmagan xabar.\n"
    )
    for nom, h in hisob.items():
        s.append(f"\n## {nom}\n")
        s.append("| Fayl:qator | Qoida | Vosita CWE | Bog'landi | Etalon CWE |")
        s.append("|---|---|---|---|---|")
        qatorlar = []
        for kod, topilmalar in h["topilgan"].items():
            for t in topilmalar:
                qatorlar.append((t["fayl"], t["qator"], t["qoida"], t["cwe"], kod, ETALON[kod][2]))
        for y in h["yolgon"]:
            qatorlar.append((y["fayl"], y["qator"], y["qoida"], y["cwe"], "FP", "—"))
        for fayl, qator, qoida, cwe, kod, e_cwe in sorted(qatorlar):
            s.append(f"| {fayl}:{qator} | `{qoida}` | {cwe} | {kod} | {e_cwe} |")
    (NATIJA / "moslashtirish.md").write_text("\n".join(s), encoding="utf-8")

    # --- Konsolga chiqarish ---
    print(f"Etalon: {len(ETALON)} ta zaiflik\n")
    bosh = f"{'Vosita':20} {'Top':>4} {'TP':>4} {'Takr':>5} {'FP':>4} {'FN':>4}"
    print(bosh + f" {'Prec':>7} {'Recall':>7} {'F1':>7}")
    print("-" * 70)
    for nom, h in hisob.items():
        x = h["metrika"]
        print(
            f"{nom:20} {x['Topilma']:>4} {x['TP']:>4} {x['Takroriy']:>5} "
            f"{x['FP']:>4} {x['FN']:>4} "
            f"{x['Precision']:>7.2f} {x['Recall']:>7.2f} {x['F1']:>7.2f}"
        )
    print("\nO'tkazib yuborilgan zaifliklar:")
    for nom, h in hisob.items():
        yoq = [k for k in ETALON if k not in h["topilgan"]]
        print(f"  {nom:20} {', '.join(yoq) if yoq else 'yo‘q'}")
    print(f"\nFayllar yozildi: {NATIJA}")


if __name__ == "__main__":
    main()
