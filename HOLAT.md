# Ish holati

Oxirgi yangilanish: 2026-10-26

---

## Tayyor

- [x] Loyiha tuzilmasi va CLAUDE.md
- [x] Tasdiqlangan reja (reja.md), bet taqsimoti bilan
- [x] Sinov obyekti: zaif Flask ilovasi (24 ta zaiflik, 15 CWE)
- [x] Etalon to'plam jadvali (ZAIFLIKLAR.md), qator raqamlari tekshirilgan
- [x] Maxsus Semgrep qoidalari (5 ta), sinovdan o'tgan
- [x] Tahlil skripti (tahlil.sh), 5 bosqich
- [x] Metrikalar hisoblagichi (hisobot.py), sinovdan o'tgan
- [x] GitHub Actions workflow (yozilgan, hali sinovdan o'tmagan)
- [x] Adabiyotlar ro'yxati — boshlang'ich 14 ta manba
- [x] Virtual muhit (`.venv`), uchta Python vositasi o'rnatildi
- [x] Uchala modulning sintaksis tekshiruvi (`py_compile`) — xatosiz
- [x] ETALON qator raqamlari kod bilan solishtirildi — 24/24 mos
- [x] `tahlil.sh` to'liq ishga tushirildi (5/5 bosqich)
- [x] pip-audit natijalari olindi (43 noyob zaiflik, 6 paket)
- [x] `hisobot.py` moslashtirish mantiqi tuzatildi (M-1, M-2)
- [x] CodeQL CLI o'rnatildi (2.27.3), `python-security-extended` bilan tahlil
- [x] `hisobot.py` CodeQL SARIF chiqishini o'qiydi
- [x] To'rtta vosita bo'yicha yakuniy metrikalar olindi
- [x] Loyiha GitHub ga yuklandi (ochiq ombor `nyxeldev/kurs-ishi-sast`)
- [x] `sast.yml` workflow sinovdan o'tdi, ikki nuqson tuzatildi
- [x] GitHub Security tab natijalari olindi (70 ogohlantirish)
- [x] Diagrammalar yasaldi (`diagramma.py`, natija fayllaridan hisoblanadi)

## Bajarilishi kerak

### Amaliy qism (Claude Code)
- [ ] Skrinshotlar: har bir vosita chiqishi, GitHub Security tabi
- [ ] M-4, M-5, M-7, M-8 bo'yicha qarorlar (pastda)

### Matn (Cowork)
- [ ] 01-bob (11 bet)
- [ ] 02-bob (13 bet)
- [ ] 03-bob (14 bet) — amaliy qism tugagach
- [ ] 00-kirish (3 bet)
- [ ] 04-xulosa (2 bet)
- [ ] Adabiyotlarni 20-25 ta ga yetkazish
- [ ] Yakuniy .docx hujjat

---

## Sinov muhiti

Manba: `kod/natijalar/00-muhit.txt`

| Komponent | Versiya |
|---|---|
| OS | Windows 11 Pro 10.0.26200 |
| Qobiq | Git Bash (MINGW64_NT-10.0-26200) |
| Python | 3.14.3 |
| Bandit | 1.9.4 |
| Semgrep | 1.182.1 |
| pip-audit | 2.10.1 |
| CodeQL | 2.27.3 |

> DIQQAT: CLAUDE.md da amaliy qism tili Python 3.12 deb belgilangan, lekin
> sinov mashinasida faqat 3.14.3 va 3.13 mavjud. Barcha o'lchovlar 3.14.3
> da olingan va ishda shu versiya keltiriladi.

CodeQL CLI loyihadan tashqarida, `C:\Users\Analyst\vositalar\codeql` ga
o'rnatilgan — rasmiy `github/codeql-action` relizidagi
`codeql-bundle-win64.tar.gz` (667 MB), SHA-256 nazorat summasi tekshirilgan.
Ma'lumotlar bazasi `kod/natijalar/codeql-db` (26 MB), `.gitignore` ga
kiritilgan.

### Ishlash vaqti

Manba: `kod/natijalar/00-vaqt.txt`

| Bosqich | Vaqt |
|---|---|
| Bandit | 1 s |
| Semgrep (rasmiy qoidalar) | 173 s |
| Semgrep (maxsus qoidalar) | 260 s |
| pip-audit | 3 s |
| CodeQL — baza yaratish | 12 s |
| CodeQL — tahlil (`security-extended`, 52 so'rov) | 2761 s |

CodeQL tahlilining 1514 soniyasi (25 daqiqa) bitta so'rovga —
`CWE-502/UnsafeDeserialization` ga ketdi.

> DIQQAT (M-8): bu raqamni CodeQL ning o'ziga xos qiymati deb keltirish
> mumkin emas. Ayni shu tahlil GitHub Actions ubuntu-latest ishchisida
> **39 soniyada** tugadi — lokal Windows o'lchoviga qaraganda ~70 barobar
> tez. Sabab tekshirilmagan (platforma, protsessor, disk tezligi yoki
> antivirus ta'siri bo'lishi mumkin). Ishda vaqt qiyoslashi uchun CI
> o'lchovlari ishlatilishi tavsiya etiladi, lokal raqam esa "bir xil
> so'rov muhitga qarab necha barobar farq qilishi" misoli sifatida
> keltirilsa to'g'ri bo'ladi.

---

## Natijalar

Manba: `kod/natijalar/metrikalar.md`, `kod/natijalar/qiyosiy-jadval.md`,
`kod/natijalar/moslashtirish.md` (`hisobot.py` chiqishi, 2026-10-26).

### SAST vositalari

| Vosita | Topilma | TP | Takroriy | FP | FN | Precision | Recall | F1 |
|---|---|---|---|---|---|---|---|---|
| Bandit | 22 | 19 | 0 | 3 | 5 | 0.86 | 0.79 | **0.83** |
| Semgrep (rasmiy) | 26 | 15 | 10 | 1 | 9 | 0.94 | 0.62 | 0.75 |
| Semgrep (maxsus) | 5 | 5 | 0 | 0 | 19 | 1.00 | 0.21 | 0.34 |
| CodeQL | 17 | 14 | 3 | 0 | 10 | **1.00** | 0.58 | 0.74 |

Etalon to'plam: 24 ta zaiflik.

### O'tkazib yuborilgan zaifliklar

| Vosita | O'tkazib yuborilganlar |
|---|---|
| Bandit | Z-03, Z-11, Z-12, Z-18, Z-22 |
| Semgrep (rasmiy) | Z-11, Z-12, Z-14, Z-15, Z-17, Z-18, Z-21, Z-22, Z-24 |
| Semgrep (maxsus) | qolgan 19 ta (qoidalar to'plami ataylab tor) |
| CodeQL | Z-01, Z-10, Z-11, Z-12, Z-13, Z-15, Z-16, Z-17, Z-22, Z-24 |

### Vositalarni birgalikda qo'llash

| Kombinatsiya | Qoplama |
|---|---|
| Bandit yolg'iz | 19 / 24 |
| Bandit + CodeQL | 21 / 24 |
| Bandit + maxsus qoidalar | 23 / 24 |
| **Bandit + CodeQL + maxsus qoidalar** | **24 / 24** |

Hech bir vosita yolg'iz 19 tadan ko'pini topmadi, uchtasi birgalikda esa
to'liq qoplama beradi. Bu xulosa bobining asosiy dalili.

### Diagrammalar

`kod/tahlil/diagramma.py` ikkita rasmni yasaydi. Raqamlar `hisobot.py` ning
moslashtirish mantiqidan olinadi — diagrammada qo'lda kiritilgan qiymat yo'q,
vositalar chiqishi o'zgarsa rasm ham o'zgaradi.

| Fayl | Mazmuni | Taklif qilinadigan nom |
|---|---|---|
| `kod/natijalar/rasm-1-aniqlash-ulushi.png` | har bir vositaning aniqlash ulushi | 3.1-rasm. Vositalarning etalon zaifliklarni aniqlash ulushi |
| `kod/natijalar/rasm-2-birgalikda-qamrov.png` | kombinatsiyalar bo'yicha qamrov | 3.2-rasm. Vositalarni birgalikda qo'llashdagi qamrov |

Har bir rasm PNG (300 dpi, Word uchun) va SVG (vektor) ko'rinishida
saqlanadi. Rasm nomi rasm ichiga yozilmagan — kurs ishida u rasm ostida
matn sifatida beriladi (CLAUDE.md, formatlash qoidasi). Raqamlash
3-bobdagi rasmlar tartibiga qarab aniqlanadi.

Chizma yechimlari: bitta o'lchov — bitta rang, 0 dan 24 gacha qat'iy o'q
(ulushni ko'z bilan solishtirish uchun), ingichka panjara, ingichka to'r,
har bir panjara uchida to'g'ridan-to'g'ri yozuv. 2-rasmda urg'u naqshi
ishlatilgan: to'liq qamrovga erishgan kombinatsiya ko'k, qolganlari
kulrang — ma'no rangga tayanmaydi, chunki barcha qiymatlar yozib
qo'yilgan.

### SCA (pip-audit)

| Paket | Versiya | Noyob zaiflik |
|---|---|---|
| flask | 0.12.2 | 4 |
| jinja2 | 2.10 | 6 |
| pyyaml | 5.1 | 3 |
| requests | 2.19.1 | 5 |
| urllib3 | 1.24.1 | 13 |
| werkzeug | 0.14.1 | 12 |
| **Jami** | **6 paket** | **43** |

pip-audit konsolda "82 known vulnerabilities" deb xabar beradi, chunki bir
xil PYSEC identifikatori ikki manbadan (PyPI advisory DB va OSV) ikki marta
qaytariladi. Noyob identifikatorlar soni — 43. Ishda 43 raqami keltiriladi.

---

## CI/CD natijalari (3.5-band)

Ombor: <https://github.com/nyxeldev/kurs-ishi-sast> (ochiq).
Oxirgi ish: <https://github.com/nyxeldev/kurs-ishi-sast/actions/runs/40226842276>

### Workflow ishlari

| Ish | Natija | Vaqt | Izoh |
|---|---|---|---|
| Bandit tahlili | xato | 20 s | tahlil va SARIF yuklash muvaffaqiyatli, **sifat darvozasi** ataylab to'xtatdi |
| Semgrep tahlili | muvaffaqiyatli | 45 s | ikkita SARIF yuklandi (rasmiy + maxsus) |
| CodeQL tahlili | muvaffaqiyatli | 39 s | `security-extended` |
| Bog'liqliklar tahlili | xato | 13 s | hisobot va artefakt muvaffaqiyatli, **sifat darvozasi** to'xtatdi |
| Umumiy hisobot | muvaffaqiyatli | 5 s | `$GITHUB_STEP_SUMMARY` jadvali |

Ikkala xato ham ataylab: sifat darvozalari yuqori jiddiylikdagi topilma
(Bandit) va zaif bog'liqlik (pip-audit) borligida qurilishni to'xtatadi.
Barcha tahlil va SARIF yuklash bosqichlari muvaffaqiyatli o'tdi.

### GitHub Security tab (kod skanerlash ogohlantirishlari)

| Vosita | Kategoriya | Ogohlantirish |
|---|---|---|
| Semgrep OSS | `semgrep` | 26 |
| Bandit | `bandit` | 22 |
| CodeQL | `codeql-python` | 17 |
| Semgrep OSS | `semgrep-maxsus` | 5 |
| **Jami** | | **70** |

Raqamlar lokal ishga tushirish natijalariga **to'liq mos keldi** (26, 22,
17, 5) — CI va lokal muhit bir xil topilmalarni beradi. Bu amaliy qismning
takrorlanuvchanligini tasdiqlaydi.

### Workflow da topilgan va tuzatilgan nuqsonlar

Birinchi ish ikki haqiqiy nuqsonni ko'rsatdi:

1. **pip-audit ishi `ResolutionImpossible` bilan yiqildi.** `requirements.txt`
   dagi versiyalar ataylab ziddiyatli (`requests 2.19.1` → `urllib3<1.24`,
   lekin `urllib3==1.24.1` qadalgan). `--no-deps --disable-pip` qo'shildi.
2. **Maxsus qoidalar natijasi tashlab yuborilardi.** `semgrep-maxsus.sarif`
   yaratilar, lekin yuklash bosqichi faqat `semgrep.sarif` ni oladi edi —
   3.4-bandning asosiy natijasi Security tabiga yetib bormasdi. Alohida
   kategoriya bilan yuklash qo'shildi.

Uchinchi nuqson emas, lekin tuzatildi: SCA sifat darvozasi hisobot olish
bosqichining ichida edi va xato kutilganmi yoki yo'qmi, ajratib bo'lmasdi.
Endi Bandit ishidagi kabi alohida "Sifat darvozasi" bosqichi.

---

## Muhim kuzatuvlar

**1. Z-18 ni faqat CodeQL topdi.**
Yo'l bo'ylab harakatlanish zaifligida manba `request.args.get` (app.py:117)
va cho'kma `os.path.join` (utils.py:21) turli modullarda joylashgan.
Bandit, Semgrep ning rasmiy qoidalari va hatto shu zaiflik uchun atayin
yozilgan maxsus qoida ham topmadi — Semgrep OSS modullararo zaharlangan
ma'lumot oqimini kuzatmaydi. CodeQL `py/path-injection` qoidasi bilan
utils.py:22 da aniqladi. Bu semantik tahlilning shablon asosidagi tahlildan
ustunligini ko'rsatadigan eng toza misol (2.2-band).

**2. CodeQL eng aniq, lekin eng tor qamrovli.**
Precision 1.00 — bitta ham yolg'on ijobiy natija bermadi. Ammo Recall
faqat 0.58: qattiq kodlangan sirlar (Z-01, Z-11, Z-12), zaif xesh
funksiyalari (Z-13, Z-16), `random` moduli (Z-15), `assert` (Z-17),
jurnalga maxfiy ma'lumot (Z-22), e'tiborsiz istisno (Z-24) va 0.0.0.0 ga
bog'lanish (Z-10) — bularning hech biri `security-extended` to'plamiga
kirmaydi. Bandit bu "oddiy shablon" zaifliklarini 1 soniyada topadi.
Xulosa: chuqur tahlil keng qamrovni almashtirmaydi, to'ldiradi.

**3. Bandit ning sirlarni aniqlash qoidasi tilga bog'liq.**
Inglizcha `SECRET_KEY` (Z-01) `B105` bilan topildi, o'zbekcha `DB_PAROL`
(Z-11) va `API_KALIT` (Z-12) topilmadi. Semgrep ning rasmiy qoidalari va
CodeQL ham ikkisini topmadi — uchala xalqaro vosita o'zbekcha nomlangan
sirlarni ko'rmadi. Maxsus qoida (`ozbekcha-qattiq-kodlangan-sir`)
ikkalasini ham aniqladi. Bu 3.4-bandning asosiy argumenti va ishning eng
original natijasi.

**4. Semgrep rasmiy qoidalari etalondan tashqari haqiqiy zaiflik topdi.**
`app.py:129` — `redirect("/profil?ism=" + login)`, ochiq qayta yo'naltirish
(open redirect, CWE-601). Etalon ro'yxatda yo'q, shu sababli yolg'on
ijobiy natija deb hisoblandi. Aslida bu haqiqiy zaiflik (M-4).

**5. Yolg'on ijobiy natijalarning tabiati.**
Bandit ning 3 ta FP si — `import pickle` (app.py:17) va `import subprocess`
(app.py:19, utils.py:8) uchun B403/B404 ogohlantirishlari; import o'zi
zaiflik emas. Semgrep ning yagona FP si — yuqoridagi open redirect.
CodeQL da FP yo'q.

**6. Takroriy xabarlar soni vositaga qarab keskin farqlanadi.**
Semgrep (rasmiy): 26 xabardan 10 tasi takroriy — Z-04 uchun uchta qoida
(`dangerous-subprocess-use`, `subprocess-injection`, `subprocess-shell-true`)
bir vaqtda ishlaydi. CodeQL: 17 dan 3 tasi. Bandit: 0 ta. Deduplikatsiyasiz
Precision sun'iy pasayadi, shu sababli `hisobot.py` takroriy xabarlarni
alohida ustunda hisoblaydi (2.4-band, alert fatigue).

**7. Vositalar bir zaiflikka turli CWE kodini beradi.**
0.0.0.0 ga bog'lanish: Bandit `B104` → CWE-605, Semgrep → CWE-668.
`SECRET_KEY`: Bandit `B105` → CWE-259, etalon → CWE-798. SQL inyeksiyasi:
Semgrep `tainted-sql-string` → CWE-704. CodeQL bitta qoidaga bir necha kod
beradi: `py/path-injection` → CWE-22, 23, 36, 73, 99. Demak CWE bo'yicha
normallashtirish avtomatik emas; `hisobot.py` shu sababli CWE kodlari
to'plami bilan ishlaydi.

**8. GitHub ning sir skanerlash himoyasi push ni bloklab qo'ydi.**
Birinchi `git push` urinishi `GH013: Repository rule violations` bilan rad
etildi: push protection `auth.py:16` dagi `sk_live_4f3c...` qiymatini
**Stripe API kaliti** deb tanidi. Himoya statik tahlil vositalarigacha,
kod omborga tushishidan oldin ishladi — SAST emas, oldini olish nazorati.
Blokni chetlab o'tish mumkin edi (GitHub maxsus havola beradi), lekin
qalbaki qiymat haqiqiy provayder formatiga taqlid qilgani uchun uni
`QALBAKI-API-KALITI-kurs-ishi-2026` ga almashtirish to'g'riroq bo'ldi.
Qator raqami o'zgarmadi, metrikalar ham o'zgarmadi (maxsus qoida
o'zgaruvchi nomi bo'yicha ishlaydi, qiymat bo'yicha emas — qayta ishga
tushirib tasdiqlandi).

Bu 1.2-band (zaifliklarni aniqlash usullari) va 3.5-band uchun qiymatli
misol: sirlarni skanerlash SAST dan alohida nazorat turi bo'lib, kodni
tahlil qilmasdan, faqat shablon bo'yicha ishlaydi va eng arzon bosqichda —
commit/push paytida — to'xtatadi.

---

## Moslashtirish metodikasi

`hisobot.py` topilmani etalon zaiflikka ikki shartdan biri bajarilganda
bog'laydi: (a) qator farqi TOLERANS = 3 dan oshmasa, yoki (b) topilma ham,
etalon zaiflik ham ayni bir funksiya tanasida joylashgan bo'lsa. Modul
darajasidagi topilmalarga faqat (a) qo'llanadi — shu sababli fayl boshidagi
`import` ogohlantirishlari yolg'on ijobiy bo'lib qoladi.

Bir topilma ko'pi bilan bitta etalon yozuviga bog'lanadi; bitta etalon
zaiflikni bir necha topilma tasdiqlashi mumkin. Bir qatorda bir nechta
etalon zaiflik bo'lsa (Z-09 va Z-10 — app.py:148), topilmalar avval CWE
kodi bo'yicha, so'ngra band bo'lmagan yozuvlar bo'yicha taqsimlanadi.

Har bir xabarning qaysi etalon yozuviga bog'langani
`kod/natijalar/moslashtirish.md` da to'liq keltirilgan — B ilovasiga
kiritiladi va metrikalarni qo'lda tekshirish imkonini beradi.

---

## Ochiq masalalar

**M-1 (hal qilindi).** Bir qatordagi ikki zaiflik (Z-09, Z-10) uchun ikki
o'tishli taqsimlash kiritildi.

**M-2 (hal qilindi).** Takroriy xabarlar yolg'on ijobiy deb sanalmaydi;
funksiya chegarasi bo'yicha moslashtirish kiritildi.

**M-3 (hal qilindi).** CodeQL lokal CLI orqali ishga tushirildi, natija
`kod/natijalar/05-codeql.sarif` da.

**M-4. Etalon to'plamda open redirect (CWE-601) yo'q.** Z-25 sifatida
qo'shish yoki ataylab qoldirilmagan zaiflik deb izohlash kerak — qarori
qabul qilinmagan.

**M-5. CodeQL ning uchta takroriy xabari aslida alohida masala.**
`py/reflective-xss` app.py:91 va app.py:101 da ishga tushdi — bu
`yaml.load` va `pickle.loads` natijasining javobga qaytarilishi, ya'ni
Z-05/Z-06 dan farqli zaiflik. Moslashtirish ularni ayni bir funksiyadagi
etalon yozuvga bog'lab, takroriy deb hisobladi. FP ga aylantirish CodeQL
ning Precision ini noo'rin pasaytirardi, shu sababli hozircha takroriy
sifatida qoldirildi. Ishda izohlash kerak.

**M-6 (hal qilindi).** Loyiha ochiq ombor sifatida GitHub ga yuklandi
(`nyxeldev/kurs-ishi-sast`), workflow uch marta ishga tushdi, ikki nuqson
tuzatildi, Security tab natijalari olindi.

**M-7. CodeQL Action v3 2026-yil dekabrda eskiradi.** Workflow ogohlantirish
beradi: `codeql-action/init@v3`, `analyze@v3` va `upload-sarif@v3` ni v4 ga
o'tkazish kerak. Hozir ishlaydi, shu sababli tegilmadi — ishni topshirish
muddatiga qarab qaror qilinadi.

**M-8. Vaqt o'lchovlari muhitga juda bog'liq.** Ayni bir CodeQL tahlili
lokal Windows muhitida 2761 soniya, GitHub Actions ishchisida 39 soniya —
~70 barobar farq. Sabab aniqlanmagan. Ishda vaqt jadvalini qaysi muhit
bo'yicha keltirish kerakligi hal qilinmagan.

**M-9. Ombor ochiq.** Ataylab zaif kod `nyxeldev/kurs-ishi-sast` da
hammaga ko'rinadi — bu kod skanerlashni bepul ishlatish uchun zarur edi
(yopiq omborda GitHub Advanced Security talab qilinadi). Ish topshirilgach
omborni yopiq qilish mumkin, lekin shunda Security tab natijalari
ko'rinmay qoladi — skrinshotlar oldin olinishi kerak.

> SAST qismi to'liq: to'rtta vosita, o'lchangan metrikalar, to'liq
> moslashtirish jurnali va ishlaydigan CI/CD quvuri. Qolgani — diagramma,
> skrinshotlar va matn.
