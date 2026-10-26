# II BOB. STATIK TAHLIL VOSITALARINING ISHLASH PRINSIPI

## 2.1. Statik tahlilning nazariy asoslari

Statik tahlil kodning matni ustida emas, uning tuzilmaviy modellari ustida
olib boriladi. Bu modellar kompilyatorlar nazariyasida ishlab chiqilgan va
xavfsizlik tahliliga o'zgarishsiz ko'chirilgan [27].

**Leksik va sintaktik tahlil.** Dastlab manba kod leksik tahlilchi
yordamida leksemalar (token) ketma-ketligiga ajratiladi, so'ngra sintaktik
tahlilchi uni tilning grammatikasi bo'yicha tekshiradi [27]. Shu bosqichdan
keyingina kod ustida har qanday mazmunli tahlil mumkin bo'ladi — shu
sababli kompilyatsiya qilinmaydigan yoki sintaktik xatoli kod ko'pchilik
vositalar uchun to'siq bo'lib qoladi (1.2-band).

**Abstrakt sintaksis daraxti (AST).** Sintaktik tahlil natijasi daraxt
ko'rinishida saqlanadi: har bir tugun til konstruksiyasiga
(o'zlashtirish, chaqiruv, shartli operator) mos keladi, bargi esa
o'zgaruvchi yoki literalga. AST da qavslar va bo'sh joy kabi matniy
tafsilotlar yo'q, shuning uchun bir xil ma'noli turli yozilishlar bir xil
daraxt beradi. Python uchun bu model standart `ast` modulida mavjud va
Bandit aynan shu daraxtni aylanib chiqib qoidalarni qo'llaydi [9].

**Boshqaruv oqimi grafi (CFG).** AST ifodalarning tuzilishini
ko'rsatadi, lekin bajarilish tartibini emas. CFG kodni bazaviy bloklarga
(shoxlanishsiz ketma-ket buyruqlar) ajratadi va ular orasidagi o'tish
imkoniyatlarini yoy sifatida belgilaydi [27]. Shu graf orqali "bu
operatorga qaysi yo'llar bilan kelish mumkin" degan savolga javob
beriladi.

**Ma'lumotlar oqimi tahlili.** CFG ustida qiymatlarning qanday
tarqalishi hisoblanadi. Tahlil iterativ ravishda, har bir tugun uchun
to'plamlarni yangilab, o'zgarish to'xtaguncha — fiksirlangan nuqtaga
(fixpoint) yetguncha — bajariladi [27]. Shu mexanizm "bu o'zgaruvchiga
qanday qiymatlar kelishi mumkin" savoliga javob beradi.

**Zaharlangan ma'lumot tahlili (taint analysis).** Xavfsizlik tahlilining
asosiy usuli ma'lumotlar oqimi tahlilining maxsus holatidir. Unda to'rtta
tushuncha ishlatiladi: **manba** (source) — tashqaridan nazorat
qilinadigan ma'lumot kiradigan nuqta; **tarqatuvchi** (propagator) —
zaharlangan qiymatni uzatadigan amal; **cho'kma** (sink) — zaharlangan
ma'lumot zarar keltiradigan joy; **tozalagich** (sanitizer) — zararni
bartaraf etuvchi amal. Agar manbadan cho'kmagacha tozalagichdan
o'tmaydigan yo'l topilsa, vosita zaiflik haqida xabar beradi. Bu
yondashuv Java ilovalaridagi zaifliklarni aniqlashda qo'llanib, to'qqizta
yirik ochiq kodli ilovada 29 ta zaiflikni topgan va shundan ikkitasi keng
ishlatiladigan kutubxonalarda joylashgan edi [29].

Tahlilning funksiya va modul chegaralaridan o'tishi (interprotsedurali
tahlil) alohida, ancha qimmat imkoniyatdir. Uning amaliy ahamiyati
3.3-bandda o'lchab ko'rsatilgan.

**Xulosa.** Statik tahlil kompilyator modellari — AST, boshqaruv oqimi
grafi va ma'lumotlar oqimi — ustiga qurilgan. Xavfsizlik nuqtai nazaridan
eng muhimi zaharlangan ma'lumot tahlili bo'lib, uning sifati manba,
cho'kma va tozalagich modellarining to'liqligiga, hamda tahlilning modul
chegarasidan o'ta olishiga bog'liq.

---

## 2.2. Tahlil usullarining turlari

**Shablon bo'yicha moslashtirish (pattern matching).** Eng sodda usul:
qoida kod namunasi sifatida yoziladi va AST da shunga mos tuzilma
qidiriladi. Semgrep ning asosiy rejimi shunday ishlaydi — qoida
tekshirilayotgan tilning o'zida, metao'zgaruvchilar bilan
ifodalanadi [10]. Usul tez va qoidasini yozish oson, lekin u kodning
ma'nosini emas, shaklini ko'radi.

**Semantik tahlil.** Bu yondashuvda kod avval ma'lumotlar bazasiga
aylantiriladi, so'ngra unga so'rovlar beriladi. CodeQL shu tamoyilga
asoslangan: kod relyatsion ma'lumotlar sifatida saqlanadi va qoidalar
maxsus so'rov tilida yoziladi [11]. Bazani qurish qimmat, lekin keyin
murakkab, modullararo oqimni talab qiladigan savollarni berish mumkin.

**Abstrakt interpretatsiya.** Nazariy jihatdan eng mustahkam yondashuv
P. Cousot va R. Cousot tomonidan 1977-yilda bayon etilgan: dasturning
konkret semantikasi hisoblash mumkin bo'lgan abstrakt domenga ko'chiriladi
va natija shu domenda yaxlitlanadi [28]. Yaxlitlash atayin "ehtiyotkor"
tomonga qilinadi: vosita mavjud bo'lishi mumkin bo'lgan holatlarni
ortiqcha qamrab oladi. Shu sababli bu usul zaiflikni o'tkazib
yubormaslikka intiladi, lekin buning evaziga mavjud bo'lmagan zaiflik
haqida xabar berishi mumkin — ya'ni **yolg'on ijobiy natijalar bu
yondashuvning nazariy oqibati**, tasodifiy nuqson emas.

**Aniqlik va ishlash tezligi o'rtasidagi muvozanat.** Amalda har bir
vosita ikki xatodan birini tanlashga majbur: zaiflikni o'tkazib yuborish
yoki ortiqcha ogohlantirish berish. Shablon asosidagi tahlil tez ishlaydi
va aniq yozilgan qoidada kam xato beradi, lekin qoidaga tushmagan
ko'rinishni butunlay ko'rmaydi. Semantik tahlil kengroq qamrovga ega,
lekin hisoblash narxi yuqori va modeli murakkab.

**Xulosa.** Uch yondashuv bir o'qda joylashgan: shakl, ma'no va rasmiy
yaxlitlash. Chuqurlik oshgani sari qamrov kengayadi, lekin hisoblash narxi
va modelning murakkabligi ham ortadi. Ushbu ishda shablon asosidagi va
semantik tahlil amalda qiyoslanadi (3.3-band).

---

## 2.3. Statik tahlil vositalarining sharhi

Sinov uchun tanlangan va qiyoslash uchun ahamiyatli vositalar
2.1-jadvalda jamlangan.

**2.1-jadval. Statik tahlil vositalarining qiyosiy tavsifi**

| Vosita | Tahlil usuli | Tillar | Qoidani kengaytirish | Chiqish formati |
|---|---|---|---|---|
| Bandit [9] | AST bo'yicha qoidalar | faqat Python | plagin sifatida | matn, JSON, SARIF |
| Semgrep [10] | shablon + taint rejimi | ko'p tilli | YAML qoida | matn, JSON, SARIF |
| CodeQL [11] | semantik, so'rov tili | ko'p tilli | QL so'rovi | SARIF |
| SonarQube [13] | sifat va xavfsizlik platformasi | ko'p tilli | maxsus qoidalar | platforma ichida |
| pip-audit [12] | bog'liqliklar tahlili (SCA) | Python paketlari | — | matn, JSON |

Bandit Python ekotizimining o'z vositasi bo'lib, tilga ixtisoslashgani
uchun sozlashsiz ham ishlaydi [9]. Semgrep qoida formatining soddaligi
bilan ajralib turadi: qoida tekshirilayotgan tilning sintaksisida
yoziladi, shuning uchun loyihaga xos qoida yozish arzon [10] — bu
imkoniyat 3.4-bandda qo'llanilgan. CodeQL kodni so'rovlanadigan
ma'lumotlar bazasiga aylantiradi va shu hisobdan modullararo oqimni
kuzata oladi [11]. SonarQube alohida platforma sifatida ishlaydi va
xavfsizlik topilmalarini kod sifati ko'rsatkichlari bilan birga
taqdim etadi [13]. pip-audit statik tahlil vositasi emas: u kodni
tekshirmaydi, bog'liqliklar ro'yxatini ma'lum zaifliklar bazalariga
solishtiradi [12].

Bu ro'yxat to'liq emas. OWASP ning manba kodini tahlil qilish
vositalari sharhida ochiq va tijorat yechimlari, jumladan Checkmarx,
Coverity va Fortify, keltirilgan [4]. Tijorat vositalari ushbu ishda
sinalmadi: ular litsenziya talab qiladi va natijalarini mustaqil
tekshirish imkoni cheklangan.

**Xulosa.** Tanlangan to'rtta vosita tahlil chuqurligi bo'yicha to'rtta
turli darajani qoplaydi: AST qoidalari, shablon moslashtirish, semantik
so'rovlar va bog'liqliklar tahlili. Shu tanlov bir xil kod ustida turli
usullarni qiyoslash imkonini beradi.

---

## 2.4. Samaradorlikni baholash metodologiyasi

**Asosiy tushunchalar.** Vositaning har bir xabari to'rtta toifadan
biriga tushadi: **TP** (true positive) — haqiqiy zaiflik to'g'ri
aniqlangan; **FP** (false positive) — zaiflik bo'lmagan joyga
ogohlantirish berilgan; **FN** (false negative) — mavjud zaiflik
o'tkazib yuborilgan; **TN** (true negative) — zaiflik yo'q va xabar ham
berilmagan. Statik tahlilda TN ni sanash amalda ma'nosiz, chunki
"zaiflik bo'lmagan joylar" soni cheklanmagan.

**Metrikalar.** Shu toifalardan uchta ko'rsatkich hisoblanadi:

```
Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
F1        = 2 * (Precision * Recall) / (Precision + Recall)
```

Precision — vosita xabarlarining qanchasi haqiqiy ekanini, Recall —
mavjud zaifliklarning qanchasi topilganini ko'rsatadi. F1 ikkisining
garmonik o'rtachasi bo'lib, bitta ko'rsatkich bilan solishtirish
imkonini beradi. Ikkala ko'rsatkichni birga qarash zarur: faqat bitta
tor qoida yozib Precision ni 1,00 ga yetkazish oson, lekin bunda Recall
juda past bo'ladi (3.3-band shu holatni ko'rsatadi).

**Ogohlantirishlardan charchash (alert fatigue).** Metrikalarning
amaliy ma'nosi muhandis xulqida namoyon bo'ladi. Yolg'on ijobiy
natijalar va natijalarning taqdim etilish usuli ishlab chiquvchilar
uchun vositadan foydalanishga asosiy to'siq bo'lib qolmoqda [24]. Yirik
ishlab chiqish muhitlarida shu sababli miqdoriy chegara qo'llanadi:
yangi tekshiruv platformaga qo'shilishi uchun uning samarali yolg'on
ijobiy natijalar ulushi 10 foizdan kam bo'lishi talab qilinadi [25].

**Etalon to'plamlar.** Vositalarni solishtirish uchun oldindan ma'lum
zaifliklarga ega to'plamlar ishlatiladi. OWASP Benchmark — Java va
Python uchun sinov to'plami bo'lib, aniqlash vositalarining tezligi va
aniqligini tekshirishga mo'ljallangan; uning joriy versiyasi — v1.2 [31].
NIST ning SARD ma'lumotlar bazasidagi Juliet to'plamlari ancha
kattaroq: Juliet C/C++ 1.3 da 64 099, Juliet Java 1.3 da 28 881,
Juliet C# 1.3 da 28 942 sinov holati mavjud [32]. Vositalarni baholash
metodologiyasi NIST ning SAMATE loyihasi doirasida ishlab
chiqilmoqda [6].

Shu bilan birga, Juliet to'plamlari Python tilini qamrab olmaydi [32],
OWASP Benchmark esa o'zbek tilida nomlangan identifikatorlarga ega
namunalarni o'z ichiga olmaydi. Ushbu ishning savoli aynan shu
bo'shliqda joylashgani uchun sinov obyekti mustaqil ishlab chiqildi
(3.1-band).

**Xulosa.** Samaradorlik Precision, Recall va F1 ko'rsatkichlari bilan
o'lchanadi, lekin ularning amaliy ma'nosi muhandis vaqtida — yolg'on
ijobiy natijalarni ko'rib chiqishga ketgan mehnatda — namoyon bo'ladi.
Mavjud etalon to'plamlar ushbu ishning savoliga mos kelmagani uchun o'z
etalon to'plami tuzildi.

---

## 2.5. Statik tahlilning nazariy cheklovlari

Statik tahlilning cheklovlari qisman amaliy, qisman esa printsipial
xarakterga ega.

**Aniqlanmaslik.** Dasturning to'xtashini umumiy holda aniqlab
bo'lmaydi, Rays teoremasi esa bu natijani umumlashtiradi: dastur
hisoblaydigan funksiyaning har qanday notrivial xossasi algoritmik
ravishda aniqlanmaydi [30]. "Bu kodda SQL inyeksiyasi bormi" degan savol
aynan shunday xossaga tegishli. Demak hech bir vosita bir vaqtning
o'zida ham to'liq (barcha zaifliklarni topadigan), ham aniq (yolg'on
ogohlantirish bermaydigan) bo'la olmaydi. Vosita ishlab chiquvchisi
ikkisidan birini tanlaydi — bu muhandislik qarori, nuqson emas.

**Dinamik kod.** `eval`, `exec` va refleksiya orqali bajariladigan kod
tahlil paytida mavjud emas, shuning uchun uning ichidagi mantiq
umuman tekshirilmaydi. Vosita faqat bunday chaqiruvning o'zini xavfli
deb belgilashi mumkin; ushbu ishning sinov obyektida shunday zaiflik
bor (3.1-band, Z-07).

**Konfiguratsiya va ish muhiti.** Zaifliklarning bir qismi kodda umuman
aks etmaydi: server sozlamalari, kirish huquqlari, muhit
o'zgaruvchilari. OWASP bu cheklovni statik tahlilning rasmiy zaif
tomoni sifatida qayd etadi (1.2-band).

**Kutubxona modelining to'liqmasligi.** Vosita tashqi kutubxonalarning
xulqini o'z modeliga tayanib baholaydi. Model kutubxonaning aniq
chaqiruvini qamrab olmasa, to'g'ri yozilgan qoida ham jim qoladi.
Ushbu ishda bunday holat amalda qayd etilgan (3.3-band).

**Xulosa.** Statik tahlilning asosiy cheklovi texnologiyaning
yetukligida emas, hisoblash nazariyasida: notrivial semantik xossalar
aniqlanmaydi, shuning uchun har bir vosita yoki o'tkazib yuborish, yoki
ortiqcha ogohlantirish tomon og'adi. Qolgan cheklovlar — dinamik kod,
konfiguratsiya va kutubxona modellari — bu nazariy chegarani amalda
yanada torroq qiladi va statik tahlilni boshqa nazoratlar bilan
birgalikda qo'llash zaruratini tug'diradi.
