# XULOSA

Ishda statik kod tahlili vositalarining dasturiy xavfsizlikni ta'minlashdagi
o'rni nazariy jihatdan ko'rib chiqildi va nazorat qilinadigan sharoitda
amaliy sinovdan o'tkazildi.

### Vazifalar bo'yicha erishilgan natijalar

**Birinchi vazifa.** Nuqson, zaiflik va xavf tushunchalari ajratildi va
baholash tizimlarining vazifa taqsimoti aniqlandi: CWE nuqson turini, CVE
aniq mahsulotdagi aniq zaiflikni, CVSS uning jiddiyligini, OWASP Top 10 esa
xavf toifasini ifodalaydi. Vositalarni qiyoslash uchun yagona asos sifatida
CWE tanlandi, chunki faqat shu tasnif kod darajasidagi topilmalarga bevosita
bog'lanadi. Aniqlashning to'rtta usuli qiyosiy jadvalda solishtirilib,
ularning "nimani topolmaydi" xossalari bir-birini qoplamasligi ko'rsatildi.

**Ikkinchi vazifa.** Statik tahlil xavfsiz hayotiy siklda alohida amaliyot
sifatida ajratiladi va "chapga surish" tamoyili bo'yicha quvurning eng
boshiga joylashtiriladi. Usulning iqtisodiy asoslanishi qayta ko'rib
chiqildi: adabiyotda keng tarqalgan "kech tuzatish bir necha o'n barobar
qimmat" turidagi da'vo zamonaviy empirik tadqiqotlarda tasdiqlanmagani
uchun dalil sifatida ishlatilmadi. Uning o'rniga tekshiriladigan uch asos
ko'rsatildi: avtomatik tekshiruvning deyarli bepul takrorlanishi,
qamrovning bir xilligi va muhandis vaqtining avtomatika yetmaydigan
masalalarga bo'shatilishi.

**Uchinchi vazifa.** Tahlil chuqurligining ierarxiyasi aniqlandi — shablon
bo'yicha moslashtirishdan abstrakt sintaksis daraxti va ma'lumotlar oqimi
orqali modullararo zaharlangan ma'lumot tahliligacha — hamda samaradorlikni
baholash metodologiyasi belgilandi. Ierarxiyaning amaliy ahamiyati uchinchi
bobda tasdiqlandi, shu bilan birga uning chegarasi ham ko'rindi: chuqurlik
bo'yicha ustunlik faqat ikkita holatda ro'y berdi, qolgan hamma joyda
usullar orasidagi farq sezilmadi.

**To'rtinchi vazifa.** Sinov uchun turli chuqurlikdagi to'rtta vosita
tanlandi: Bandit — abstrakt sintaksis daraxti asosidagi bazaviy daraja;
Semgrep — qoida asosidagi o'rta daraja; CodeQL — semantik, zaharlangan
ma'lumot oqimini kuzatuvchi chuqur daraja; pip-audit — statik tahlil umuman
ko'rmaydigan sohani qoplovchi bog'liqliklar tahlili.

**Beshinchi vazifa.** 293 qatorli, uch modulli sinov ilovasi ishlab
chiqildi; unga 15 xil CWE toifasiga tegishli 24 ta zaiflik kiritilib, har
birining manzili oldindan qayd etildi. Vositalar bir xil muhitda ishga
tushirilib, metrikalar o'lchandi: Bandit 19 ta zaiflikni topdi (F1 = 0,83),
Semgrep ning rasmiy qoidalari 15 tasini (0,75), CodeQL 14 tasini (0,70),
maxsus qoidalar 5 tasini (0,34); pip-audit oltita paketda 43 ta noyob
zaiflikni aniqladi.

Har bir o'tkazib yuborishning sababi aniqlanib, uch toifaga ajratildi:
qoidaning yo'qligi, tahlil usulining cheklovi, hamda qoida mavjud bo'lsa-da
ishga tushmagan holatlar. Natija kutilganidan farq qildi: o'tkazib
yuborishlarning aksariyati texnologiya cheklovi emas, qoidalar to'plamining
bo'shligi bo'lib chiqdi — chinakam texnik sabab faqat ikkita holatda,
ma'lumot manbasi va cho'kmasi turli modullarda joylashganida qayd etildi.
Oltita yolg'on ijobiy natija ham tasniflandi: bir qismida oqim umuman
tahlil qilinmaydi, qolganida oqim to'g'ri kuzatiladi, lekin cho'kmaning
konteksti baholanmaydi.

**Oltinchi vazifa.** Beshta maxsus qoida ishlab chiqildi; to'rttasi ishladi
va yolg'on ijobiy natija bermadi, beshinchisi esa mantiqi to'g'ri
bo'lishiga qaramay natija bermadi, chunki ishlatilgan vosita modullararo
oqimni kuzatmaydi. Maxsus qoidalar uchta zaiflikni aniqladiki, ularni
sinovdagi uchta xalqaro vosita birgalikda ham topmagan edi. Vositalar
amaldagi CI/CD quvuriga integratsiya qilindi: natijalar yagona formatda
jamlandi, ikkita sifat darvozasi kutilganidek qurilishni to'xtatdi, CI dagi
ogohlantirishlar soni esa lokal natijalarga to'liq mos keldi — bu amaliy
qismning takrorlanuvchanligini tasdiqlaydi.

### Vositalarni tanlash bo'yicha amaliy tavsiyalar

**Bazaviy daraja — tilga ixtisoslashgan tez vosita**, har bir o'zgarishda
ishlatiladi: Bandit sinovda soniyalar ichida tugadi va eng yuqori qoplamani
berdi. Shu bilan birga uning yuqori ko'rsatkichi sinov korpusi tarkibining
ta'siri bo'lib, umumiy ustunlik dalili emas.

**Chuqur tahlil — modullararo oqim uchun.** CodeQL umumiy qoplama bo'yicha
oldinda emas, lekin boshqa hech bir vosita ko'rmagan zaiflikni topdi.
Semantik tahlil shunday holatlar uchun muqobilsiz, shuning uchun u pull
request yoki muntazam to'liq skanerlash bosqichida qo'llanadi.

**Bog'liqliklar tahlili — almashtirilmaydigan alohida nazorat.** Statik
tahlil vositalari bog'liqliklardagi zaifliklarning birortasini ham topmadi
va topishi ham mumkin emas edi, chunki zaif kod loyihaning o'zida emas.

**Maxsus qoidalar — milliy tildagi kod bazalari uchun zarurat.** Xalqaro
vositalarning nomga tayanadigan qoidalari o'zbekcha nomlangan
identifikatorlarni o'tkazib yubordi, ishlab chiquvchi esa buni sezmaydi:
vosita xato bermaydi, shunchaki jim qoladi.

**Qo'shimcha vositani asoslash.** Yangi vosita to'plamga faqat boshqalar
ko'rmaydigan sinf zaifliklarni topsagina qo'shilishi kerak; sinovda bu
shart bir vosita uchun bajarilmadi. **Sifat darvozasi** chegarasi esa
yolg'on ijobiy natijalar tushmaydigan qilib tanlanadi — sinovda qurilish
faqat jiddiy topilma uchun to'xtadi.

### Statik tahlilni boshqa usullar bilan birgalikda qo'llash zarurati

Ishning asosiy amaliy dalili vositalarni birgalikda qo'llash tahlilidan
kelib chiqadi: hech bir vosita yolg'iz 24 ta zaiflikdan 19 tasidan ko'pini
topmadi, uchtasi birgalikda esa to'liq qoplama berdi. Ya'ni eng yaxshi
yakka vosita ham etalon to'plamning beshdan bir qismini ko'rmay qoldi.

Bu birinchi bobdagi nazariy qoidani tasdiqlaydi: aniqlash usullari
raqobatchi emas, to'ldiruvchi. Statik tahlil konfiguratsiyani ko'rmaydi,
dinamik tahlil zaiflikning kod ichidagi manzilini bermaydi, interaktiv
tahlil sinalmagan kodni tekshirmaydi, bog'liqliklar tahlili esa loyihaning
o'z kodiga qaramaydi. Ishda sinalgan vositalar bu spektrning faqat ikki
uchini qoplaydi, demak to'liq qoplama uchun dinamik va interaktiv
nazoratlar ham talab qilinadi.

Shu bilan birga, ko'proq vosita qo'shish o'z-o'zidan yechim emas: sinovda
to'rtinchi vosita qoplamaga hech narsa qo'shmagani holda ko'rib chiqilishi
kerak bo'lgan xabarlar sonini sezilarli oshirdi. Vositalar soni bo'yicha
emas, qoplanmagan zaiflik sinflari bo'yicha tanlanishi kerak.

### Keyingi tadqiqot yo'nalishlari

**Til bog'liqligi bo'yicha nazorat tajribasi.** Uchinchi bobda semantik
tahlil vositasining ikki o'tkazib yuborishi uchun til to'sig'i gipotezasi
qo'yildi, lekin tasdiqlanmadi; uni tekshirish uchun o'zgaruvchilarni ingliz
tiliga qayta nomlab tahlilni takrorlash yetarli.

**Kattaroq va muvozanatli etalon to'plam.** Sinov korpusi kichik va tarkibi
shablon bilan ifodalanadigan zaifliklar tomon og'gan, bu esa metrikalarga
bevosita ta'sir qildi. Zaiflik sinflari bo'yicha muvozanatli korpus
vositalarni adolatliroq solishtirish imkonini beradi va ayni paytda
tezlik hamda miqyoslanuvchanlikni o'lchash savolini ham hal qiladi — bu
korpusda kesh isiganidan keyin to'rtala vosita ham soniyalar ichida tugadi.

**Dinamik va interaktiv nazoratlarni qo'shish.** To'ldiruvchilik gipotezasi
faqat statik tahlil doirasida sinaldi; uni to'liq tekshirish uchun ayni bir
sinov obyektida boshqa usullarni ham ishga tushirish kerak. Shu qatorda
bog'liqliklar tahlilida aniqlangan zaifliklarning qanchasi amalda
chaqiriladigan kodga tegishli ekani ham tekshirilishi lozim.

**Milliy tilga moslashtirilgan ochiq qoidalar to'plami.** Ishda ishlab
chiqilgan qoidalar bitta loyiha ehtiyojidan kelib chiqqan; ularni o'zbek
tilidagi dasturlash amaliyotida uchraydigan nomlar va naqshlar bo'yicha
to'liq to'plamga keltirish mustaqil amaliy qiymatga ega bo'lardi.
