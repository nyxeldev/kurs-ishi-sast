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
- [x] M-4 tekshirildi: open redirect topilmasi tasdiqlangan yolg'on ijobiy
      natija ekani aniqlanib, hujjatlashtirildi (etalon 24 ta bo'lib qoldi)
- [x] M-8 tekshirildi: vaqt farqi kesh bilan izohlanib, xato xulosa olib
      tashlandi
- [x] M-5 tekshirildi: CodeQL ning ikki `reflective-xss` topilmasi yolg'on
      ijobiy deb tasniflandi (`TASDIQLANGAN_FP` ro'yxati)
- [x] CodeQL Action v3 dan v4 ga o'tkazildi va sinovdan o'tdi (M-7)

## Bajarilishi kerak

### Amaliy qism (Claude Code)
- [ ] Skrinshotlar: har bir vosita chiqishi, GitHub Security tabi
- [ ] M-9, M-10 bo'yicha qarorlar (pastda)

### Matn (Cowork)
- [x] 01-bob (11 bet) — yozildi, 3667 so'z, 24 ta manbaga havola
- [x] 02-bob — yozildi, 1477 so'z, 6 bet (rejada 13 bet edi; hajm
      ataylab qisqartirildi, M-17 ga qarang). Bitta jadval, 2.1-2.5
      bandlar, har bandda xulosa. Olti yangi manba qo'shildi.
- [x] 03-bob (14 bet) — yozildi, 5854 so'z, 15 jadval, 2 rasm.
      Barcha raqamlar `kod/natijalar/` dan skript bilan qayta tekshirilgan.
      DIQQAT: hajm rejadagidan katta (taxminan 16-17 bet), .docx yig'ishda
      qisqartirish kerak bo'lishi mumkin.
- [x] 00-kirish (3 bet) — yozildi, 1068 so'z. Olti vazifa belgilandi,
      har biri aniq bandlarga bog'langan. Yangi manba qo'shilmadi.
- [x] 04-xulosa (2 bet) — yozildi, 941 so'z (~2,8 bet). Vazifa -> natija
      tuzilmasi, yangi fakt va yangi manba yo'q, havola ishlatilmagan.
- [x] Adabiyotlarni 20-25 ta ga yetkazish — 26 ta real manba tasdiqlandi
      (+ II/III bob uchun 5 ta o'rin band qilingan)
- [x] Yakuniy .docx hujjat — `ilovalar/kurs-ishi.docx` yig'ildi
      (titul, mundarija, kirish, 3 bob, xulosa, adabiyotlar; 18 jadval,
      2 rasm). Formatlash Word COM orqali tekshirilgan.
      **DIQQAT: 58 bet chiqdi, CLAUDE.md dagi chegara 35-45 bet.**
      Batafsil pastdagi M-14 da.

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

| Bosqich | Birinchi ishga tushirish | Takroriy ishga tushirish | GitHub Actions |
|---|---|---|---|
| Bandit | 1 s | 2 s | 20 s |
| Semgrep (rasmiy qoidalar) | 173 s | 11 s | 45 s |
| Semgrep (maxsus qoidalar) | 260 s | 7 s | (yuqoridagi ish ichida) |
| pip-audit | 3 s | 5 s | 13 s |
| CodeQL (baza + `security-extended`) | 2773 s | 57 s | 39 s |

Lokal ustunlar — `kod/natijalar/00-vaqt.txt`; CI ustuni — ish (job)
davomiyligi, unga `checkout` va muhitni tayyorlash ham kiradi.

**Birinchi va takroriy ishga tushirish farqi hal qiluvchi ahamiyatga ega.**
Birinchi ishda Semgrep qoidalar bazasini tarmoqdan yuklab oladi, CodeQL esa
so'rovlarni kompilyatsiya qiladi: `CWE-502/UnsafeDeserialization` so'rovi
birinchi safar 1514 soniya (25 daqiqa), ikkinchi safar 12 soniya ishladi.
Kesh isigach CodeQL ning to'liq tahlili 2773 dan 57 soniyaga tushdi —
48 barobar.

> TUZATISH (M-8 yopildi): HOLAT.md ning avvalgi tahririda "CodeQL Bandit
> dan ~2770 barobar sekin" degan xulosa bor edi. **Bu noto'g'ri.** O'sha
> raqam tahlil narxini emas, bir martalik tayyorgarlik narxini o'lchagan.
> Ushbu 3 modulli, ~290 qatorli sinov obyektida kesh isiganidan keyin
> to'rtala vosita ham soniyalar ichida tugaydi va ular orasidagi tezlik
> farqi amaliy ahamiyatga ega emas. "Chuqur tahlil sekin" degan tezisni
> bu korpusda umuman tekshirib bo'lmaydi — buning uchun ancha katta kod
> bazasi kerak. Ishda shu cheklov ochiq aytilishi shart (2.2-band).

---

## Natijalar

Manba: `kod/natijalar/metrikalar.md`, `kod/natijalar/qiyosiy-jadval.md`,
`kod/natijalar/moslashtirish.md` (`hisobot.py` chiqishi, 2026-10-26).

### SAST vositalari

| Vosita | Topilma | TP | Takroriy | FP | FN | Precision | Recall | F1 |
|---|---|---|---|---|---|---|---|---|
| Bandit | 22 | 19 | 0 | 3 | 5 | 0.86 | **0.79** | **0.83** |
| Semgrep (rasmiy) | 26 | 15 | 10 | 1 | 9 | 0.94 | 0.62 | 0.75 |
| Semgrep (maxsus) | 5 | 5 | 0 | 0 | 19 | 1.00 | 0.21 | 0.34 |
| CodeQL | 17 | 14 | 1 | 2 | 10 | 0.88 | 0.58 | 0.70 |

Etalon to'plam: 24 ta zaiflik.

CodeQL ning ikkita FP si qo'lda tekshiruvdan keyin shunday tasniflandi
(M-5): `py/reflective-xss` qoidasi `app.py:91` va `app.py:101` da ishga
tushgan, lekin u yerda javob `application/json` — batafsil
`ZAIFLIKLAR.md` ning 4.2-bandida. Avval ular takroriy xabar deb
hisoblanardi va CodeQL Precision i 1.00 ko'rinardi.

Keng qamrovli qoidalar to'plamiga ega uch vositaning hech biri mukammal
aniqlikka erishmadi. 1.00 ko'rsatkichi faqat maxsus qoidalarda — ular
ataylab tor yozilgani uchun.

### O'tkazib yuborilgan zaifliklar

| Vosita | O'tkazib yuborilganlar |
|---|---|
| Bandit | Z-03, Z-11, Z-12, Z-18, Z-22 |
| Semgrep (rasmiy) | Z-11, Z-12, Z-14, Z-15, Z-17, Z-18, Z-21, Z-22, Z-24 |
| Semgrep (maxsus) | qolgan 19 ta (qoidalar to'plami ataylab tor) |
| CodeQL | Z-01, Z-10, Z-11, Z-12, Z-13, Z-15, Z-16, Z-17, Z-22, Z-24 |

### Vositalarni birgalikda qo'llash

Ochko'z (greedy) tartib — har qadamda eng ko'p yangi zaiflik qo'shadigan
vosita:

| Qadam | Qoplama |
|---|---|
| Bandit | 19 / 24 |
| + Semgrep (maxsus qoidalar) | 23 / 24 |
| **+ CodeQL** | **24 / 24** |

Hech bir vosita yolg'iz 19 tadan ko'pini topmadi, uchtasi birgalikda esa
to'liq qoplama beradi. Bu xulosa bobining asosiy dalili.

Semgrep ning rasmiy qoidalari bu ketma-ketlikka kirmadi: ular topgan 15 ta
zaiflikning hammasini yuqoridagi uchlik allaqachon qamrab oladi. Bu
"ko'proq vosita — ko'proq qoplama" degan sodda qoidani rad etadi: qo'shimcha
vosita faqat boshqalar ko'rmaydigan sinf zaifliklarni topsagina qiymat
qo'shadi.

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
ishlatilgan: to'liq qamrovga erishgan qadam ko'k, qolganlari kulrang —
ma'no rangga tayanmaydi, chunki barcha qiymatlar yozib qo'yilgan.

2-rasmdagi ketma-ketlik qo'lda yozilmagan, ochko'z (greedy) tartibda
hisoblanadi: har qadamda etalonga eng ko'p YANGI zaiflik qo'shadigan vosita
tanlanadi, hech narsa qo'shmaydigani esa diagrammaga umuman kirmaydi.
Shuning uchun Semgrep ning rasmiy qoidalari rasmda yo'q — ular topgan
hamma narsa Bandit, maxsus qoidalar va CodeQL uchligida allaqachon bor.

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
Oxirgi ish: <https://github.com/nyxeldev/kurs-ishi-sast/actions/runs/40238306488>
(CodeQL Action v4 bilan)

### Workflow ishlari

| Ish | Natija | Vaqt | Izoh |
|---|---|---|---|
| Bandit tahlili | xato | 19 s | tahlil va SARIF yuklash muvaffaqiyatli, **sifat darvozasi** ataylab to'xtatdi |
| Semgrep tahlili | muvaffaqiyatli | 38 s | ikkita SARIF yuklandi (rasmiy + maxsus) |
| CodeQL tahlili | muvaffaqiyatli | 51 s | `security-extended` |
| Bog'liqliklar tahlili | xato | 18 s | hisobot va artefakt muvaffaqiyatli, **sifat darvozasi** to'xtatdi |
| Umumiy hisobot | muvaffaqiyatli | 6 s | `$GITHUB_STEP_SUMMARY` jadvali |

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

**2. CodeQL eng chuqur, lekin eng tor qamrovli.**
Recall atigi 0.58: qattiq kodlangan sirlar (Z-01, Z-11, Z-12), zaif xesh
funksiyalari (Z-13, Z-16), `random` moduli (Z-15), `assert` (Z-17),
jurnalga maxfiy ma'lumot (Z-22), e'tiborsiz istisno (Z-24) va 0.0.0.0 ga
bog'lanish (Z-10) — bularning hech biri `security-extended` to'plamiga
kirmaydi. Bandit bu "oddiy shablon" zaifliklarini 1-2 soniyada topadi.
Xulosa: chuqur tahlil keng qamrovni almashtirmaydi, to'ldiradi.

Precision bo'yicha ham CodeQL mukammal emas: 0.88 (M-5). Uning kuchi
aniqlikda emas, balki **boshqalar umuman ko'rmaydigan** zaiflikni
(Z-18) topishida.

**3. Bandit ning sirlarni aniqlash qoidasi tilga bog'liq.**
Inglizcha `SECRET_KEY` (Z-01) `B105` bilan topildi, o'zbekcha `DB_PAROL`
(Z-11) va `API_KALIT` (Z-12) topilmadi. Semgrep ning rasmiy qoidalari va
CodeQL ham ikkisini topmadi — uchala xalqaro vosita o'zbekcha nomlangan
sirlarni ko'rmadi. Maxsus qoida (`ozbekcha-qattiq-kodlangan-sir`)
ikkalasini ham aniqladi. Bu 3.4-bandning asosiy argumenti va ishning eng
original natijasi.

**4. Semgrep ning yagona FP si — tasdiqlangan yolg'on ijobiy natija.**
`app.py:124` da `open-redirect` qoidasi ishga tushdi va topilmani CWE-601
deb belgiladi. Topilma etalonda yo'q edi, shuning uchun avval etalonning
kamchiligi deb taxmin qilindi (M-4) va Z-25 sifatida qo'shib ko'rildi.
Tekshiruv taxminni rad etdi: `redirect("/profil?ism=" + login)` manzili
har doim `/profil?ism=` bilan boshlanadi, ya'ni sayt ichidagi nisbiy yo'l.
Hujumchi faqat so'rov satrining qiymatini boshqaradi, boshqa saytga
yo'naltira olmaydi — CWE-601 ta'rifi bajarilmaydi.

CodeQL bu yerda jim qoldi, garchi `py/url-redirection` (CWE-601) so'rovi
ishga tushgan va SARIF da e'lon qilingan bo'lsa ham: uning modeli hujumchi
host ni o'zgartira olishini talab qiladi. Bitta misolda shablon asosidagi
va semantik tahlil o'rtasidagi farq ko'rinadi — to'liq tahlili
`ZAIFLIKLAR.md` ning 4-bo'limida, 3.3-bandga tayyor.

**5. Yolg'on ijobiy natijalarning tabiati.**
Bandit ning 3 ta FP si — `import pickle` (app.py:17) va `import subprocess`
(app.py:19, utils.py:8) uchun B403/B404 ogohlantirishlari; import o'zi
zaiflik emas. Semgrep ning yagona FP si — yuqoridagi open redirect.
CodeQL ning ikkitasi — JSON javobidagi "aks etgan XSS" (4.2-band).

Uchala holat ham bir xil sinfdan: qoida ma'lumot oqimini to'g'ri
kuzatadi, lekin cho'kmaning kontekstini baholamaydi. Bandit ning FP lari
esa boshqa sinfdan — oqim umuman tahlil qilinmaydi, import ko'ringani
uchun ogohlantirish beriladi. 3.3-bandda ikkala sinfni ajratib
ko'rsatish kerak.

**6. Takroriy xabarlar soni vositaga qarab keskin farqlanadi.**
Semgrep (rasmiy): 26 xabardan 10 tasi takroriy — Z-04 uchun uchta qoida
(`dangerous-subprocess-use`, `subprocess-injection`, `subprocess-shell-true`)
bir vaqtda ishlaydi. CodeQL: 17 dan 1 tasi. Bandit: 0 ta. Deduplikatsiyasiz
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

**9. "100 barobar qimmat" da'vosi ishda dalil sifatida ishlatilmaydi.**
1.4-bandni yozishda tekshirildi. Manba — Boehm va Basili (IEEE Computer,
2001, 34(1), 135–137): ular mahsulot topshirilgandan keyingi tuzatish
"ko'pincha" taxminan 100 barobar qimmatroq deydi, lekin o'sha maqolada
kichik, kritik bo'lmagan tizimlar uchun nisbat 5:1 ga yaqin ekani ham
aytilgan. Menzies va boshqalar (Empirical Software Engineering, 2017,
22(4), 1903–1935) 171 ta loyihada bu effektga dalil topmagan; Bossavit
dalil bazasini metodologik jihatdan tanqid qilgan.

Qaror: raqam keltiriladi, lekin faqat bahsli da'vo sifatida, ikkala
tomonga havola bilan. Statik tahlilning foydasi boshqa, tekshiriladigan
asoslarga tayantiriladi (takrorlash narxi, qamrovning bir xilligi, mehnat
taqsimoti). **00-kirish va 04-xulosa yozilayotganda shu qaror
saqlanishi shart** — "kech topilgan zaiflik 100 barobar qimmat" degan
jumla ishning hech bir joyida dalil sifatida ishlatilmasligi kerak.

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

**M-4 (hal qilindi).** Open redirect topilmasi Z-25 sifatida etalonga
qo'shib ko'rildi, so'ng qaytarildi: tekshiruvda u ochiq qayta yo'naltirish
emasligi aniqlandi (4-kuzatuv). Etalon 24 ta bo'lib qoldi. Topilma
`ZAIFLIKLAR.md` ning 4-bo'limida tasdiqlangan yolg'on ijobiy natija
sifatida sabablari bilan hujjatlashtirildi.

Qo'shilgan holatdagi metrikalar (qaytarilgan, faqat taqqoslash uchun):
Semgrep (rasmiy) Precision 1.00 ga ko'tarilardi, CodeQL esa to'g'ri
ishlagani uchun FN olib, Recall 0.58 dan 0.56 ga tushardi. Ya'ni xato
etalon yozuvi noto'g'ri vositani mukofotlab, to'g'risini jazolagan
bo'lardi.

**M-5 (hal qilindi).** `py/reflective-xss` ning `app.py:91` va
`app.py:101` dagi topilmalari tekshirildi. Ular na takroriy xabar, na
haqiqiy zaiflik — **yolg'on ijobiy natija**: Flask ko'rinishidan
qaytarilgan lug'at `application/json` javobiga aylanadi va brauzer uni
HTML sifatida talqin qilmaydi. Taint oqimining o'zi to'g'ri kuzatilgan,
xato faqat cho'kma kontekstini baholamaslikda.

Amalga oshirish: `hisobot.py` ga `TASDIQLANGAN_FP` ro'yxati qo'shildi —
qo'lda tekshiruvdan o'tgan topilmalar sababi bilan qayd etiladi va
to'g'ridan-to'g'ri FP deb hisoblanadi. Ro'yxatdagi yozuv mos topilma
topmasa (masalan qator raqami surilsa), skript ogohlantirish beradi.
Natija: CodeQL Precision 1.00 dan 0.88 ga, F1 0.74 dan 0.70 ga tushdi.

**M-6 (hal qilindi).** Loyiha ochiq ombor sifatida GitHub ga yuklandi
(`nyxeldev/kurs-ishi-sast`), workflow uch marta ishga tushdi, ikki nuqson
tuzatildi, Security tab natijalari olindi.

**M-7 (hal qilindi).** CodeQL Action v3 dan v4 ga o'tkazildi: `init`,
`analyze` va uchala `upload-sarif` chaqiruvi. v4 ning yagona farqi —
Node.js v24 da ishlashi (`codeql-action#3169`); kirish parametrlari va
xulqi o'zgarmagan, ikkala shox parallel saqlanmoqda (v3.39.1 va v4.39.1
bir kunda chiqqan). Sinovdan o'tkazildi: CodeQL va Semgrep ishlari
muvaffaqiyatli, Security tab natijalari aynan o'sha — 70 ogohlantirish,
bir xil taqsimot. v3 eskirishi haqidagi ogohlantirish yo'qoldi.

**M-8 (hal qilindi).** Vaqt farqining sababi aniqlandi: birinchi ishga
tushirishda Semgrep qoidalar bazasini yuklab oladi, CodeQL esa so'rovlarni
kompilyatsiya qiladi. Kesh isigach CodeQL 2773 dan 57 soniyaga tushdi.
Vaqt jadvali endi uch ustunli (birinchi / takroriy / CI) va "chuqur tahlil
sekin" degan xulosa olib tashlandi — bu korpusda u tasdiqlanmaydi.

**M-17. 45 bet maqsadi II bobning hajmi bilan erishilmaydi.**
Muallif II bobni "hujjat 45 betga sig'adigan" hajmda yozishni so'radi.
Arifmetika shuni ko'rsatadi: II bob **bo'sh** bo'lganda ham hujjat
57-58 bet edi, ya'ni maqsad II bobning hajmidan mustaqil.

II bob 1477 so'z (6 bet) qilib yozildi — rejadagi 13 bet emas, lekin
o'z vazifasi uchun yetarli. Hozirgi holat:

| Bo'lim | Haqiqatda | Rejada | 45 bet uchun |
|---|---|---|---|
| Titul + mundarija | 3 | — | 3 |
| KIRISH | 5 | 3 | 4 |
| I BOB | 16 | 11 | 11 |
| II BOB | 6 | 13 | 6 |
| III BOB | 25 | 14 | 15 |
| XULOSA | 4 | 2 | 3 |
| ADABIYOTLAR | 5 | 2 | 3 |
| **JAMI** | **64** | **38-42** | **45** |

Ya'ni 45 betga tushish uchun **19 bet (~3 900 so'z) qisqartirish** kerak,
va uning asosiy qismi — **III bobdan 10 bet**.

Tavsiya etiladigan tartib (eng arzondan boshlab):
1. Adabiyotlardagi ishchi izohlar va 33-o'rin olib tashlansa: ~1 bet;
2. III bobdagi katta jadvallarni ilovalarga ko'chirish — 3.2 (etalon,
   24 qator), 3.8 (qiyosiy, 24 qator), 3.10 (FN sabablari, 13 qator),
   3.5 (CodeQL so'rovlari, 11 qator) va to'rtta kod bloki: ~4-5 bet.
   Matnda havola qoladi, tahlil buzilmaydi;
3. III bob matnini ~1 000 so'zga qisqartirish: ~5 bet;
4. I bob matnini ~1 000 so'zga qisqartirish: ~5 bet;
5. Kirish va xulosadan 1 bet.

2-band tahlilga tegmaydi, shuning uchun eng xavfsiz. 3- va 4-bandlar
yozilgan matnni qisqartirishni talab qiladi — bu muallif qarori.

**M-16. Formatlash namuna hujjatga moslashtirildi.**
Muallif namuna sifatida boshqa kurs ishini berdi
(`Nizamov_Sardorbek_Kurs_ishi`, 39 bet, 7 156 so'z). U Word orqali
o'qilib, formatlash unga moslashtirildi:

| Jihat | Namuna | Oldin | Endi |
|---|---|---|---|
| Bob sarlavhasi | 14 pt markaz | 16 pt | 14 pt |
| Jadval/rasm nomi | markaz, 12 pt, kursiv | chap, 14 pt qalin | markaz, 12 pt, kursiv |
| Bet raqami | pastda markazda | pastda o'ngda | pastda markazda |
| Kod shrifti | Consolas | Courier New | Consolas |
| Jadval ichi | 11 pt | 10-12 pt | 11 pt (7 ustunda 10) |
| 3-daraja sarlavha | oddiy qalin paragraf | sarlavha uslubi | oddiy paragraf |
| Titul beti | muassasa/fakultet/kafedra/yo'nalish/talaba/fan, "KURS ISHI" 20 pt, "Reyting bali" | bo'sh chiziqlar | namuna tartibida |

Chekkalar, asosiy shrift (TNR 14 pt), qator oralig'i (1,5), ikki chetga
tekislash va 12,5 mm abzats ikkala hujjatda allaqachon bir xil edi.

**Ataylab namunadan chetlashilgan ikki joy:**
1. **Mundarija avtomatik qoldirildi.** Namunada u qo'lda yozilgan va
   nuqsonli (sahifa raqami matnga yopishgan: "KIRISH03", "XULOSA035").
   Bizda Word maydoni, o'zi yangilanadi. Namunada mundarijada faqat
   boblar bor, bizda bandlar ham (1.1, 1.2, ...).
2. **Bob sarlavhalari yangi betdan uslub orqali** (namunada qo'lda bet
   uzilishi bilan) — ko'rinishi bir xil, lekin matn o'zgarganda buzilmaydi.

**Titul betida to'ldirilmagan joylar** (ma'lumot menda yo'q, o'ylab
topilmadi): ta'lim muassasasi, fakultet, kafedra, yo'nalish, kurs, fan
nomi, shahar, familiya.

**M-14. Hujjat hajmi chegaradan oshdi: 58 bet (chegara 35-45).**
`ilovalar/kurs-ishi.docx` Word da o'lchandi. Bet taqsimoti (mundarijadagi
raqamlar bo'yicha):

| Bo'lim | Haqiqatda | Rejada |
|---|---|---|
| Titul + mundarija | 3 | — |
| KIRISH | 5 | 3 |
| I BOB | 16 | 11 |
| II BOB (yozilmagan) | 1 | 13 |
| III BOB | 25 | 14 |
| XULOSA | 4 | 2 |
| ADABIYOTLAR | 4 | 2 |
| **JAMI** | **58** | **38-42** |

**Sababi — bet zichligini noto'g'ri baholaganim.** Boblarni yozganda
333 so'z/bet deb hisoblagan edim; Times New Roman 14 pt, 1,5 oraliq va
30/15/20/20 chekkalarda haqiqiy zichlik **~205 so'z/bet** (11 256 so'z /
55 bet matn). Ya'ni 35-45 bet chegarasi taxminan **7 200-9 200 so'zga**
to'g'ri keladi, hozirgi matn esa 11 256 so'z — va II bob hali yo'q.

**Eng muhim xulosa:** II bob rejadagi 13 betga yozilsa, jami ~70 bet
bo'ladi. Shuning uchun II bobni yozishdan OLDIN qaror kerak: yoki
chegarani oshirish kelishiladi, yoki I/III bob qisqartiriladi, yoki
II bob rejadagidan ancha qisqa yoziladi.

Qisqartirish uchun eng arzon variantlar (tahlil matniga tegmasdan):
- 3.2-jadval (etalon to'plam, 24 qator) va 3.8-jadval (qiyosiy jadval,
  24 qator) — A/B ilovasiga, matnda havola qoldirilib: ~3-4 bet;
- 3.5-jadval (CodeQL so'rovlari) va kod bloklari — B ilovasiga: ~1 bet;
- adabiyotlardagi ishchi izohlar va "To'ldirilishi kerak" bo'limi
  olib tashlansa: ~1 bet.

**M-15. Hujjatda ishchi izohlar qolgan.** Yig'ish ataylab "sodiq"
bajarildi — hech narsa jimgina tashlab ketilmadi. Natijada hujjatga
quyidagilar ham tushdi va topshirishdan oldin olib tashlanishi kerak:
- `02-bob.md` dagi "> **Holat:** yozilmagan. Hajm: 13 bet." izohi;
- `adabiyotlar.md` dagi "> **Holat:**" va "> **Qoida:**" izohlari,
  "To'ldirilishi kerak (II va III boblar uchun)" bo'limi (27-31 o'rinlar)
  va oxirgi "Eslatma" bo'limi — ikkisi mundarijaga ham chiqdi;
- titul betidagi to'ldirilmagan joylar: ta'lim muassasasi, fakultet,
  guruh, ilmiy rahbar, shahar. Bu ma'lumotlar menda yo'q, shuning uchun
  ataylab bo'sh chiziq qoldirildi.

**M-13. Kirish va xulosa II bobga tayanadi, lekin II bob hali yozilmagan.**
00-kirish va 04-xulosa yozilganda `matn/02-bob.md` bo'sh skelet edi (42
so'z). Shu sababli:

- kirishdagi **3-** va **4-vazifa** hamda "Ishning tuzilishi" bo'limidagi
  II bob tavsifi `reja.md` ga (tasdiqlangan rejaga) tayanadi, yozilgan
  matnga emas;
- xulosadagi 3- va 4-vazifa natijalari ataylab faqat I va III bobda
  haqiqatan asoslangan da'volar bilan cheklangan (tahlil chuqurligi
  ierarxiyasi va to'rtta vositaning tanlanishi) — II bobdan hech qanday
  raqam yoki xulosa keltirilmagan.

**02-bob yozilgandan keyin tekshirilishi SHART:** kirishdagi 3- va
4-vazifa matni, "Ishning tuzilishi" dagi II bob paragrafi va xulosadagi
3-/4-vazifa natijalari yozilgan matnga mos kelishi. Agar II bob
rejadagidan farq qilsa, uchala joy ham yangilanadi.

**M-11. `ZAIFLIKLAR.md` ning 3-bo'limi eskirgan.** 03-bobni yozishda
aniqlandi. U yerda "Natijada Z-18 ni sinovdagi hech bir vosita topmadi"
deyilgan, lekin bu CodeQL ishga tushirilishidan oldin yozilgan.
`qiyosiy-jadval.md` va yuqoridagi 1-kuzatuvga ko'ra **CodeQL Z-18 ni
topgan** (`py/path-injection`, utils.py:22). 3-bob to'g'ri ma'lumotga
tayanadi; `ZAIFLIKLAR.md` ning 3-bo'limi yangilanishi kerak.

**M-12. `ZAIFLIKLAR.md` ning 4.1-bandida qator raqami chalkash.** U yerda
Semgrep ning `open-redirect` topilmasi `app.py:124` deb ko'rsatilib,
darhol `redirect("/profil?ism=" + login)` kodi keltiriladi. Aslida
`app.py:124` — taint **manbasi**
(`login = request.form.get("login", "")`), `redirect()` chaqiruvi esa
`app.py:129` da. Semgrep taint rejimidagi topilmani manba qatorida e'lon
qiladi (shu sababli `hisobot.py` da TOLERANS kerak). Vosita chiqishi
to'g'ri, faqat hujjatdagi izoh chalkash — 3.3-bandda to'g'ri yozilgan.

**M-9. Ombor ochiq.** Ataylab zaif kod `nyxeldev/kurs-ishi-sast` da
hammaga ko'rinadi — bu kod skanerlashni bepul ishlatish uchun zarur edi
(yopiq omborda GitHub Advanced Security talab qilinadi). Ish topshirilgach
omborni yopiq qilish mumkin, lekin shunda Security tab natijalari
ko'rinmay qoladi — skrinshotlar oldin olinishi kerak.

**M-10. Boshqa amallar Node.js 20 ni mo'ljallaydi.** v4 ga o'tgandan keyin
yangi ogohlantirish chiqdi: `actions/checkout@v4` va
`actions/setup-python@v5` Node.js 20 ni mo'ljallaydi va majburan Node.js
24 da ishga tushirilmoqda (GitHub 2025-09-19 dagi e'lon). Hozircha
ishlaydi. Mavjud versiyalar: `checkout` v7.0.1, `setup-python` v7.1.0,
`upload-artifact` v7.0.2 — ya'ni uch-to'rt katta versiya orqada.
Bu CodeQL ga aloqasi yo'q alohida masala va katta versiya sakrashi
bo'lgani uchun ko'r-ko'rona yangilab bo'lmaydi: har birining
o'zgarishlarini tekshirish kerak.

> SAST qismi to'liq: to'rtta vosita, o'lchangan metrikalar, to'liq
> moslashtirish jurnali va ishlaydigan CI/CD quvuri (CodeQL Action v4).
> Qolgani — skrinshotlar va matn.
