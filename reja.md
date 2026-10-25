# Kurs ishi rejasi

**Mavzu:** Statik kod tahlili vositalarining dasturiy xavfsizlikni ta'minlashdagi o'rni
**Umumiy hajm:** 38–42 bet (ilovalarsiz)

---

## KIRISH — 3 bet

- Mavzuning dolzarbligi: zaifliklarni kech aniqlashning oqibatlari va narxi
- Muammoning qo'yilishi
- Ish maqsadi
- Ish vazifalari (5–6 ta, boblarga mos)
- Tadqiqot obyekti va predmeti
- Tadqiqot metodlari
- Ishning tuzilishi

---

## I BOB. DASTURIY XAVFSIZLIK VA KODNI TAHLIL QILISH ASOSLARI — 11 bet

**1.1. Dasturiy ta'minot zaifliklari va ularning tasnifi** *(3 bet)*
- Zaiflik, ekspluatatsiya, xavf tushunchalari
- CWE tasnifi va uning tuzilishi
- OWASP Top 10 — asosiy toifalar
- CVE/NVD ekotizimi va CVSS baholash tizimi

**1.2. Zaifliklarni aniqlash usullari** *(3 bet)*
- Statik tahlil (SAST) — mohiyati va qamrovi
- Dinamik tahlil (DAST)
- Interaktiv tahlil (IAST)
- Bog'liqliklar tahlili (SCA)
- Qiyosiy jadval: nima topadi, nimani topolmaydi, qachon qo'llanadi

**1.3. Xavfsiz ishlab chiqish hayotiy sikli va DevSecOps** *(3 bet)*
- SSDLC bosqichlari
- "Shift-left" tamoyili
- Statik tahlilning CI/CD quvuridagi o'rni
- Quality gate tushunchasi

**1.4. Statik tahlilni qo'llashning iqtisodiy asoslanishi** *(2 bet)*
- Zaiflikni tuzatish narxining bosqichlar bo'yicha o'sishi
- Avtomatlashtirish va qo'lda kod tekshirish nisbati

---

## II BOB. STATIK TAHLIL VOSITALARINING ISHLASH PRINSIPI — 13 bet

**2.1. Statik tahlilning nazariy asoslari** *(4 bet)*
- Leksik va sintaktik tahlil
- Abstrakt sintaksis daraxti (AST)
- Boshqaruv oqimi grafi (CFG)
- Ma'lumotlar oqimi tahlili (data-flow analysis)
- Zaharlangan ma'lumot tahlili (taint analysis): source → propagator → sink → sanitizer

**2.2. Tahlil usullarining turlari** *(2 bet)*
- Shablon bo'yicha moslashtirish (pattern matching)
- Semantik tahlil
- Abstrakt interpretatsiya va rasmiy usullar
- Aniqlik va ishlash tezligi o'rtasidagi muvozanat

**2.3. Statik tahlil vositalarining sharhi** *(4 bet)*
- Bandit — Python uchun AST asosidagi vosita
- Semgrep — qoida asosidagi ko'p tilli vosita
- CodeQL — kodni ma'lumotlar bazasi sifatida so'rovlash
- SonarQube — sifat va xavfsizlik platformasi
- pip-audit, Safety — bog'liqliklar tahlili
- Tijorat yechimlari: Checkmarx, Coverity, Fortify (qisqacha)
- Umumlashtiruvchi qiyosiy jadval

**2.4. Samaradorlikni baholash metodologiyasi** *(2 bet)*
- TP, FP, TN, FN tushunchalari
- Precision, Recall, F1-o'lchov formulalari
- Yolg'on ijobiy natijalar charchoqligi (alert fatigue)
- Etalon to'plamlar: OWASP Benchmark, Juliet Test Suite

**2.5. Statik tahlilning nazariy cheklovlari** *(1 bet)*
- To'xtash muammosi va Rays teoremasi
- Dinamik kod: `eval`, `exec`, refleksiya
- Konfiguratsiya va ish muhitiga bog'liq zaifliklar

---

## III BOB. AMALIY QISM: VOSITALARNI QIYOSIY SINASH — 14 bet

**3.1. Sinov obyekti va metodika** *(3 bet)*
- Sinov ilovasining tavsifi (Flask, modullar tuzilmasi)
- Kiritilgan zaifliklar ro'yxati va CWE bo'yicha taqsimoti
- Ground truth jadvali (qaysi fayl, qaysi qator, qaysi CWE)
- Sinov muhiti: OS, Python versiyasi, vositalar versiyalari
- Baholash mezonlari

**3.2. Vositalarni ishga tushirish va natijalar** *(4 bet)*
- Bandit: konfiguratsiya, buyruq, chiqish, tahlil
- Semgrep: ishlatilgan qoidalar to'plami, chiqish, tahlil
- CodeQL: ma'lumotlar bazasini yaratish, so'rov, chiqish, tahlil
- pip-audit: bog'liqliklardagi aniqlangan CVE lar

**3.3. Natijalarni qiyosiy tahlil qilish** *(3 bet)*
- CWE bo'yicha normallashtirilgan umumiy jadval
- Metrikalar jadvali (Precision, Recall, F1, vaqt)
- Diagramma: har bir vosita topgan zaifliklar ulushi
- Yolg'on ijobiy natijalar tahlili — tipik sabablar
- O'tkazib yuborilgan zaifliklar tahlili — nima uchun topilmadi

**3.4. Maxsus qoida ishlab chiqish** *(2 bet)*
- Loyihaga xos zaiflik namunasi
- Semgrep qoidasining tuzilishi va yozilishi
- Sinov natijasi

**3.5. CI/CD ga integratsiya** *(2 bet)*
- GitHub Actions workflow tuzilmasi
- SARIF formati va natijalarni birlashtirish
- Quality gate sozlash: qaysi darajadagi topilma qurilishni to'xtatadi
- Ishlab chiqarish jarayoniga joriy etish bo'yicha tavsiyalar

---

## XULOSA — 2 bet

- Vazifalar bo'yicha erishilgan natijalar
- Vositalarni tanlash bo'yicha amaliy tavsiyalar
- Statik tahlilni boshqa usullar bilan birgalikda qo'llash zarurati
- Keyingi tadqiqot yo'nalishlari

---

## FOYDALANILGAN ADABIYOTLAR — 2 bet

20–25 manba. Tarkibi:
- Rasmiy hujjatlar va standartlar (NIST, OWASP, MITRE)
- Ilmiy maqolalar (IEEE, ACM)
- Vositalarning rasmiy hujjatlari
- O'zbekiston me'yoriy hujjatlari (agar mavjud bo'lsa)

---

## ILOVALAR — hajmga kirmaydi

- A ilovasi. Sinov ilovasining to'liq kodi
- B ilovasi. Vositalarning to'liq hisobotlari
- C ilovasi. Semgrep maxsus qoidasi
- D ilovasi. GitHub Actions workflow fayli
- E ilovasi. Skrinshotlar
