# III BOB. AMALIY QISM: VOSITALARNI QIYOSIY SINASH

## 3.1. Sinov obyekti va metodika

### Sinov ilovasining tavsifi

Vositalarni qiyoslash uchun ataylab zaif qilingan Flask ilovasi ishlab
chiqildi. Tayyor etalon to'plamlardan (OWASP Benchmark, Juliet Test Suite)
foydalanish o'rniga o'z obyektini yaratish qarori ikki sababga asoslanadi:
birinchidan, ishning asosiy savollaridan biri — xalqaro vositalarning
o'zbek tilida nomlangan identifikatorlar bilan ishlashi, bunday namunalar
esa tayyor to'plamlarda umuman yo'q; ikkinchidan, kichik va to'liq nazorat
qilinadigan obyekt har bir topilmani qo'lda tekshirish imkonini beradi.

Ilova uchta moduldan iborat (3.1-jadval).

**3.1-jadval. Sinov ilovasining modullari**

| Modul | Qator soni | Mazmuni |
|---|---|---|
| `app.py` | 148 | Flask marshrutlari: qidiruv, shablon, buyruq bajarish, deserializatsiya, fayl o'qish, kirish |
| `auth.py` | 65 | Autentifikatsiya: parol xeshlash, SQL so'rov, sessiya tokeni, huquq tekshiruvi |
| `utils.py` | 80 | Yordamchi funksiyalar: fayl o'qish, tashqi so'rov, vaqtinchalik fayl, jurnalga yozish, huquqlar |
| **Jami** | **293** | |

Manba: `kod/zaif-ilova/`.

Modullarga bo'lish tasodifiy emas. Bir qator zaifliklarda ma'lumot manbasi
(source) va cho'kmasi (sink) ataylab turli fayllarga joylashtirilgan:
`app.py` dagi marshrut `request.args.get` orqali foydalanuvchi kiritmasini
oladi va uni `utils.py` yoki `auth.py` dagi funksiyaga uzatadi. Bu
modullararo zaharlangan ma'lumot oqimini kuzata oladigan va kuzata
olmaydigan vositalarni ajratish imkonini beradi (3.3-band).

Bandit hisobotiga ko'ra, tahlil qilingan kodning sof hajmi — 184 qator
(izohlar va bo'sh qatorlarsiz), `#nosec` izohi bilan chetlab o'tilgan
qatorlar yo'q. Manba: `kod/natijalar/01-bandit.txt`.

### Kiritilgan zaifliklar va etalon to'plam

Ilovaga 24 ta zaiflik kiritilgan; ularning har biri uchun fayl, qator, CWE
kodi va jiddiylik darajasi oldindan qayd etilgan. Shu ro'yxat etalon
to'plam (ground truth) vazifasini bajaradi va metrikalarni hisoblashning
yagona asosi hisoblanadi (3.2-jadval).

**3.2-jadval. Etalon to'plam: sinov ilovasiga kiritilgan zaifliklar**

| Kod | Fayl:qator | CWE | Zaiflik | Jiddiylik |
|---|---|---|---|---|
| Z-01 | app.py:30 | CWE-798 | Qattiq kodlangan maxfiy kalit (`SECRET_KEY`) | O'rta |
| Z-02 | app.py:48 | CWE-89 | SQL inyeksiyasi (`%`-formatlash) | Yuqori |
| Z-03 | app.py:64 | CWE-79 | XSS / SSTI (`render_template_string`) | Yuqori |
| Z-04 | app.py:73 | CWE-78 | Buyruq inyeksiyasi (`subprocess`, `shell=True`) | Kritik |
| Z-05 | app.py:90 | CWE-502 | Xavfsiz bo'lmagan `yaml.load` | Yuqori |
| Z-06 | app.py:100 | CWE-502 | `pickle.loads` ishonchsiz manbadan | Kritik |
| Z-07 | app.py:110 | CWE-94 | Kod inyeksiyasi (`eval`) | Kritik |
| Z-08 | app.py:141 | CWE-78 | Buyruq inyeksiyasi (`os.system`) | Kritik |
| Z-09 | app.py:148 | CWE-489 | `debug=True` ishlab chiqarish rejimida | Yuqori |
| Z-10 | app.py:148 | CWE-605 | Barcha interfeyslarga bog'lanish (`0.0.0.0`) | O'rta |
| Z-11 | auth.py:12 | CWE-798 | Qattiq kodlangan MB paroli (`DB_PAROL`) | Yuqori |
| Z-12 | auth.py:16 | CWE-798 | Qattiq kodlangan API kaliti (`API_KALIT`) | Yuqori |
| Z-13 | auth.py:25 | CWE-327 | Parol uchun MD5, tuzsiz | Yuqori |
| Z-14 | auth.py:34 | CWE-89 | SQL inyeksiyasi (f-satr) | Yuqori |
| Z-15 | auth.py:50 | CWE-330 | Token uchun `random` moduli | O'rta |
| Z-16 | auth.py:57 | CWE-327 | SHA-1 xesh funksiyasi | O'rta |
| Z-17 | auth.py:64 | CWE-617 | Huquq tekshiruvi uchun `assert` | O'rta |
| Z-18 | utils.py:21 | CWE-22 | Yo'l bo'ylab harakatlanish | Yuqori |
| Z-19 | utils.py:30 | CWE-78 | Buyruq inyeksiyasi (`subprocess.run`) | Kritik |
| Z-20 | utils.py:37 | CWE-295 | TLS tekshiruvi o'chirilgan (`verify=False`) | Yuqori |
| Z-21 | utils.py:45 | CWE-377 | Xavfsiz bo'lmagan vaqtinchalik fayl | Past |
| Z-22 | utils.py:54 | CWE-532 | Parol jurnalga yozilmoqda | O'rta |
| Z-23 | utils.py:60 | CWE-732 | Juda keng fayl huquqlari (`0o777`) | O'rta |
| Z-24 | utils.py:65 | CWE-390 | E'tiborsiz qoldirilgan istisno | Past |

Manba: `kod/zaif-ilova/ZAIFLIKLAR.md`.

Jami 24 ta zaiflik 15 xil CWE toifasiga tegishli. Eng ko'p uchraydigan
toifalar: CWE-78 (buyruq inyeksiyasi) va CWE-798 (qattiq kodlangan
ma'lumot) — har biridan 3 tadan; CWE-89, CWE-502 va CWE-327 — har biridan
2 tadan; qolgan 12 ta CWE bittadan vakil bilan ifodalangan.

Bog'liqliklardagi zaifliklar etalon to'plamga kiritilmagan. `requirements.txt`
da ataylab eskirgan oltita paket qoldirilgan (Flask 0.12.2, Jinja2 2.10,
Werkzeug 0.14.1, PyYAML 5.1, requests 2.19.1, urllib3 1.24.1); ular statik
tahlil vositalari tomonidan topilmasligi kerak va faqat SCA vositasi uchun
sinov materiali bo'lib xizmat qiladi.

### Sinov muhiti

Barcha o'lchovlar bitta mashinada, bir kunda olingan (3.3-jadval).

**3.3-jadval. Sinov muhiti**

| Komponent | Versiya |
|---|---|
| Operatsion tizim | Windows 11 Pro 10.0.26200 |
| Qobiq | Git Bash (MINGW64_NT-10.0-26200) |
| Python | 3.14.3 |
| Bandit | 1.9.4 |
| Semgrep | 1.182.1 |
| pip-audit | 2.10.1 |
| CodeQL | 2.27.3 |

Manba: `kod/natijalar/00-muhit.txt` (2026-10-26, 01:32).

Vositalarning versiyalari xotiradan emas, `--version` chiqishidan olingan
va avtomatik ravishda fayl ga yozilgan. CI muhitida Python ning boshqa
versiyasi — 3.12 — ishlatiladi (`.github/workflows/sast.yml`); bu farq
natijalarga ta'sir qilmadi, chunki CI dagi topilmalar soni lokal natijalar
bilan to'liq mos keldi (3.5-band).

### Baholash mezonlari va moslashtirish metodikasi

Har bir vosita uchun quyidagi ko'rsatkichlar hisoblanadi: to'g'ri aniqlangan
zaifliklar (TP), yolg'on ijobiy natijalar (FP), o'tkazib yuborilgan
zaifliklar (FN = 24 − TP), hamda ulardan kelib chiqadigan Precision, Recall
va F1 ko'rsatkichlari (formulalar 2.4-bandda keltirilgan). Alohida ustun
sifatida takroriy xabarlar sanaladi.

Hisoblash qo'lda emas, `kod/tahlil/hisobot.py` skripti orqali bajariladi.
Skript topilmani etalon zaiflikka ikki shartdan biri bajarilganda
bog'laydi: qator farqi uchtadan oshmasa yoki topilma bilan etalon zaiflik
ayni bir funksiya tanasida joylashgan bo'lsa. Modul darajasidagi
topilmalarga faqat birinchi shart qo'llanadi.

Metodikaning uch jihati natijalarni to'g'ri talqin qilish uchun muhim.
Birinchidan, **takroriy xabarlar yolg'on ijobiy deb sanalmaydi**: bitta
zaiflikni bir necha qoida belgilasa, birinchisi TP, qolganlari alohida
ustunda hisoblanadi — aks holda ko'p qoidali to'plamlar sun'iy jazolangan
bo'lardi. Ikkinchidan, **bir qatorda bir nechta zaiflik bo'lishi mumkin**
(`app.py:148` da Z-09 va Z-10), shuning uchun topilmalar avval CWE kodi,
so'ngra band bo'lmagan yozuvlar bo'yicha taqsimlanadi. Uchinchidan,
**qo'lda tekshirilgan yolg'on ijobiy natijalar alohida ro'yxatda**:
skriptdagi `TASDIQLANGAN_FP` yozuvlari sababi bilan qayd etiladi va
to'g'ridan-to'g'ri FP deb hisoblanadi.

Har bir xabarning qaysi etalon yozuviga bog'langani
`kod/natijalar/moslashtirish.md` faylida to'liq keltirilgan; bu metrikalarni
mustaqil qayta tekshirish imkonini beradi va B ilovasiga kiritiladi.

**Xulosa.** Sinov obyekti — 293 qatorli, uch modulli Flask ilovasi; unga
15 xil CWE toifasiga tegishli 24 ta zaiflik kiritilib, aniq manzili
oldindan qayd etildi. Metrikalar skript orqali hisoblanadi va har bir
bog'lanish hujjatlashtiriladi, shuning uchun natijalar takrorlanuvchi.
Obyektning kichikligi statistik umumlashtirishga imkon bermaydi, lekin
har bir o'tkazib yuborishning sababini aniqlash imkonini beradi — ishning
maqsadi aynan shu.

---

## 3.2. Vositalarni ishga tushirish va natijalar

Barcha vositalar `kod/tahlil/tahlil.sh` skripti orqali, beshta bosqichda
ketma-ket ishga tushiriladi. Chiqish fayllari `kod/natijalar/` ga
yoziladi: inson o'qishi uchun matnli, dastur qayta ishlashi uchun JSON yoki
SARIF ko'rinishida.

### Bandit

Bandit Python uchun ixtisoslashgan, abstrakt sintaksis daraxti asosida
ishlaydigan vosita. U 22 ta topilma berdi. Topilmalarning jiddiylik va
ishonch bo'yicha taqsimoti 3.4-jadvalda keltirilgan.

**3.4-jadval. Bandit topilmalarining taqsimoti**

| Daraja | Jiddiylik bo'yicha | Ishonch bo'yicha |
|---|---|---|
| Yuqori | 8 | 17 |
| O'rta | 7 | 4 |
| Past | 7 | 1 |
| **Jami** | **22** | **22** |

Manba: `kod/natijalar/01-bandit.txt`, `01-bandit.json` (`metrics._totals`).

Taqsimot muhim xossani ko'rsatadi: 22 ta xabardan 17 tasi yuqori ishonch
bilan berilgan, ya'ni ishonch darajasi jiddiylikdan sezilarli yuqori. Buning
sababi — Bandit qoidalarining sodda va aniq shablonlarga tayanishi:
`hashlib.md5()` chaqiruvini topish uchun oqim tahlili kerak emas. Past
jiddiylikdagi yettita xabarning uchtasi esa umuman zaiflik emas (3.3-band).

Bandit chiqishining tipik ko'rinishi:

```
>> Issue: [B105:hardcoded_password_string] Possible hardcoded password:
   's3cr3t-kalit-2024-oz'
   Severity: Low   Confidence: Medium
   CWE: CWE-259 (https://cwe.mitre.org/data/definitions/259.html)
   Location: .../app.py:30:11
```

E'tiborga loyiq nuqta: Bandit bu topilmani CWE-259 (qattiq kodlangan
parol) deb belgiladi, etalonda esa u CWE-798 (qattiq kodlangan ma'lumot)
sifatida qayd etilgan. Bunday nomuvofiqliklar muntazam uchraydi va
normallashtirish zaruratini tug'diradi (3.3-band).

### Semgrep — rasmiy qoidalar

Semgrep ikkita rasmiy qoidalar to'plami bilan ishga tushirildi: `p/python`
va `p/security-audit`. Natija — 26 ta topilma, xatolarsiz; ular 24 ta
noyob qoidaga tegishli. Jiddiylik bo'yicha: `ERROR` — 14 ta, `WARNING` —
12 ta. Manba: `kod/natijalar/02-semgrep.json`.

Qoidalar to'plamlarining bir-birini qoplashi hatto qoidalarning o'z
nomlarida ham ko'rinadi: 24 ta to'liq identifikator orasida ikkitasi bir
xil qisqa nomga ega — `python.django.security.injection.raw-html-format.`
`raw-html-format` va `python.flask.security.injection.raw-html-concat.`
`raw-html-format`. Ikkalasi ham `app.py:63` da, ya'ni ayni bir zaiflikda
(Z-03) ishga tushdi. Ya'ni qisqa nom bo'yicha 23 ta, to'liq identifikator
bo'yicha 24 ta qoida.

Semgrep ning eng ko'zga tashlanadigan xususiyati — takroriy xabarlar.
26 ta topilmadan 10 tasi ayni bir zaiflik haqidagi qo'shimcha xabarlardir.
Masalan, `app.py:73` dagi bitta buyruq inyeksiyasini (Z-04) uchta qoida bir
vaqtda belgilaydi: `dangerous-subprocess-use`, `subprocess-injection` va
`subprocess-shell-true`. Xuddi shunday, `app.py:110` dagi `eval`
chaqiruvini (Z-07) `user-eval`, `eval-detected` va `eval-injection`
qoidalari uch marta xabar qiladi. Bu qoidalar to'plamlarining bir-birini
qoplashi natijasidir va deduplikatsiyasiz Precision ko'rsatkichini sun'iy
ravishda pasaytiradi.

Topilmalar jurnalini tahlil qilishda yana bir xususiyat aniqlandi:
Semgrep taint rejimidagi qoidalarning topilmasini **manba** qatorida,
shablon asosidagi qoidalarning topilmasini esa **cho'kma** qatorida
e'lon qiladi. Masalan, `app.py:43` da `sql-injection-db-cursor-execute`
(manba — `request.args.get`) va `app.py:48` da `tainted-sql-string`
(cho'kma — so'rovni yig'ish) bitta zaiflik, Z-02, haqida xabar beradi;
`app.py:107` / `app.py:110` va `app.py:138` / `app.py:141` juftliklarida
ham xuddi shunday. Bu kuzatuv 3.1-banddagi moslashtirish tolerantligini
(uch qator) tushuntiradi: tolerantliksiz bir zaiflikning manba va cho'kma
xabarlari ikki turli topilma deb hisoblanar edi. Manba:
`kod/natijalar/moslashtirish.md`.

### CodeQL

CodeQL avval kodni ma'lumotlar bazasiga aylantiradi, so'ngra unga so'rovlar
beradi. Tahlil `python-security-extended` to'plami bilan bajarildi.

SARIF chiqishida 50 ta so'rov e'lon qilingan, ya'ni to'plam shu so'rovlarni
kod ustida ishga tushirgan. Ulardan atigi 11 tasi natija qaytardi
(3.5-jadval), jami 17 ta topilma bilan.

**3.5-jadval. CodeQL: natija qaytargan so'rovlar**

| So'rov | CWE teglari |
|---|---|
| `py/path-injection` | CWE-22, 23, 36, 73, 99 |
| `py/template-injection` | CWE-74 |
| `py/command-line-injection` | CWE-78, 88 |
| `py/reflective-xss` | CWE-79, 116 |
| `py/sql-injection` | CWE-89 |
| `py/code-injection` | CWE-94, 95, 116 |
| `py/flask-debug` | CWE-215, 489 |
| `py/insecure-temporary-file` | CWE-377 |
| `py/unsafe-deserialization` | CWE-502 |
| `py/request-without-cert-validation` | CWE-295 |
| `py/overly-permissive-file` | CWE-732 |

Manba: `kod/natijalar/05-codeql.sarif` (`runs[0].tool.driver.rules` va
`runs[0].results`).

"E'lon qilingan 50, natija bergan 11" nisbati 3.3-banddagi tahlil uchun
hal qiluvchi: u o'tkazib yuborishning sababi so'rovning umuman yo'qligimi
yoki so'rov ishlagani holda modeli mos kelmaganimi — degan savolga javob
beradi. Jadvaldagi CWE teglari yana bir muammoni ko'rsatadi: bitta
so'rovga beshtagacha kod biriktirilgan, shuning uchun moslashtirish bitta
kod bilan emas, kodlar to'plami bilan amalga oshiriladi.

### pip-audit

pip-audit `requirements.txt` dagi oltita paketni ma'lum zaifliklar
bazalari bilan solishtirdi. Konsol chiqishi "Found 82 known vulnerabilities
in 6 packages" deb xabar beradi, lekin bu raqam to'g'ridan-to'g'ri
keltirilishi mumkin emas: bir xil PYSEC identifikatori ikki manbadan
(PyPI advisory ma'lumotlar bazasi va OSV) ikki marta qaytariladi.
Noyob identifikatorlar bo'yicha hisoblaganda natija boshqacha (3.6-jadval).

**3.6-jadval. pip-audit: paketlar bo'yicha noyob zaifliklar**

| Paket | Versiya | Noyob zaiflik |
|---|---|---|
| urllib3 | 1.24.1 | 13 |
| werkzeug | 0.14.1 | 12 |
| jinja2 | 2.10 | 6 |
| requests | 2.19.1 | 5 |
| flask | 0.12.2 | 4 |
| pyyaml | 5.1 | 3 |
| **Jami** | **6 paket** | **43** |

Manba: `kod/natijalar/04-pip-audit.txt` (noyob PYSEC identifikatorlari
bo'yicha hisoblangan).

Ishda 43 raqami keltiriladi. Bu holatning o'zi SCA natijalari bilan
ishlashda deduplikatsiya zarurligini ko'rsatadi — vositaning o'z xabari
haqiqiy zaifliklar sonini deyarli ikki barobar oshirib ko'rsatgan.

Natijalarning mazmuni ham diqqatga sazovor: eng ko'p zaiflik ilova
bevosita chaqirmaydigan paketlarda — `urllib3` va `werkzeug` da — topildi.
Bular tranzitiv bog'liqliklar bo'lib, ishlab chiquvchi ularni odatda
umuman ko'rmaydi. Statik tahlil vositalari bu zaifliklarning birortasini
ham topmadi va topishi ham mumkin emas edi: zaif kod loyihaning o'zida
emas, o'rnatilgan kutubxonalarda joylashgan.

### Ishlash vaqti

Vositalarning takroriy ishga tushirishdagi vaqti 3.7-jadvalda keltirilgan.

**3.7-jadval. Vositalarning ishlash vaqti**

| Bosqich | Takroriy ishga tushirish | GitHub Actions |
|---|---|---|
| Bandit | 2 s | 20 s |
| Semgrep (rasmiy qoidalar) | 11 s | 45 s |
| Semgrep (maxsus qoidalar) | 7 s | (yuqoridagi ish ichida) |
| pip-audit | 5 s | 13 s |
| CodeQL (baza + `security-extended`) | 57 s | 39 s |

Manbalar: lokal ustun — `kod/natijalar/00-vaqt.txt`; CI ustuni — GitHub
Actions dagi ish (job) davomiyligi, unga `checkout` va muhitni tayyorlash
ham kiradi.

Birinchi ishga tushirish vaqtlari keskin boshqacha bo'lgan: Semgrep qoidalar
bazasini tarmoqdan yuklab oladi, CodeQL esa so'rovlarni kompilyatsiya
qiladi. Loyiha jurnalida qayd etilishicha, CodeQL ning to'liq tahlili kesh
isigach 2773 soniyadan 57 soniyaga tushgan (manba: `HOLAT.md`).

Shu sababli vaqt ko'rsatkichlaridan "chuqur tahlil sekin" degan xulosa
chiqarilmaydi: kesh isiganidan keyin bu hajmdagi korpusda to'rtala vosita
ham soniyalar ichida tugaydi. Tezlik bo'yicha asosli xulosa uchun ancha
katta kod bazasi kerak; bu ushbu ishning ochiq cheklovi.

**Xulosa.** To'rtta vosita bir xil kod ustida ishga tushirilib, mos ravishda
22, 26, 17 va 43 ta natija qaytardi. Xabarlar sonining o'zi vosita sifatini
ko'rsatmaydi: Semgrep eng ko'p xabar bergan bo'lsa-da, ularning 10 tasi
takroriy; pip-audit ning 82 ta xabari esa aslida 43 ta noyob zaiflikdir.
Shu sababli keyingi bandda barcha natijalar etalon to'plamga nisbatan
normallashtiriladi.

---

## 3.3. Natijalarni qiyosiy tahlil qilish

### Umumiy jadval

Barcha vositalarning natijalari etalon to'plamga nisbatan normallashtirilib,
yagona jadvalga keltirildi (3.8-jadval).

**3.8-jadval. Zaifliklarning vositalar bo'yicha aniqlanishi**

| Kod | Fayl:qator | CWE | Bandit | Semgrep (rasmiy) | Semgrep (maxsus) | CodeQL |
|---|---|---|---|---|---|---|
| Z-01 | app.py:30 | CWE-798 | + | + | − | − |
| Z-02 | app.py:48 | CWE-89 | + | + | − | + |
| Z-03 | app.py:64 | CWE-79 | − | + | + | + |
| Z-04 | app.py:73 | CWE-78 | + | + | − | + |
| Z-05 | app.py:90 | CWE-502 | + | + | − | + |
| Z-06 | app.py:100 | CWE-502 | + | + | − | + |
| Z-07 | app.py:110 | CWE-94 | + | + | − | + |
| Z-08 | app.py:141 | CWE-78 | + | + | − | + |
| Z-09 | app.py:148 | CWE-489 | + | + | − | + |
| Z-10 | app.py:148 | CWE-605 | + | + | − | − |
| Z-11 | auth.py:12 | CWE-798 | − | − | + | − |
| Z-12 | auth.py:16 | CWE-798 | − | − | + | − |
| Z-13 | auth.py:25 | CWE-327 | + | + | − | − |
| Z-14 | auth.py:34 | CWE-89 | + | − | − | + |
| Z-15 | auth.py:50 | CWE-330 | + | − | − | − |
| Z-16 | auth.py:57 | CWE-327 | + | + | − | − |
| Z-17 | auth.py:64 | CWE-617 | + | − | − | − |
| Z-18 | utils.py:21 | CWE-22 | − | − | − | + |
| Z-19 | utils.py:30 | CWE-78 | + | + | − | + |
| Z-20 | utils.py:37 | CWE-295 | + | + | − | + |
| Z-21 | utils.py:45 | CWE-377 | + | − | − | + |
| Z-22 | utils.py:54 | CWE-532 | − | − | + | − |
| Z-23 | utils.py:60 | CWE-732 | + | + | − | + |
| Z-24 | utils.py:65 | CWE-390 | + | − | + | − |
| **Jami** | | | **19** | **15** | **5** | **14** |

`+` — aniqlandi, `−` — o'tkazib yuborildi.
Manba: `kod/natijalar/qiyosiy-jadval.md`.

### Aniqlik metrikalari

3.8-jadval asosida hisoblangan ko'rsatkichlar 3.9-jadvalda keltirilgan.

**3.9-jadval. Vositalarning aniqlik metrikalari**

| Vosita | Topilma | TP | Takroriy | FP | FN | Precision | Recall | F1 |
|---|---|---|---|---|---|---|---|---|
| Bandit | 22 | 19 | 0 | 3 | 5 | 0,86 | **0,79** | **0,83** |
| Semgrep (rasmiy) | 26 | 15 | 10 | 1 | 9 | 0,94 | 0,62 | 0,75 |
| Semgrep (maxsus) | 5 | 5 | 0 | 0 | 19 | 1,00 | 0,21 | 0,34 |
| CodeQL | 17 | 14 | 1 | 2 | 10 | 0,88 | 0,58 | 0,70 |

Etalon to'plam: 24 ta zaiflik.
Manba: `kod/natijalar/metrikalar.md` (`hisobot.py` chiqishi).

Birinchi kuzatuv kutilganidan farq qiladi: F1 bo'yicha eng yaxshi natijani
to'rtlikdagi eng sodda vosita — Bandit ko'rsatdi (0,83). Sabab sinov
obyektining tarkibida: etalon to'plamdagi zaifliklarning ko'pchiligi aniq
shablon bilan ifodalanadi (`hashlib.md5`, `eval`, `verify=False`,
`os.chmod(0o777)`), bunday zaifliklarni esa AST darajasidagi qoida ham
ishonchli topadi. Bu natija Bandit ning CodeQL dan kuchliroq ekanini emas,
korpus tarkibining metrikaga qanchalik kuchli ta'sir qilishini ko'rsatadi —
har qanday qiyosiy baholashda hisobga olinishi shart bo'lgan cheklov.

Ikkinchidan, keng qamrovli qoidalar to'plamiga ega uch vositaning hech biri
mukammal aniqlikka erishmadi; 1,00 ko'rsatkichi faqat ataylab tor yozilgan
maxsus qoidalarda, buning evaziga ularning Recall i atigi 0,21. Uchinchidan,
hech bir vosita yolg'iz 19 tadan ko'pini topmadi — eng yaxshi holatda ham
etalon to'plamning beshdan bir qismi ko'rinmay qoldi.

### O'tkazib yuborilgan zaifliklar va ularning sabablari

Metrikalarning o'zi vosita nima uchun zaiflikni topmaganini tushuntirmaydi.
Har bir o'tkazib yuborish qo'lda tekshirildi; natijalar 3.10-jadvalda.

**3.10-jadval. O'tkazib yuborilgan zaifliklar va sabablari**

| Vosita | Zaiflik | Sababi |
|---|---|---|
| Bandit | Z-03 (CWE-79) | Shablon mexanizmi semantikasi modellanmagan: `render_template_string` hech bir qora ro'yxatda yo'q |
| Bandit | Z-11, Z-12 (CWE-798) | `B105` qoidasi faqat inglizcha nomlarni taniydi; `DB_PAROL`, `API_KALIT` shablonga tushmaydi |
| Bandit | Z-18 (CWE-22) | Ma'lumot oqimi tahlili yo'q; `os.path.join` o'zi xavfli chaqiruv emas |
| Bandit | Z-22 (CWE-532) | Argumentning maxfiyligini aniqlash qoidasi mavjud emas |
| Semgrep (rasmiy) | Z-11, Z-12 (CWE-798) | Rasmiy qoidalardagi nom shablonlari inglizcha |
| Semgrep (rasmiy) | Z-14 (CWE-89) | Zaharlangan ma'lumot manbasi `app.py` da, cho'kma `auth.py` da — modullararo oqim kuzatilmaydi |
| Semgrep (rasmiy) | Z-18 (CWE-22) | Xuddi shu sabab: manba `app.py:117`, cho'kma `utils.py:21` |
| Semgrep (rasmiy) | Z-15, Z-17, Z-21, Z-22, Z-24 | Ishlatilgan to'plamlarda (`p/python`, `p/security-audit`) mos qoida yo'q |
| CodeQL | Z-01, Z-11, Z-12 (CWE-798) | `security-extended` da qattiq kodlangan ma'lumotlar uchun so'rov umuman e'lon qilinmagan |
| CodeQL | Z-15 (CWE-330), Z-17 (CWE-617), Z-24 (CWE-390) | Mos so'rov to'plamga kirmaydi |
| CodeQL | Z-10 (CWE-605) | `py/bind-socket-all-network-interfaces` e'lon qilingan, lekin ishlamadi: u soket darajasidagi `bind` ni modellaydi, kod esa `app.run(host="0.0.0.0")` dan foydalanadi |
| CodeQL | Z-13, Z-16 (CWE-327) | `py/weak-cryptographic-algorithm` va `py/weak-sensitive-data-hashing` e'lon qilingan, lekin ishlamadi |
| CodeQL | Z-22 (CWE-532) | `py/clear-text-logging-sensitive-data` e'lon qilingan, lekin ishlamadi |

Manbalar: `kod/natijalar/moslashtirish.md`, `05-codeql.sarif`,
`kod/zaif-ilova/ZAIFLIKLAR.md`.

Jadvaldan ko'rinadiki, o'tkazib yuborishlar bir xil sinfdan emas. Ularni
uch toifaga ajratish mumkin.

**Birinchi toifa — qoidaning yo'qligi.** Vositada mos qoida umuman mavjud
emas yoki ishlatilgan to'plamga kirmagan. Semgrep ning beshta va CodeQL ning
oltita o'tkazib yuborishi shu toifaga kiradi. Bu texnologiyaning emas,
konfiguratsiyaning cheklovi: boshqa to'plam tanlansa yoki qoida yozilsa,
zaiflik topiladi. Buni 3.4-band bevosita isbotlaydi — maxsus qoidalar
Z-22 va Z-24 ni muammosiz aniqladi.

**Ikkinchi toifa — tahlil usulining cheklovi.** Z-14 va Z-18 ni Semgrep
topa olmadi, chunki ularning manbasi va cho'kmasi turli modullarda. Semgrep
OSS modullararo zaharlangan ma'lumot oqimini kuzatmaydi, CodeQL esa
kuzatadi — va ikkala zaiflikni ham topdi. Bu ikki nuqta 2.2-banddagi
"shablon asosidagi va semantik tahlil" farqining eng toza empirik
tasdig'idir: modullararo oqim kuzatiladigan ikkala holatda semantik tahlil
yutdi, qolgan hamma joyda farq sezilmadi.

Z-18 ayniqsa ko'rsatkichli. Uni **faqat CodeQL topdi** — Bandit ham,
Semgrep ning rasmiy qoidalari ham, hatto aynan shu zaiflik uchun atayin
yozilgan maxsus qoida ham (3.4-band) topa olmadi. Manba `app.py:117` dagi
`request.args.get("nom", "ozt.txt")`, cho'kma esa `utils.py:21` dagi
`os.path.join(YUKLAMALAR_PAPKASI, nom)`; oraliqda funksiya chaqiruvi va
modul chegarasi bor. CodeQL `py/path-injection` so'rovi bilan `utils.py:22`
da aniqladi.

**Uchinchi toifa — qoida mavjud, lekin ishga tushmadi.** Bu eng qiziq
toifa, chunki uni faqat SARIF ning e'lon qilingan so'rovlar ro'yxatini
tekshirish orqali ajratib olish mumkin. CodeQL ning to'rtta o'tkazib
yuborishi (Z-10, Z-13, Z-16, Z-22) shu toifaga kiradi: tegishli so'rov
to'plamda bor va kod ustida ishlagan, lekin natija bermagan.

Z-10 uchun sabab aniq: so'rov soket darajasidagi `bind` chaqiruvini
modellaydi, kod esa Flask ning `app.run(host="0.0.0.0")` chaqiruvidan
foydalanadi — bu kutubxona modelidagi bo'shliq.

Z-13 va Z-22 uchun sabab, ehtimol, boshqacha va u keyingi kichik bo'limning
mavzusi bilan bevosita bog'liq.

### Vositalarning o'zbekcha identifikatorlarga munosabati

Ushbu ishning eng o'ziga xos natijasi tasodifan olindi. Etalon to'plamda
qattiq kodlangan ma'lumotlar uchta zaiflik bilan ifodalangan: `SECRET_KEY`
(Z-01, inglizcha nom), `DB_PAROL` (Z-11) va `API_KALIT` (Z-12) — ikkinchisi
va uchinchisi o'zbekcha nomlangan. Uchalasi ham struktura jihatidan
bir xil: modul darajasida satr literali o'zgaruvchiga o'zlashtirilgan.

Natija keskin farqlandi. Bandit `B105` qoidasi bilan `SECRET_KEY` ni topdi,
lekin `DB_PAROL` va `API_KALIT` ni topmadi. Semgrep ning rasmiy qoidalari
ham `SECRET_KEY` ni topib (`avoid_hardcoded_config_SECRET_KEY`), qolgan
ikkitasini o'tkazib yubordi. CodeQL uchalasini ham topmadi, lekin boshqa
sababga ko'ra — uning to'plamida bu sinf uchun so'rov umuman yo'q edi.

Sabab Bandit ning `B105` qoidasi tuzilishida: u satr literali
o'zlashtirilgan o'zgaruvchi nomini inglizcha kalit so'zlar ro'yxati bilan
solishtiradi (`password`, `pass`, `secret`, `token`, `key` va shu kabilar).
`SECRET_KEY` bu ro'yxatga tushadi, `DB_PAROL` va `API_KALIT` esa tushmaydi.
Shunday qilib, **qoidaning ishlashi o'zgaruvchi nomining tiliga bog'liq**.

Bu kuzatuv CodeQL ning ikkita tushunarsiz o'tkazib yuborishini ham
izohlashi mumkin. Z-13 da parol `hashlib.md5(parol.encode())` ko'rinishida
xeshlanadi, Z-22 da esa `logging.info("... parol=%s", login, parol)`
orqali jurnalga yoziladi. Ikkala holat uchun ham tegishli so'rov SARIF da
e'lon qilingan (`py/weak-sensitive-data-hashing`,
`py/clear-text-logging-sensitive-data`), lekin ular natija bermadi. Bu
so'rovlarning ikkalasi ham ma'lumotning **maxfiy** deb tanilishini talab
qiladi, maxfiylikni aniqlash esa CodeQL da nom evristikasiga tayanadi.
O'zgaruvchi `parol` deb nomlangan — ya'ni gipoteza shundaki, bu yerda ham
til to'sig'i ishlagan.

Bu gipotezani tasdiqlash uchun nazorat tajribasi kerak: o'zgaruvchilarni
`password` ga qayta nomlab, CodeQL ni qayta ishga tushirish. Ushbu ishda
bunday tajriba o'tkazilmadi, shuning uchun Z-13 va Z-22 bo'yicha xulosa
gipoteza darajasida qoldiriladi. Bandit bo'yicha xulosa esa gipoteza emas:
u bevosita o'lchangan va uchta bir xil tuzilishdagi zaiflikning faqat
inglizcha nomlangani topilgani bilan tasdiqlanadi.

Amaliy ahamiyati jiddiy. Milliy tilda yozilgan kod bazalarida xalqaro
statik tahlil vositalarining nomga tayanadigan qoidalari ishlamay qoladi,
ishlab chiquvchi esa buni bilmaydi: vosita xato bermaydi, shunchaki jim
qoladi. Yechim — maxsus qoidalar; u 3.4-bandda ko'rib chiqiladi.

### Yolg'on ijobiy natijalarning tahlili

Jami oltita yolg'on ijobiy natija qayd etildi. Ularni ikki toifaga ajratish
mumkin (3.11-jadval).

**3.11-jadval. Yolg'on ijobiy natijalarning toifalari**

| Toifa | Vosita | Topilma | Mohiyati |
|---|---|---|---|
| I. Oqim umuman tahlil qilinmaydi | Bandit | `app.py:17` (B403, `import pickle`) | Import ko'ringani uchun ogohlantirish beriladi; modul ishlatilishi tahlil qilinmaydi |
| I | Bandit | `app.py:19` (B404, `import subprocess`) | Xuddi shunday |
| I | Bandit | `utils.py:8` (B404, `import subprocess`) | Xuddi shunday |
| II. Oqim to'g'ri, cho'kma konteksti baholanmaydi | Semgrep | `app.py:124` (`open-redirect`, CWE-601) | Qayta yo'naltirish manzili `/profil?ism=` prefiksi bilan qattiq bog'langan — tashqi saytga yo'naltirib bo'lmaydi |
| II | CodeQL | `app.py:91` (`py/reflective-xss`) | Qaytarilgan lug'at `application/json` javobiga aylanadi; brauzer uni HTML deb talqin qilmaydi |
| II | CodeQL | `app.py:101` (`py/reflective-xss`) | Xuddi shunday |

Manbalar: `kod/natijalar/metrikalar.md`, `kod/zaif-ilova/ZAIFLIKLAR.md`
(4-bo'lim).

**Birinchi toifa — eng sodda.** Bandit ning uchala yolg'on ijobiy natijasi
`import` operatorlariga berilgan ogohlantirishdir. Modulni import qilish
o'zi zaiflik emas; qoida faqat import faktini ko'radi va modul qanday
ishlatilishini umuman tahlil qilmaydi. Bunday xabarlarni konfiguratsiya
orqali o'chirish oson, lekin ularning mavjudligi vositaning tahlil
chuqurligini aniq ko'rsatadi.

**Ikkinchi toifa — ancha nozik.** Bu holatlarda qoida ma'lumot oqimini
**xatosiz** kuzatadi: SARIF dagi `codeFlows` ni tekshirganda CodeQL
manbadan cho'kmagacha bo'lgan yo'lni to'g'ri aniqlagani ko'rinadi. Xato
oqimda emas, cho'kma kontekstini baholashda.

Semgrep ning ochiq qayta yo'naltirish topilmasi ayniqsa o'rganarli.
Topilma `app.py:124` da e'lon qilingan — bu taint manbasi
(`login = request.form.get("login", "")`), cho'kma esa `app.py:129` da:
`redirect("/profil?ism=" + login)`. Qoida "so'rov ma'lumoti
`redirect()` ga yetib bordi" deb xabar beradi, lekin manzilning qattiq
kodlangan `/profil?ism=` prefiksi bilan boshlanishini hisobga olmaydi —
hujumchi faqat so'rov satri qiymatini boshqaradi va boshqa saytga
yo'naltira olmaydi. CodeQL bu yerda jim qoldi, garchi `py/url-redirection`
(CWE-601) so'rovi to'plamda e'lon qilingan bo'lsa ham: uning modeli
hujumchi host nomini o'zgartira olishini talab qiladi.

Bitta misolda ikkala yondashuvning farqi aniq ko'rinadi. Shablon asosidagi
qoida oqimni kuzatadi va ogohlantiradi; semantik so'rov zaiflikning
ekspluatatsiya qilinish shartini modellaydi va shart bajarilmasa jim
qoladi. Shu bilan birga, bu farq bir tomonlama emas: aynan CodeQL ikkita
`py/reflective-xss` yolg'on ijobiy natijasini berdi, chunki uning
modeli javobning `Content-Type` sarlavhasini hisobga olmaydi.

Bu topilmalar dastlab Z-05 va Z-06 ning takroriy xabari deb hisoblangan
edi, chunki ular ayni bir funksiya tanasida joylashgan. Tekshiruv buni rad
etdi: Z-05 va Z-06 — deserializatsiya zaifliklari (CWE-502), bu topilmalar
esa boshqa sinf (CWE-79) haqida da'vo qiladi. Tuzatishdan keyin CodeQL ning
Precision ko'rsatkichi 1,00 dan 0,88 ga, F1 esa 0,74 dan 0,70 ga tushdi.
Metodologik xulosa: takroriy xabar va yolg'on ijobiy natijani ajratishda
joylashuv emas, da'voning mazmuni hal qiluvchi bo'lishi kerak.

### Vositalarni birgalikda qo'llash

Alohida vositalarning ko'rsatkichlari ularning birgalikdagi qiymatini
ifodalamaydi. Qoplamani hisoblash uchun ochko'z (greedy) tartib qo'llandi:
har qadamda etalon to'plamga eng ko'p **yangi** zaiflik qo'shadigan vosita
tanlanadi (3.12-jadval).

**3.12-jadval. Vositalarni birgalikda qo'llashdagi qoplama**

| Qadam | Qo'shilgan vosita | Qoplama |
|---|---|---|
| 1 | Bandit | 19 / 24 |
| 2 | + Semgrep (maxsus qoidalar) | 23 / 24 |
| 3 | + CodeQL | **24 / 24** |

Manba: `kod/tahlil/diagramma.py` (`hisobot.py` moslashtirish mantiqidan
hisoblanadi).

Natija ikki xulosa beradi.

Birinchidan, **uchta vosita birgalikda to'liq qoplama beradi**, holbuki
hech biri yolg'iz 19 tadan ko'pini topmadi. Bu ishning asosiy amaliy
dalilidir va 1.2-banddagi nazariy qoidani tasdiqlaydi: usullar bir-birining
o'rnini bosmaydi, to'ldiradi.

Ikkinchidan — va bu kutilmagan natija — **Semgrep ning rasmiy qoidalari bu
ketma-ketlikka umuman kirmadi.** Ular topgan 15 ta zaiflikning hammasini
yuqoridagi uchlik allaqachon qamrab oladi, ya'ni to'plamga qo'shilganda
qoplamani bir birlikka ham oshirmaydi. Bu "ko'proq vosita — ko'proq
qoplama" degan sodda qoidani rad etadi: qo'shimcha vosita faqat boshqalar
ko'rmaydigan sinf zaifliklarni topsagina qiymat qo'shadi, aks holda u
faqat qo'shimcha xabarlar va qo'shimcha ko'rib chiqish vaqtini keltiradi.

Natijalar ikkita diagrammada ko'rsatilgan. Diagrammalardagi raqamlar
qo'lda kiritilmagan — ular `hisobot.py` ning moslashtirish mantiqidan
hisoblanadi, ya'ni vositalar chiqishi o'zgarsa rasm ham o'zgaradi.

![Vositalarning aniqlash ulushi](../kod/natijalar/rasm-1-aniqlash-ulushi.png)

*3.1-rasm. Vositalarning etalon zaifliklarni aniqlash ulushi*

![Birgalikdagi qamrov](../kod/natijalar/rasm-2-birgalikda-qamrov.png)

*3.2-rasm. Vositalarni birgalikda qo'llashdagi qamrov*

### CWE kodlarini normallashtirish muammosi

Natijalarni solishtirish jarayonida alohida texnik muammo yuzaga keldi:
vositalar ayni bir zaiflikka turli CWE kodini beradi. Misollar
`kod/natijalar/moslashtirish.md` dan: `0.0.0.0` ga bog'lanish (Z-10) —
Bandit `B104` → CWE-605, Semgrep → CWE-668; `SECRET_KEY` (Z-01) — Bandit
`B105` → CWE-259, etalon → CWE-798; SQL inyeksiyasi (Z-02) — Semgrep
`tainted-sql-string` → CWE-704, etalon → CWE-89. CodeQL esa bitta
so'rovga bir necha kod beradi: `py/path-injection` → CWE-22, 23, 36, 73, 99.

Demak CWE bo'yicha moslashtirishni to'liq avtomatlashtirib bo'lmaydi.
`hisobot.py` shu sababli bitta kod bilan emas, kodlar to'plami bilan
ishlaydi va asosiy moslashtirishni joylashuv (fayl va qator) bo'yicha
amalga oshiradi. Amaliy xulosa: bir necha SAST vositasi natijasini
birlashtiruvchi har qanday tizim CWE ni yagona kalit sifatida ishlatmasligi
kerak.

**Xulosa.** Eng yaxshi F1 ko'rsatkichini (0,83) eng sodda vosita — Bandit
ko'rsatdi, lekin bu korpus tarkibining ta'siri bo'lib, umumiy xulosa
emas. O'tkazib yuborishlarning aksariyati texnologiya cheklovi emas, qoida
to'plamining bo'shlig'i: faqat ikkita holatda (Z-14, Z-18) sabab chinakam
texnik — modullararo oqim kuzatilmasligi, va ikkalasini ham semantik tahlil
hal qildi. Yolg'on ijobiy natijalarning hammasi ikki toifaga bo'linadi:
oqim umuman tahlil qilinmaydi yoki oqim to'g'ri kuzatiladi-yu, cho'kma
konteksti baholanmaydi. Uch vosita birgalikda to'liq qoplama beradi,
to'rtinchisi esa hech narsa qo'shmaydi.

---

## 3.4. Maxsus qoida ishlab chiqish

### Muammoning qo'yilishi

3.3-bandda aniqlangan til bog'liqligi muammosi standart konfiguratsiya
doirasida hal qilinmaydi: `B105` qoidasining kalit so'zlar ro'yxatini
tashqaridan kengaytirib bo'lmaydi. Shu sababli loyihaga xos qoidalar
yozish zarurati tug'iladi.

Qoidalarni yozish uchun Semgrep tanlandi. Sabab — qoida formati YAML da
ifodalanadi va kodning o'ziga o'xshaydi, ya'ni yangi so'rov tili o'rganish
talab qilinmaydi; bundan tashqari Semgrep taint rejimini (`mode: taint`)
qo'llab-quvvatlaydi, ya'ni shablon darajasida ham, oqim darajasida ham
qoida yozish mumkin.

Jami beshta qoida ishlab chiqildi
(`kod/tahlil/qoidalar/maxsus-qoidalar.yml`). Quyida ulardan eng
ahamiyatlisi — o'zbekcha identifikatorlardagi sirlarni aniqlovchi qoida —
bosqichma-bosqich ko'rib chiqiladi.

### Qoida mantiqi

Aniqlanishi kerak bo'lgan naqsh quyidagicha: satr literali shunday
o'zgaruvchiga o'zlashtiriladiki, uning nomida maxfiylikni bildiruvchi so'z
bor. Mantiq ikki shartning kesishmasidan iborat: **strukturaviy shart** —
ifoda `$NOM = "..."` ko'rinishida bo'lishi (`"..."` — Semgrep ning istalgan
satr literalini ifodalovchi metashabloni); **nom sharti** — `$NOM`
metao'zgaruvchisi maxfiylikni bildiruvchi so'zlar ro'yxatiga mos kelishi.

Muammoning yechimi ikkinchi shartda: ro'yxatga o'zbekcha o'zaklar
(`parol`, `kalit`, `maxfiy`, `sir`, `kirish_kodi`) ham, xalqaro atama
(`token`) ham kiritiladi. Solishtirish registrga sezgir emas (`(?i)`
bayrog'i), chunki Python da bunday konstantalar bosh harflar bilan
yoziladi.

### Qoidaning YAML kodi

```yaml
- id: ozbekcha-qattiq-kodlangan-sir
  patterns:
    - pattern-either:
        - pattern: $NOM = "..."
        - pattern: $NOM = '...'
    - metavariable-regex:
        metavariable: $NOM
        regex: (?i).*(parol|kalit|maxfiy|sir|token|kirish_kodi).*
  message: >-
    Qattiq kodlangan maxfiy ma'lumot aniqlandi ($NOM). Sirlar kod
    ichida saqlanmasligi kerak — muhit o'zgaruvchisi yoki maxsus
    sir boshqaruvi tizimidan foydalaning.
  languages: [python]
  severity: ERROR
  metadata:
    cwe: "CWE-798: Use of Hard-coded Credentials"
```

Manba: `kod/tahlil/qoidalar/maxsus-qoidalar.yml`.

Qoidaning tuzilishi oddiy: `patterns` ro'yxatidagi shartlar VA mantig'i
bilan birlashtiriladi, `pattern-either` esa ichida YOKI mantig'ini beradi.
`metavariable-regex` bo'limi aynan til muammosini hal qiladigan joy.
`metadata.cwe` maydoni esa topilmaning etalon bilan avtomatik
moslashtirilishini ta'minlaydi.

### Sinov natijasi

Maxsus qoidalar to'plami 5 ta topilma berdi (3.13-jadval).

**3.13-jadval. Maxsus qoidalarning natijalari**

| Qoida | Topilma | Etalon | Jiddiylik | Boshqa vositalar topganmi |
|---|---|---|---|---|
| `flask-shablon-inyeksiyasi` | app.py:64 | Z-03 | ERROR | Semgrep (rasmiy), CodeQL |
| `ozbekcha-qattiq-kodlangan-sir` | auth.py:12 | Z-11 | ERROR | **hech biri** |
| `ozbekcha-qattiq-kodlangan-sir` | auth.py:16 | Z-12 | ERROR | **hech biri** |
| `jurnalga-maxfiy-malumot` | utils.py:54 | Z-22 | WARNING | **hech biri** |
| `etiborsiz-istisno` | utils.py:65 | Z-24 | WARNING | Bandit (`B110`) |
| `yol-boylab-harakatlanish` | — | — | — | CodeQL (Z-18 ni topdi) |

Manba: `kod/natijalar/03-semgrep-maxsus.json`.

Natija aniq: beshta topilmaning hammasi haqiqiy zaiflik, yolg'on ijobiy
natija yo'q (Precision 1,00). Muhimi esa shundaki, **uchta zaiflikni
(Z-11, Z-12, Z-22) sinovdagi boshqa hech bir vosita topmagan edi.** Ya'ni
bir nechta o'nlab qator YAML kodi uchta xalqaro vosita birgalikda ko'ra
olmagan uchta zaiflikni aniqladi.

Qoidalar to'plamining Recall ko'rsatkichi atigi 0,21 — bu kutilgan va
to'g'ri natija: qoidalar ataylab tor yozilgan, ular rasmiy to'plamlarni
almashtirish uchun emas, ulardagi aniq bo'shliqlarni to'ldirish uchun
mo'ljallangan.

### Muvaffaqiyatsiz qoida va undan olingan saboq

Beshinchi qoida — `yol-boylab-harakatlanish` — Z-18 ni aniqlash uchun
atayin yozilgan edi va **hech qanday topilma bermadi**. Bu salbiy natija
ijobiylaridan kam ahamiyatli emas.

Qoida taint rejimida yozilgan: manba sifatida `request.args.get(...)`,
cho'kma sifatida `open(...)` va `os.path.join(...)`, tozalagich sifatida
`os.path.basename(...)` va `secure_filename(...)` ko'rsatilgan. Mantiq
to'g'ri va kodda bu naqsh aynan mavjud. Lekin manba `app.py:117` da,
cho'kma esa `utils.py:21` da joylashgan, oraliqda `read_user_file(nom)`
funksiya chaqiruvi va modul chegarasi bor.

Semgrep OSS modullararo (interfile) zaharlangan ma'lumot oqimini
kuzatmaydi — taint tahlili bitta fayl doirasida bajariladi. Shuning uchun
to'g'ri yozilgan qoida ham ishlamaydi.

Bundan ikki xulosa kelib chiqadi. Birinchisi texnik: maxsus qoida
vositaning qoidalar bazasidagi bo'shliqni to'ldira oladi, lekin uning
tahlil usulidagi cheklovni chetlab o'ta olmaydi. Ikkinchisi amaliy: Z-18
ni faqat CodeQL topgani tasodif emas — modullararo oqimni talab qiladigan
zaifliklar uchun semantik tahlil muqobilsiz.

**Xulosa.** Beshta maxsus qoida yozilib, ulardan to'rttasi ishladi va uchta
zaiflikni aniqladiki, ularni sinovdagi boshqa hech bir vosita topmagan edi.
Yolg'on ijobiy natija bo'lmadi. Beshinchi qoida ishlamadi va buning sababi
qoida mantiqida emas, Semgrep OSS ning modullararo oqimni kuzatmasligida.
Maxsus qoidalar qoidalar bazasidagi bo'shliqni arzon to'ldiradi, lekin
tahlil usulining chegarasini siljita olmaydi.

---

## 3.5. CI/CD ga integratsiya

### Workflow tuzilmasi

Statik tahlil vositalarini uzluksiz integratsiya quvuriga joylashtirish
uchun GitHub Actions workflow ishlab chiqildi
(`.github/workflows/sast.yml`). U uchta hodisada ishga tushadi: `main`
shoxiga push qilinganda, pull request ochilganda va har dushanba soat
06:00 (UTC) da jadval bo'yicha. Oxirgisi muhim: kod o'zgarmasa ham, yangi
CVE lar e'lon qilinishi bog'liqliklar holatini o'zgartiradi.

Workflow beshta ishdan iborat: Bandit tahlili, Semgrep tahlili (rasmiy va
maxsus qoidalar), CodeQL tahlili, bog'liqliklar tahlili va yakuniy umumiy
hisobot. Birinchi to'rttasi parallel bajariladi, beshinchisi `needs` orqali
ularning natijasini kutadi. Ruxsatlar eng kam imtiyoz tamoyili bo'yicha
berilgan: `contents: read` va `security-events: write`.

### SARIF va natijalarni birlashtirish

Har bir vosita o'z natijasini SARIF formatida chiqaradi va
`github/codeql-action/upload-sarif@v4` amali orqali yuklanadi. Har bir
yuklashga alohida `category` beriladi (`bandit`, `semgrep`,
`semgrep-maxsus`, `codeql-python`), aks holda keyingi yuklash
oldingisining natijalarini almashtirib yuboradi. Aynan shu nuqta birinchi
ishga tushirishda nuqson sifatida namoyon bo'ldi: `semgrep-maxsus.sarif`
yaratilar, lekin yuklash bosqichi faqat `semgrep.sarif` ni olardi —
natijada 3.4-bandning asosiy natijasi Security tabiga umuman yetib
bormasdi. Shu yerda 1.3-bandda bayon etilgan SARIF ning amaliy qiymati
ko'rinadi: to'rtta turli vosita natijasi bitta formatda jamlanadi.

### Sifat darvozasi

Workflow da ikkita sifat darvozasi o'rnatilgan.

**Bandit darvozasi** alohida bosqich sifatida bajariladi va tahlil
bosqichidan ajratilgan. Tahlil bosqichi `--exit-zero` bilan ishlaydi (uning
vazifasi — SARIF yaratish), darvoza esa chegara bilan qayta ishga
tushiriladi:

```yaml
- name: Sifat darvozasi
  run: |
    bandit -r kod/zaif-ilova \
      --severity-level high \
      --confidence-level medium
```

Chegara tanlovi tasodifiy emas. Lokal natijalarga ko'ra bu shartga 22 ta
topilmadan 8 tasi javob beradi; past jiddiylikdagi yettita xabar, shu
jumladan uchta yolg'on ijobiy natija (`import pickle`, `import subprocess`),
darvozadan o'tib ketadi. Ya'ni darvoza qurilishni faqat jiddiy topilma
uchun to'xtatadi va yolg'on ijobiy natijalar tufayli ishga tushmaydi — bu
1.3-bandda ta'riflangan muvozanatning amaliy ifodasi.

**SCA darvozasi** pip-audit ni ikkinchi marta, bu safar `|| true` siz ishga
tushiradi: zaif bog'liqlik topilsa, vosita noldan farqli kod bilan tugaydi
va ish to'xtaydi.

### Ishga tushirish natijalari

Workflow `nyxeldev/kurs-ishi-sast` omborida bir necha marta ishga
tushirildi. Oxirgi ishning natijalari 3.14-jadvalda.

**3.14-jadval. Workflow ishlarining natijalari**

| Ish | Natija | Vaqt | Izoh |
|---|---|---|---|
| Bandit tahlili | xato | 19 s | tahlil va SARIF yuklash muvaffaqiyatli, **sifat darvozasi** ataylab to'xtatdi |
| Semgrep tahlili | muvaffaqiyatli | 38 s | ikkita SARIF yuklandi (rasmiy + maxsus) |
| CodeQL tahlili | muvaffaqiyatli | 51 s | `security-extended` |
| Bog'liqliklar tahlili | xato | 18 s | hisobot va artefakt muvaffaqiyatli, **sifat darvozasi** to'xtatdi |
| Umumiy hisobot | muvaffaqiyatli | 6 s | `$GITHUB_STEP_SUMMARY` jadvali |

Manba: `HOLAT.md` (GitHub Actions ishi, CodeQL Action v4 bilan).

Ikkala "xato" ham kutilgan: sifat darvozalari ataylab zaif kod bazasida
ishga tushdi. Barcha tahlil va SARIF yuklash bosqichlari muvaffaqiyatli
o'tdi.

GitHub Security tabidagi ogohlantirishlar soni 3.15-jadvalda.

**3.15-jadval. GitHub Security tabidagi ogohlantirishlar**

| Vosita | Kategoriya | Ogohlantirish |
|---|---|---|
| Semgrep OSS | `semgrep` | 26 |
| Bandit | `bandit` | 22 |
| CodeQL | `codeql-python` | 17 |
| Semgrep OSS (maxsus) | `semgrep-maxsus` | 5 |
| **Jami** | | **70** |

Manba: `HOLAT.md` (GitHub Security tab natijalari).

Raqamlar lokal ishga tushirish natijalariga to'liq mos keldi: 26, 22, 17
va 5. Bu amaliy qismning takrorlanuvchanligini tasdiqlaydi — CI va lokal
muhit, turli operatsion tizim va Python versiyasiga qaramay, bir xil
topilmalarni berdi.

### Joriy etish bo'yicha tavsiyalar

Olingan natijalar asosida quyidagi tavsiyalarni shakllantirish mumkin.

**Vositalarni tanlash.** Bitta vosita bilan cheklanmaslik kerak: to'liq
qoplama faqat uchta vosita birgalikda erishildi (3.12-jadval). Bazaviy
daraja — tilga ixtisoslashgan tez vosita (Bandit, 2 soniya) har bir
commit da; semantik tahlil (CodeQL) modullararo oqimni talab qiladigan
zaifliklarni qoplaydi; SCA esa statik tahlil umuman ko'rmaydigan sohani —
bog'liqliklarni — tekshiradi.

**Qo'shimcha vositani asoslash.** Yangi vosita to'plamga faqat boshqalar
ko'rmaydigan sinf zaifliklarni topsagina qo'shilishi kerak. Semgrep ning
rasmiy qoidalari misolida bu shart bajarilmadi: 26 ta qo'shimcha xabar
berib, qoplamani bir birlikka ham oshirmadi.

**Maxsus qoidalar va darvoza.** Milliy tilda yozilgan kod bazalari uchun
maxsus qoidalar zarur: Z-11, Z-12 va Z-22 ni faqat ular topdi, narxi esa
bir necha o'nlab qator YAML. Darvoza chegarasi yolg'on ijobiy natijalar
tushmaydigan qilib tanlanadi, aks holda u birinchi haftadayoq chetlab
o'tila boshlanadi. Har bir vosita natijasi esa o'z kategoriyasi bilan
SARIF da yuklanishi shart — aks holda bir qismi jimgina yo'qoladi.

**Xulosa.** Beshta ishdan iborat workflow ishlab chiqildi va amalda ishga
tushirildi: to'rtta vosita natijasi SARIF orqali bitta interfeysda
jamlandi, ikkita sifat darvozasi esa zaif kod bazasida kutilganidek
qurilishni to'xtatdi. CI dagi topilmalar soni lokal natijalarga to'liq mos
keldi, bu amaliy qismning takrorlanuvchanligini tasdiqlaydi. Integratsiya
jarayonida ikkita haqiqiy nuqson aniqlanib tuzatildi, shundan biri — maxsus
qoidalar natijasining yo'qolishi — ishning asosiy natijasini Security
tabidan butunlay yashirgan bo'lardi.
