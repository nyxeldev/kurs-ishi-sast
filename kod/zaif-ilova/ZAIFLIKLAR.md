# Etalon to'plam (Ground Truth)

Sinov ilovasiga **ataylab kiritilgan** zaifliklarning to'liq ro'yxati.
Statik tahlil vositalarining aniqlik metrikalarini hisoblash uchun asos.

Qator raqamlari tekshirilgan (Python 3.12, 2026-yil oktyabr holatiga).

---

## 1. Zaifliklar ro'yxati

| № | Fayl | Qator | CWE | Zaiflik nomi | Jiddiylik |
|---|---|---|---|---|---|
| Z-01 | app.py | 30 | CWE-798 | Qattiq kodlangan maxfiy kalit (SECRET_KEY) | O'rta |
| Z-02 | app.py | 48 | CWE-89 | SQL inyeksiyasi (`%`-formatlash) | Yuqori |
| Z-03 | app.py | 64 | CWE-79 | XSS / SSTI (`render_template_string`) | Yuqori |
| Z-04 | app.py | 73 | CWE-78 | Buyruq inyeksiyasi (`subprocess`, shell=True) | Kritik |
| Z-05 | app.py | 90 | CWE-502 | Xavfsiz bo'lmagan `yaml.load` | Yuqori |
| Z-06 | app.py | 100 | CWE-502 | `pickle.loads` ishonchsiz manbadan | Kritik |
| Z-07 | app.py | 110 | CWE-94 | Kod inyeksiyasi (`eval`) | Kritik |
| Z-08 | app.py | 141 | CWE-78 | Buyruq inyeksiyasi (`os.system`) | Kritik |
| Z-09 | app.py | 148 | CWE-489 | `debug=True` ishlab chiqarish rejimida | Yuqori |
| Z-10 | app.py | 148 | CWE-605 | Barcha interfeyslarga bog'lanish (0.0.0.0) | O'rta |
| Z-11 | auth.py | 12 | CWE-798 | Qattiq kodlangan MB paroli (`DB_PAROL`) | Yuqori |
| Z-12 | auth.py | 16 | CWE-798 | Qattiq kodlangan API kaliti (`API_KALIT`) | Yuqori |
| Z-13 | auth.py | 25 | CWE-327 | Parol uchun MD5, tuzsiz | Yuqori |
| Z-14 | auth.py | 34 | CWE-89 | SQL inyeksiyasi (f-satr) | Yuqori |
| Z-15 | auth.py | 50 | CWE-330 | Token uchun `random` moduli | O'rta |
| Z-16 | auth.py | 57 | CWE-327 | SHA-1 xesh funksiyasi | O'rta |
| Z-17 | auth.py | 64 | CWE-617 | Huquq tekshiruvi uchun `assert` | O'rta |
| Z-18 | utils.py | 21 | CWE-22 | Yo'l bo'ylab harakatlanish | Yuqori |
| Z-19 | utils.py | 30 | CWE-78 | Buyruq inyeksiyasi (`subprocess.run`) | Kritik |
| Z-20 | utils.py | 37 | CWE-295 | TLS tekshiruvi o'chirilgan (`verify=False`) | Yuqori |
| Z-21 | utils.py | 45 | CWE-377 | Xavfsiz bo'lmagan vaqtinchalik fayl | Past |
| Z-22 | utils.py | 54 | CWE-532 | Parol jurnalga yozilmoqda | O'rta |
| Z-23 | utils.py | 60 | CWE-732 | Juda keng fayl huquqlari (0o777) | O'rta |
| Z-24 | utils.py | 65 | CWE-390 | E'tiborsiz qoldirilgan istisno | Past |

**Jami: 24 ta zaiflik, 15 xil CWE toifasi.**

### Bog'liqliklardagi zaifliklar (SCA uchun alohida)

`requirements.txt` da ataylab eskirgan versiyalar qoldirilgan:
Flask 0.12.2, Jinja2 2.10, Werkzeug 0.14.1, PyYAML 5.1, requests 2.19.1, urllib3 1.24.1.

Bu zaifliklar SAST vositalari tomonidan **topilmasligi kerak** — ularni
faqat SCA vositasi (pip-audit) aniqlaydi. Aniq CVE ro'yxati pip-audit
chiqishidan olinadi va `kod/natijalar/` ga yoziladi.

---

## 2. CWE bo'yicha taqsimot

| CWE | Soni | Toifa |
|---|---|---|
| CWE-78 | 3 | Buyruq inyeksiyasi |
| CWE-798 | 3 | Qattiq kodlangan ma'lumot |
| CWE-89 | 2 | SQL inyeksiyasi |
| CWE-502 | 2 | Xavfsiz bo'lmagan deserializatsiya |
| CWE-327 | 2 | Zaif kriptografiya |
| Qolganlari | 12 | Har biridan 1 ta |

---

## 3. Dastlabki sinov natijalari

> Bu raqamlar tekshirish uchun olingan. Yakuniy jadval `kod/natijalar/`
> dagi to'liq tahlildan keyin shakllantiriladi.

**Bandit 1.9.4:** 22 ta topilma

Topdi (19/24): Z-01, Z-02, Z-04, Z-05, Z-06, Z-07, Z-08, Z-09, Z-10,
Z-13, Z-14, Z-15, Z-16, Z-17, Z-19, Z-20, Z-21, Z-23, Z-24

**O'tkazib yubordi:**

| Zaiflik | Sabab |
|---|---|
| Z-03 (XSS) | Bandit shablon mexanizmlari semantikasini bilmaydi |
| Z-11, Z-12 (sirlar) | B105 qoidasi faqat **inglizcha** nomlarni taniydi (`password`, `secret`, `key`) — `DB_PAROL`, `API_KALIT` shablonga tushmaydi |
| Z-18 (path traversal) | Ma'lumot oqimi tahlili yo'q, faqat chaqiruv shabloni |
| Z-22 (jurnal) | Maxfiy ma'lumotni kuzatish qoidasi mavjud emas |

**Yolg'on ijobiy natijalar (3 ta):** `import pickle` (q.17), `import subprocess`
(app.py q.19, utils.py q.8) — import o'zi zaiflik emas, faqat ogohlantirish.

**Maxsus Semgrep qoidalari:** 5 ta topilma — Z-03, Z-11, Z-12, Z-22, Z-24.
Shundan to'rttasi (Z-03, Z-11, Z-12, Z-22) Bandit o'tkazib yuborgan
zaifliklardir; Z-24 ni Bandit ham (B110) aniqlagan.

Z-18 (yo'l bo'ylab harakatlanish) uchun maxsus qoida yozilgan bo'lsa-da,
topilma bermadi: manba (`request.args.get` — app.py) va cho'kma
(`os.path.join` — utils.py) turli modullarda joylashgan, Semgrep OSS esa
modullararo zaharlangan ma'lumot oqimini kuzatmaydi. Natijada Z-18 ni
sinovdagi hech bir vosita topmadi.

---

## 4. Tasdiqlangan yolg'on ijobiy natijalar

Quyidagi topilmalar qo'lda tekshirilib, yolg'on ijobiy natija deb
tasdiqlandi. Ikkalasi ham bir xil sababga ega: qoida ma'lumot oqimini
to'g'ri kuzatadi, lekin **cho'kmaning kontekstini** baholamaydi — ya'ni
ma'lumot yetib borgan joyda u haqiqatan zarar keltira oladimi, degan
savolni so'ramaydi.

`kod/tahlil/hisobot.py` dagi `TASDIQLANGAN_FP` ro'yxati 4.2-banddagi
ikkita topilmani yolg'on ijobiy deb belgilaydi (4.1-dagi topilma etalonga
yaqin emasligi uchun avtomatik ravishda shunday hisoblanadi).

### 4.1. Ochiq qayta yo'naltirish — Semgrep

Semgrep ning rasmiy `python.flask.security.open-redirect.open-redirect`
qoidasi `app.py:124` da topilma beradi va uni CWE-601 (ochiq qayta
yo'naltirish, open redirect) deb belgilaydi. Topilma etalon ro'yxatda
yo'q edi, shuning uchun u dastlab etalonning kamchiligi deb taxmin
qilindi va Z-25 sifatida ro'yxatga qo'shish ko'rib chiqildi.

Tekshiruv bu taxminni rad etdi.

**Kod:**

```python
javob = redirect("/profil?ism=" + login)
```

**Sabab.** Qayta yo'naltirish manzili har doim `/profil?ism=` bilan
boshlanadi — bu sayt ichidagi nisbiy yo'l. Hujumchi faqat so'rov satri
(query string) qiymatini boshqaradi, satrning boshini emas. Shu sababli
`//evil.com` yoki `https://evil.com` ko'rinishidagi tashqi manzilni
hosil qilib bo'lmaydi. Boshqa saytga yo'naltirish imkoni bo'lmasa,
CWE-601 ta'rifi bajarilmaydi.

**Vositalarning xulq-atvori:**

| Vosita | Natija | Sababi |
|---|---|---|
| Semgrep (rasmiy) | topilma berdi | taint qoidasi: "so'rov ma'lumoti `redirect()` ga yetib bordi". Cho'kmadagi manzil qattiq kodlangan prefiks bilan bog'lanmaganmi — tekshirmaydi |
| CodeQL | topilma bermadi | `py/url-redirection` (CWE-601) so'rovi ishga tushdi va SARIF da e'lon qilingan, lekin natija bermadi: uning modeli hujumchi host'ni o'zgartira olishini talab qiladi |
| Bandit | topilma bermadi | bunday qoida umuman yo'q |

**Xulosa.** Bu topilma — **haqiqiy yolg'on ijobiy natija**, etalonning
kamchiligi emas. Z-25 sifatida qo'shilmadi: qo'shilganda Semgrep ning
Precision ko'rsatkichi sun'iy ravishda 1.00 ga ko'tarilar, to'g'ri
ishlagan CodeQL esa o'tkazib yuborish (FN) uchun jazolanar edi.

Ish uchun ahamiyati (3.3-band, yolg'on ijobiy natijalar tahlili): bu
bitta misolda shablon asosidagi va semantik tahlil o'rtasidagi farq
ko'rinadi. Semgrep ma'lumot oqimini kuzatadi, lekin cho'kmaning
kontekstini baholamaydi; CodeQL zaiflikning ekspluatatsiya qilinish
shartini modellashtiradi va shu sababli jim qoladi. Yolg'on ijobiy
natijalarning katta qismi aynan shunday — qoida to'g'ri ishlaydi, lekin
uning modeli haqiqiy xavfni ifodalash uchun yetarlicha nozik emas.

### 4.2. JSON javobidagi aks etgan XSS — CodeQL

CodeQL ning `py/reflective-xss` qoidasi uch joyda ishga tushdi:
`app.py:64`, `app.py:91` va `app.py:101`. Birinchisi to'g'ri — u Z-03
(`render_template_string`) ni ko'rsatadi. Qolgan ikkitasi yolg'on ijobiy.

**Kod:**

```python
konfig = yaml.load(matn)        # 90-qator, Z-05
return {"konfig": konfig}       # 91-qator — CodeQL shu yerni belgilaydi

holat = pickle.loads(maydon)    # 100-qator, Z-06
return {"holat": str(holat)}    # 101-qator — CodeQL shu yerni belgilaydi
```

**Oqim to'g'ri.** SARIF dagi `codeFlows` ni tekshirganda ko'rinadiki,
CodeQL manbadan (`request.form.get`, `request.files`) cho'kmagacha
(`Dict` — ko'rinishning qaytish qiymati) oqimni xatosiz kuzatgan.

**Sabab.** Flask 1.1.0 (2019-yil 4-iyul) dan boshlab ko'rinishdan
qaytarilgan lug'at `jsonify()` orqali `application/json` javobiga
aylanadi. Brauzer bunday javobni HTML sifatida talqin qilmaydi, demak
skript bajarilmaydi — aks etgan XSS uchun shart bajarilmaydi. Qo'shimcha
ravishda ikkala marshrut ham faqat POST ni qabul qiladi, bu esa aks etgan
XSS ni ekspluatatsiya qilishni yanada qiyinlashtiradi.

`py/reflective-xss` qoidasining rasmiy tavsifi javob turini umuman
tilga olmaydi: u "foydalanuvchi kiritmasini tozalamasdan veb-sahifaga
yozish" deb ta'riflanadi. Ya'ni qoida `Content-Type` ni modellashtirmaydi.

**Qo'shimcha kuzatuv.** `requirements.txt` da Flask 0.12.2 qadalgan, unda
ko'rinishdan lug'at qaytarish umuman qo'llab-quvvatlanmaydi (bu imkoniyat
1.1.0 da qo'shilgan). Ya'ni qadalgan muhitda bu kod ishlamay, xato
bergan bo'lardi. Bu statik tahlilning yana bir cheklovini ko'rsatadi:
vosita kutubxonaning zamonaviy modelidan foydalanadi va loyihada
qadalgan versiyani hisobga olmaydi.

**Nega "takroriy" emas.** Dastlab bu topilmalar Z-05 va Z-06 ning
takroriy xabari deb hisoblangan edi, chunki ular ayni bir funksiya
tanasida joylashgan. Bu noto'g'ri: Z-05 va Z-06 — deserializatsiya
zaifliklari (CWE-502), bu topilmalar esa boshqa sinf (CWE-79) haqida
da'vo qiladi. Ularni takroriy deb sanash CodeQL Z-05/Z-06 ni
tasdiqlagandek ko'rsatardi, holbuki u butunlay boshqa narsa haqida
xabar bergan.

**Metrikaga ta'siri.** CodeQL ning Precision ko'rsatkichi 1.00 dan
0.88 ga (14 / 16), F1 esa 0.74 dan 0.70 ga tushdi. Ya'ni sinovdagi
hech bir vosita mukammal aniqlikka erishmadi.

---

## 5. Muhim kuzatuv (kurs ishi uchun)

Bandit ning qattiq kodlangan sirlarni aniqlash qoidasi **o'zgaruvchi
nomining tiliga bog'liq**. Ingliz tilidagi `SECRET_KEY` topildi, lekin
o'zbekcha `DB_PAROL` va `API_KALIT` topilmadi.

Bu — ishda alohida muhokama qilishga arziydigan natija: xalqaro statik
tahlil vositalari ingliz tilidagi kod bazalariga sozlangan va milliy
tillardagi loyihalarda aniqlik darajasi pasayadi. Yechim — maxsus
qoidalar (3.4-band).

---

## 6. Metrikalarni hisoblash

```
TP = etalon ro'yxatdan to'g'ri topilganlar soni
FP = zaiflik bo'lmagan joyga berilgan ogohlantirishlar
FN = o'tkazib yuborilgan zaifliklar (24 - TP)

Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
F1        = 2 * (Precision * Recall) / (Precision + Recall)
```

Hisoblash `kod/tahlil/hisobot.py` skripti orqali avtomatlashtirilgan.
