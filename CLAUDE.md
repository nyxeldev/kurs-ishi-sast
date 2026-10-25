# Kurs ishi loyihasi — kontekst fayli

Bu fayl Claude Code va Claude Cowork tomonidan avtomatik o'qiladi.
Har safar kontekstni qaytadan tushuntirish shart emas.

---

## 1. Loyiha haqida

**Mavzu:** Statik kod tahlili vositalarining dasturiy xavfsizlikni ta'minlashdagi o'rni

**Tur:** Kurs ishi
**Hajm:** 35–45 bet (ilovalarsiz)
**Til:** O'zbek tili (lotin yozuvi)
**Amaliy qism tili:** Python 3.12
**Muallif:** Jahongir

---

## 2. Muhim qoidalar

### Til va uslub
- **Barcha matn o'zbek tilida yoziladi.** Kod izohlari ham o'zbekcha.
- Ilmiy-texnik uslub. "Men", "biz qildik" o'rniga: "tahlil qilindi", "natijalar ko'rsatadiki".
- Texnik atamalar birinchi marta kelganda qavs ichida inglizchasi beriladi:
  "zaharlangan ma'lumot tahlili (taint analysis)".
- Keyingi o'rinlarda faqat o'zbekcha atama ishlatiladi.
- Qisqartmalar birinchi marta ochib yoziladi: SAST (Static Application Security Testing).

### Faktlar bilan ishlash
- **Hech qanday raqam yoki statistika o'ylab topilmaydi.** Har bir raqamning manbasi bo'lishi shart.
- Agar manba topilmasa — raqam umuman yozilmaydi, taxminiy qiymat qo'yilmaydi.
- Amaliy qismdagi barcha jadvallar faqat `kod/natijalar/` dagi haqiqiy chiqish fayllaridan to'ldiriladi.
- Vositalar versiyalari har doim `--version` chiqishidan olinadi, xotiradan emas.

### Formatlash
- Boblar: `1.1.`, `1.2.` ko'rinishida raqamlanadi
- Jadvallar: "1.1-jadval. Nomi" (tepada), rasmlar: "2.3-rasm. Nomi" (pastda)
- Manbalarga havola matn ichida kvadrat qavsda: [12]
- Adabiyotlar ro'yxati raqamlangan, GOST uslubida

---

## 3. Papka tuzilmasi

```
kurs-ishi/
├── CLAUDE.md              <- shu fayl
├── README.md              <- ish tartibi bo'yicha qo'llanma
├── reja.md                <- tasdiqlangan reja, bet taqsimoti bilan
├── HOLAT.md               <- bajarilgan/qolgan ishlar ro'yxati
│
├── kod/                   <- CLAUDE CODE shu yerda ishlaydi
│   ├── zaif-ilova/        <- sinov obyekti (ataylab zaif Flask ilovasi)
│   │   ├── app.py
│   │   ├── auth.py
│   │   ├── utils.py
│   │   ├── requirements.txt
│   │   └── ZAIFLIKLAR.md  <- ground truth: qaysi qatorda qaysi CWE
│   ├── tahlil/
│   │   ├── tahlil.sh      <- barcha vositalarni ishga tushirish
│   │   ├── hisobot.py     <- natijalarni normallashtirib jadval yasash
│   │   └── qoidalar/      <- Semgrep uchun maxsus qoidalar
│   └── natijalar/         <- vositalar chiqishi (JSON/SARIF) + jadvallar
│
├── matn/                  <- COWORK shu yerda ishlaydi
│   ├── 00-kirish.md
│   ├── 01-bob.md
│   ├── 02-bob.md
│   ├── 03-bob.md
│   ├── 04-xulosa.md
│   └── adabiyotlar.md
│
├── manbalar/              <- yuklab olingan PDF/maqolalar
├── ilovalar/              <- tayyor hujjatlar (docx) va skrinshotlar
└── .github/workflows/     <- CI/CD namunasi
```

---

## 4. Qaysi agent nima qiladi

### Claude Code (terminal kerak bo'lgan ishlar)
- Zaif ilovani yozish va tekshirish
- `pip install` va vositalarni o'rnatish
- Bandit, Semgrep, CodeQL, pip-audit ni ishga tushirish
- Natijalarni `kod/natijalar/` ga yozish
- `hisobot.py` orqali qiyosiy jadvallarni hisoblash
- GitHub Actions workflow'ini sinash

### Claude Cowork (hujjat ishlari)
- `matn/` ichidagi boblarni yozish va tahrirlash
- `kod/natijalar/` dagi jadvallarni bobga ko'chirish
- Adabiyotlar ro'yxatini tartiblash
- Yakuniy `.docx` hujjatni yig'ish (`ilovalar/` ga)

**Ikkalasi ham shu bitta papkani ko'radi** — fayllarni qo'lda ko'chirish kerak emas.

---

## 5. Amaliy qism: sinaladigan vositalar

| Vosita | Turi | Rol |
|---|---|---|
| Bandit | AST asosida, Python-ga ixtisoslashgan | bazaviy daraja |
| Semgrep | qoida (pattern) asosida, ko'p tilli | o'rta daraja + custom qoida |
| CodeQL | semantik, taint analysis | chuqur daraja |
| pip-audit | SCA (bog'liqliklar) | SAST o'rnini to'ldiradi |

**Baholash metrikalari:** TP, FP, FN, Precision, Recall, F1, ishlash vaqti.
Ground truth — `kod/zaif-ilova/ZAIFLIKLAR.md` faylida.

---

## 6. Xavfsizlik ogohlantirishi

`kod/zaif-ilova/` ichidagi kod **ataylab zaif qilingan** va faqat statik
tahlil vositalarini sinash uchun mo'ljallangan.

- Internetga chiqariladigan serverga joylashtirilmaydi
- Faqat `127.0.0.1` da, izolyatsiya qilingan muhitda ishga tushiriladi
- Undagi hech bir namuna haqiqiy loyihaga ko'chirilmaydi

---

## 7. Ish tartibi

Har bir bosqich tugagach `HOLAT.md` yangilanadi.
Yangi bob yozishdan oldin `reja.md` dagi bet taqsimoti tekshiriladi.
