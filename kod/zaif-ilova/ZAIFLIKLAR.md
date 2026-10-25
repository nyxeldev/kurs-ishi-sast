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

## 4. Muhim kuzatuv (kurs ishi uchun)

Bandit ning qattiq kodlangan sirlarni aniqlash qoidasi **o'zgaruvchi
nomining tiliga bog'liq**. Ingliz tilidagi `SECRET_KEY` topildi, lekin
o'zbekcha `DB_PAROL` va `API_KALIT` topilmadi.

Bu — ishda alohida muhokama qilishga arziydigan natija: xalqaro statik
tahlil vositalari ingliz tilidagi kod bazalariga sozlangan va milliy
tillardagi loyihalarda aniqlik darajasi pasayadi. Yechim — maxsus
qoidalar (3.4-band).

---

## 5. Metrikalarni hisoblash

```
TP = etalon ro'yxatdan to'g'ri topilganlar soni
FP = zaiflik bo'lmagan joyga berilgan ogohlantirishlar
FN = o'tkazib yuborilgan zaifliklar (24 - TP)

Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
F1        = 2 * (Precision * Recall) / (Precision + Recall)
```

Hisoblash `kod/tahlil/hisobot.py` skripti orqali avtomatlashtirilgan.
