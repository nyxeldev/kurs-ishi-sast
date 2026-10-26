# ILOVALAR

## A ilovasi. Tasnif tizimlarining ma'lumotnoma jadvallari

**A.1-jadval. CWE Top 25 (2025) ro'yxatining birinchi o'nligi**

| O'rin | CWE | Nuqson nomi |
|---|---|---|
| 1 | CWE-79 | Veb-sahifa shakllantirishda kiritishni noto'g'ri neytrallash (saytlararo skript bajarish, XSS) |
| 2 | CWE-89 | SQL buyrug'idagi maxsus elementlarni noto'g'ri neytrallash (SQL inyeksiyasi) |
| 3 | CWE-352 | Saytlararo so'rovni qalbakilashtirish (CSRF) |
| 4 | CWE-862 | Avtorizatsiyaning yo'qligi |
| 5 | CWE-787 | Chegaradan tashqariga yozish |
| 6 | CWE-22 | Fayl yo'lini cheklangan katalog bilan chegaralamaslik (yo'l bo'ylab harakatlanish) |
| 7 | CWE-416 | Bo'shatilgandan keyin foydalanish |
| 8 | CWE-125 | Chegaradan tashqaridan o'qish |
| 9 | CWE-78 | OS buyrug'idagi maxsus elementlarni noto'g'ri neytrallash (buyruq inyeksiyasi) |
| 10 | CWE-94 | Kod generatsiyasini noto'g'ri nazorat qilish (kod inyeksiyasi) |

Manba: [2]. Matndagi havola: 1.1-band.

**A.2-jadval. OWASP Top 10:2025 toifalari**

| Kod | Toifa nomi |
|---|---|
| A01 | Buzilgan kirish nazorati |
| A02 | Xavfsizlik konfiguratsiyasidagi xatolar |
| A03 | Ta'minot zanjiridagi nuqsonlar |
| A04 | Kriptografik nuqsonlar |
| A05 | Inyeksiya |
| A06 | Xavfsiz bo'lmagan loyihalash |
| A07 | Autentifikatsiya nuqsonlari |
| A08 | Dasturiy ta'minot yoki ma'lumotlar yaxlitligidagi nuqsonlar |
| A09 | Xavfsizlik jurnali va ogohlantirishlaridagi nuqsonlar |
| A10 | Istisno holatlarini noto'g'ri boshqarish |

Manba: [3]. Matndagi havola: 1.1-band.

---

## B ilovasi. Etalon to'plam

**B.1-jadval. Sinov ilovasiga kiritilgan zaifliklarning to'liq ro'yxati**

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

Manba: `kod/zaif-ilova/ZAIFLIKLAR.md`. Matndagi havola: 3.1-band.

---

## C ilovasi. Vositalar natijalarining to'liq jadvallari

**C.1-jadval. Zaifliklarning vositalar bo'yicha aniqlanishi**

| Kod | CWE | Bandit | Semgrep (rasmiy) | Semgrep (maxsus) | CodeQL |
|---|---|---|---|---|---|
| Z-01 | CWE-798 | + | + | − | − |
| Z-02 | CWE-89 | + | + | − | + |
| Z-03 | CWE-79 | − | + | + | + |
| Z-04 | CWE-78 | + | + | − | + |
| Z-05 | CWE-502 | + | + | − | + |
| Z-06 | CWE-502 | + | + | − | + |
| Z-07 | CWE-94 | + | + | − | + |
| Z-08 | CWE-78 | + | + | − | + |
| Z-09 | CWE-489 | + | + | − | + |
| Z-10 | CWE-605 | + | + | − | − |
| Z-11 | CWE-798 | − | − | + | − |
| Z-12 | CWE-798 | − | − | + | − |
| Z-13 | CWE-327 | + | + | − | − |
| Z-14 | CWE-89 | + | − | − | + |
| Z-15 | CWE-330 | + | − | − | − |
| Z-16 | CWE-327 | + | + | − | − |
| Z-17 | CWE-617 | + | − | − | − |
| Z-18 | CWE-22 | − | − | − | + |
| Z-19 | CWE-78 | + | + | − | + |
| Z-20 | CWE-295 | + | + | − | + |
| Z-21 | CWE-377 | + | − | − | + |
| Z-22 | CWE-532 | − | − | + | − |
| Z-23 | CWE-732 | + | + | − | + |
| Z-24 | CWE-390 | + | − | + | − |
| **Jami** | | **19** | **15** | **5** | **14** |

`+` — aniqlandi, `−` — o'tkazib yuborildi.
Manba: `kod/natijalar/qiyosiy-jadval.md`. Matndagi havola: 3.3-band.

**C.2-jadval. O'tkazib yuborilgan zaifliklar va ularning sabablari**

| Vosita | Zaiflik | Sababi |
|---|---|---|
| Bandit | Z-03 | Shablon mexanizmi semantikasi modellanmagan: `render_template_string` qora ro'yxatda yo'q |
| Bandit | Z-11, Z-12 | `B105` faqat inglizcha nomlarni taniydi |
| Bandit | Z-18 | Ma'lumot oqimi tahlili yo'q; `os.path.join` o'zi xavfli chaqiruv emas |
| Bandit | Z-22 | Argumentning maxfiyligini aniqlash qoidasi yo'q |
| Semgrep (rasmiy) | Z-11, Z-12 | Rasmiy qoidalardagi nom shablonlari inglizcha |
| Semgrep (rasmiy) | Z-14 | Manba `app.py` da, cho'kma `auth.py` da — modullararo oqim kuzatilmaydi |
| Semgrep (rasmiy) | Z-18 | Xuddi shu sabab: manba `app.py:117`, cho'kma `utils.py:21` |
| Semgrep (rasmiy) | Z-15, Z-17, Z-21, Z-22, Z-24 | Ishlatilgan to'plamlarda mos qoida yo'q |
| CodeQL | Z-01, Z-11, Z-12 | `security-extended` da qattiq kodlangan ma'lumot so'rovi e'lon qilinmagan |
| CodeQL | Z-15, Z-17, Z-24 | Mos so'rov to'plamga kirmaydi |
| CodeQL | Z-10 | `py/bind-socket-all-network-interfaces` e'lon qilingan, lekin soket `bind` ni modellaydi; kod `app.run(host="0.0.0.0")` dan foydalanadi |
| CodeQL | Z-13, Z-16 | `py/weak-cryptographic-algorithm` va `py/weak-sensitive-data-hashing` e'lon qilingan, lekin ishlamadi |
| CodeQL | Z-22 | `py/clear-text-logging-sensitive-data` e'lon qilingan, lekin ishlamadi |

Manbalar: `kod/natijalar/moslashtirish.md`, `05-codeql.sarif`.
Matndagi havola: 3.3-band.

**C.3-jadval. CodeQL: natija qaytargan so'rovlar**

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

SARIF da 50 ta so'rov e'lon qilingan, natija qaytargani — 11 tasi.
Manba: `kod/natijalar/05-codeql.sarif`. Matndagi havola: 3.2-band.

**Bandit chiqishining tipik ko'rinishi**

```
>> Issue: [B105:hardcoded_password_string] Possible hardcoded password:
   's3cr3t-kalit-2024-oz'
   Severity: Low   Confidence: Medium
   CWE: CWE-259 (https://cwe.mitre.org/data/definitions/259.html)
   Location: .../app.py:30:11
```

Manba: `kod/natijalar/01-bandit.txt`.

---

## D ilovasi. CI/CD quvurining natijalari

**D.1-jadval. Workflow ishlarining natijalari**

| Ish | Natija | Vaqt | Izoh |
|---|---|---|---|
| Bandit tahlili | xato | 19 s | tahlil va SARIF yuklash muvaffaqiyatli, **sifat darvozasi** ataylab to'xtatdi |
| Semgrep tahlili | muvaffaqiyatli | 38 s | ikkita SARIF yuklandi |
| CodeQL tahlili | muvaffaqiyatli | 51 s | `security-extended` |
| Bog'liqliklar tahlili | xato | 18 s | hisobot muvaffaqiyatli, **sifat darvozasi** to'xtatdi |
| Umumiy hisobot | muvaffaqiyatli | 6 s | `$GITHUB_STEP_SUMMARY` jadvali |

**D.2-jadval. GitHub Security tabidagi ogohlantirishlar**

| Vosita | Kategoriya | Ogohlantirish |
|---|---|---|
| Semgrep OSS | `semgrep` | 26 |
| Bandit | `bandit` | 22 |
| CodeQL | `codeql-python` | 17 |
| Semgrep OSS (maxsus) | `semgrep-maxsus` | 5 |
| **Jami** | | **70** |

Manba: `HOLAT.md` (GitHub Actions ishi). Matndagi havola: 3.5-band.

---

## Qo'shilishi kerak bo'lgan ilovalar

Quyidagi materiallar omborda mavjud, lekin hujjatga hali kiritilmagan:

- **E ilovasi.** Sinov ilovasining to'liq kodi — `kod/zaif-ilova/`
  (`app.py`, `auth.py`, `utils.py`, `requirements.txt`)
- **F ilovasi.** Maxsus Semgrep qoidalarining to'liq fayli —
  `kod/tahlil/qoidalar/maxsus-qoidalar.yml`
- **G ilovasi.** GitHub Actions workflow fayli —
  `.github/workflows/sast.yml`
- **H ilovasi.** Vositalarning to'liq moslashtirish jurnali —
  `kod/natijalar/moslashtirish.md`
- **I ilovasi.** Skrinshotlar: vositalar chiqishi va GitHub Security
  tabi (hali olinmagan)
