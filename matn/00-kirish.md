# KIRISH

### Mavzuning dolzarbligi

Zamonaviy dasturiy ta'minotning xavfsizligi tobora ko'proq ishlab
chiquvchining o'z kodidan tashqarida shakllanadi. Black Duck kompaniyasining
2026-yilgi hisoboti 17 ta sohadagi 947 ta kod bazasini tekshirib, ochiq
kodli komponentlar kod bazalarining 98 foizida uchrashini aniqladi; bir kod
bazasiga to'g'ri keladigan zaifliklarning o'rtacha soni esa bir yil ichida
107 foizga oshgan [26]. Bu o'sish tasodifiy emas: ilovalar tarkibidagi
begona kod hajmi ortgani sari uning xavfsizlik holatini qo'lda kuzatish
amalda imkonsiz bo'lib boradi.

Muammoning miqyosi tasniflash tizimlarining o'lchamidan ham ko'rinadi.
MITRE korporatsiyasining keng tarqalgan nuqsonlar ro'yxati 2026-yil oktabr
holatiga 944 ta nuqson turini o'z ichiga oladi [1], OWASP Top 10
ro'yxatining 2025-yilgi tahriri esa 2,8 milliondan ortiq ilova bo'yicha
to'plangan ma'lumotlarga va taxminan 220 000 ta CVE yozuviga tayanadi [3].
O'sha tahrirda ta'minot zanjiridagi nuqsonlar alohida toifa sifatida
ro'yxatga kirgani [3] bu yo'nalishning ustuvorligini ko'rsatadi.

Kodni har bir o'zgarishda avtomatik tekshirish shu sababli sanoat
amaliyotiga aylandi: Google kompaniyasining statik tahlil platformasi
kuniga 50 000 dan ortiq kod ko'rigi o'zgarishini tahlil qiladi [25]. Ayni
paytda bu avtomatlashtirishning o'z narxi bor — B. Johnson va
hammualliflarining tadqiqotida ishlab chiquvchilar vositalarning qiymatini
tan olgan holda, yolg'on ijobiy natijalarni va natijalarning taqdim etilish
usulini ulardan foydalanishga asosiy to'siq deb ko'rsatgan [24]. Statik
tahlilni joriy etish adabiyotda ko'pincha zaiflikni kech aniqlash narxining
keskin o'sishi haqidagi da'vo bilan asoslanadi; ushbu ishda bu da'vo dalil
sifatida ishlatilmaydi, chunki uning dalil bazasi zamonaviy empirik
tadqiqotlarda tasdiqlanmagan (1.4-band).

Alohida, hozirgacha deyarli o'rganilmagan jihat — xalqaro vositalarning
milliy tilda nomlangan kod bilan ishlashi. Mavjud etalon to'plamlar
butunlay ingliz tilidagi namunalardan tuzilgan, shu sababli bu savolni
ular ustida sinab ko'rish mumkin emas. Ushbu ishda masala alohida
tekshirildi va natija kutilmagan bo'lib chiqdi (3.3-band).

### Muammoning qo'yilishi

Statik kod tahlili vositalari bozorida o'nlab yechim mavjud va ularning
har biri o'z samaradorligini e'lon qiladi. Biroq amaliyotchi uchun asosiy
savollar odatda javobsiz qoladi: qaysi vosita qanday sinf zaifliklarni
haqiqatan topadi, nimani umuman ko'rmaydi, bu cheklov vositaning tahlil
usulidan kelib chiqadimi yoki shunchaki qoidalar to'plamining bo'shligimi,
va bir necha vositani birgalikda qo'llash qoplamani qanchalik oshiradi.
Vositalar hujjatlari bu savollarga javob bermaydi, chunki ular o'z
mahsulotini tavsiflaydi, uni raqobatchilar bilan bir xil sharoitda
solishtirmaydi.

Shundan kelib chiqib, muammo quyidagicha qo'yiladi: statik kod tahlili
vositalarining zaifliklarni aniqlash samaradorligini nazorat qilinadigan
sharoitda o'lchash, har bir o'tkazib yuborish va yolg'on ijobiy natijaning
sababini aniqlash hamda shu asosda vositalarni tanlash va joriy etish
bo'yicha asoslangan tavsiyalar shakllantirish zarur.

### Tadqiqot maqsadi

Ishning maqsadi — statik kod tahlili vositalarining Python ilovalaridagi
zaifliklarni aniqlash samaradorligini etalon to'plam asosida o'lchash,
ularning cheklovlari va o'zaro to'ldiruvchiligini aniqlash hamda shu asosda
vositalarni tanlash va xavfsiz ishlab chiqish jarayoniga joriy etish
bo'yicha asoslangan tavsiyalar ishlab chiqishdan iborat.

### Tadqiqot vazifalari

Maqsadga erishish uchun quyidagi vazifalar belgilandi:

1. Dasturiy ta'minot zaifliklarining tasnifi va baholash tizimlarini
   (CWE, OWASP Top 10, CVE/NVD, CVSS) o'rganish hamda zaifliklarni
   aniqlashning asosiy usullarini — statik, dinamik, interaktiv tahlil va
   bog'liqliklar tahlilini — qiyoslash (1.1, 1.2-bandlar).
2. Statik tahlilning xavfsiz ishlab chiqish hayotiy siklidagi va CI/CD
   quvuridagi o'rnini hamda uni qo'llashning iqtisodiy asoslarini aniqlash
   (1.3, 1.4-bandlar).
3. Statik tahlilning nazariy asoslarini — abstrakt sintaksis daraxti,
   boshqaruv va ma'lumotlar oqimi, zaharlangan ma'lumot tahlili — hamda
   samaradorlikni baholash metodologiyasini va usulning nazariy
   cheklovlarini o'rganish (2.1, 2.2, 2.4, 2.5-bandlar).
4. Mavjud statik tahlil vositalarini sharhlash va qiyosiy sinov uchun
   turli tahlil chuqurligiga ega vositalarni tanlash (2.3-band).
5. Oldindan ma'lum etalon to'plamga ega sinov obyektini ishlab chiqish,
   tanlangan vositalarni unda sinab aniqlik metrikalarini o'lchash hamda
   har bir o'tkazib yuborish va yolg'on ijobiy natijaning sababini
   aniqlash (3.1, 3.2, 3.3-bandlar).
6. Aniqlangan bo'shliqlarni to'ldiruvchi maxsus qoidalar ishlab chiqish va
   vositalarni CI/CD quvuriga integratsiya qilib, sifat darvozasining
   ishlashini sinash (3.4, 3.5-bandlar).

### Tadqiqot obyekti, predmeti va metodlari

**Tadqiqot obyekti** — dasturiy ta'minotni xavfsiz ishlab chiqish jarayoni
va undagi kod darajasidagi xavfsizlik nazoratlari. **Tadqiqot predmeti** —
statik kod tahlili vositalarining Python kodidagi zaifliklarni aniqlash
samaradorligi, ularning cheklovlari va uzluksiz integratsiya quvuriga
joriy etish usullari.

Ishda bir necha metod birgalikda qo'llanildi. **Manbalarni tahlil
qilish**: nazariy qism rasmiy standartlar (MITRE, OWASP, NIST, FIRST),
vositalarning rasmiy hujjatlari va retsenziyali ilmiy nashrlar asosida
tuzildi; har bir faktik da'vo manbaga havola bilan beriladi, manbasi
topilmagan raqam ishga umuman kiritilmadi. **Qiyosiy tahlil va
eksperiment**: aniqlash usullari hamda tanlangan vositalar yagona mezonlar
bo'yicha solishtirildi, nazorat qilinadigan sinov obyekti — oldindan qayd
etilgan zaifliklarga ega, ataylab zaif qilingan ilova — ishlab chiqildi va
barcha vositalar bir xil kod ustida, bir xil muhitda ishga tushirildi.
**Metrik baholash va topilmalarni qo'lda tasniflash**: natijalar etalon
to'plamga nisbatan normallashtirilib, Precision, Recall va F1
ko'rsatkichlari skript orqali hisoblandi va har bir bog'lanish jurnalda
qayd etildi; har bir yolg'on ijobiy natija va o'tkazib yuborilgan zaiflik
alohida tekshirilib, sababi aniqlandi — aynan shu bosqich metrikalar o'zi
bermaydigan xulosalarni berdi. **Joriy etishni sinash**: vositalar
amaldagi CI/CD quvuriga integratsiya qilinib, ochiq omborda ishga
tushirildi va natijalari lokal o'lchovlar bilan solishtirildi.

### Ishning tuzilishi

Ish kirish, uch bob, xulosa, foydalanilgan adabiyotlar ro'yxati va
ilovalardan iborat.

**Birinchi bobda** dasturiy xavfsizlik asoslari bayon etiladi: zaiflik,
ekspluatatsiya va xavf tushunchalari, CWE, OWASP Top 10, CVE/NVD va CVSS
tizimlari; aniqlashning to'rtta asosiy usuli qiyosiy jadval bilan; statik
tahlilning xavfsiz hayotiy sikldagi va CI/CD quvuridagi o'rni; hamda
usulni qo'llashning iqtisodiy asoslanishi.

**Ikkinchi bobda** vositalarning ishlash prinsipi ko'rib chiqiladi:
abstrakt sintaksis daraxti, boshqaruv oqimi grafi, ma'lumotlar oqimi va
zaharlangan ma'lumot tahlili; tahlil usullarining turlari; amaldagi
vositalarning sharhi; samaradorlikni baholash metodologiyasi va nazariy
cheklovlar.

**Uchinchi bob** amaliy qism: sinov obyekti va metodika, vositalarni ishga
tushirish natijalari, qiyosiy tahlil, loyihaga xos maxsus qoidalar ishlab
chiqish va CI/CD quvuriga integratsiya. **Xulosada** har bir vazifa
bo'yicha erishilgan natijalar jamlanadi va tavsiyalar beriladi. Ilovalarda
tasnif jadvallari, etalon to'plam va vositalar natijalarining to'liq
jadvallari keltiriladi.
