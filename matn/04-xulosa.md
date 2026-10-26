# XULOSA

Ishda statik kod tahlili vositalarining dasturiy xavfsizlikni ta'minlashdagi
o'rni nazariy jihatdan ko'rib chiqildi va nazorat qilinadigan sharoitda
amaliy sinovdan o'tkazildi.

### Vazifalar bo'yicha erishilgan natijalar

**Birinchi va ikkinchi vazifalar.** Nuqson, zaiflik va xavf tushunchalari
ajratildi va baholash tizimlarining vazifa taqsimoti aniqlandi: CWE nuqson
turini, CVE aniq mahsulotdagi aniq zaiflikni, CVSS uning jiddiyligini,
OWASP Top 10 esa xavf toifasini ifodalaydi. Vositalarni qiyoslash uchun
yagona asos sifatida CWE tanlandi, chunki faqat shu tasnif kod darajasidagi
topilmalarga bevosita bog'lanadi. Aniqlashning to'rtta usuli qiyosiy
jadvalda solishtirilib, ularning "nimani topolmaydi" xossalari bir-birini
qoplamasligi ko'rsatildi. Statik tahlil xavfsiz hayotiy siklda alohida
amaliyot sifatida ajratiladi va "chapga surish" tamoyili bo'yicha quvurning
eng boshiga joylashtiriladi. Usulning iqtisodiy asoslanishi qayta ko'rib
chiqildi: adabiyotda keng tarqalgan "kech tuzatish bir necha o'n barobar
qimmat" turidagi da'vo zamonaviy empirik tadqiqotlarda tasdiqlanmagani
uchun dalil sifatida ishlatilmadi; uning o'rniga uch tekshiriladigan asos
ko'rsatildi — avtomatik tekshiruvning deyarli bepul takrorlanishi,
qamrovning bir xilligi va muhandis vaqtining bo'shatilishi.

**Uchinchi va to'rtinchi vazifalar.** Tahlil chuqurligining ierarxiyasi
aniqlandi — shablon moslashtirishdan AST va ma'lumotlar oqimi orqali
modullararo zaharlangan ma'lumot tahliligacha — hamda baholash
metodologiyasi belgilandi. Shu asosda turli chuqurlikdagi to'rtta vosita
tanlandi: Bandit (AST qoidalari), Semgrep (shablon va taint), CodeQL
(semantik so'rovlar) va pip-audit (bog'liqliklar tahlili). Ierarxiyaning
chegarasi ham ko'rindi: chuqurlik bo'yicha ustunlik faqat ikkita holatda
ro'y berdi.

**Beshinchi vazifa.** 293 qatorli, uch modulli sinov ilovasi ishlab
chiqildi; unga 15 xil CWE toifasiga tegishli 24 ta zaiflik kiritilib, har
birining manzili oldindan qayd etildi. Metrikalar o'lchandi: Bandit 19 ta
zaiflikni topdi (F1 = 0,83), Semgrep ning rasmiy qoidalari 15 tasini
(0,75), CodeQL 14 tasini (0,70), maxsus qoidalar 5 tasini (0,34);
pip-audit oltita paketda 43 ta noyob zaiflikni aniqladi. Har bir o'tkazib
yuborishning sababi aniqlanib, uch toifaga ajratildi: qoidaning yo'qligi,
tahlil usulining cheklovi, hamda qoida mavjud bo'lsa-da ishga tushmagan
holatlar. Natija kutilganidan farq qildi: aksariyati texnologiya cheklovi
emas, qoidalar to'plamining bo'shligi bo'lib chiqdi — chinakam texnik
sabab faqat ikkita holatda qayd etildi. Oltita yolg'on ijobiy natija ham
ikki toifaga tasniflandi.

**Oltinchi vazifa.** Beshta maxsus qoidadan to'rttasi ishladi va yolg'on
ijobiy natija bermadi; beshinchisi mantiqi to'g'ri bo'lishiga qaramay
natija bermadi, chunki ishlatilgan vosita modullararo oqimni kuzatmaydi.
Maxsus qoidalar uchta zaiflikni aniqladiki, ularni sinovdagi uchta
xalqaro vosita birgalikda ham topmagan edi. Vositalar CI/CD quvuriga
integratsiya qilindi: ikkita sifat darvozasi kutilganidek qurilishni
to'xtatdi, CI dagi ogohlantirishlar soni esa lokal natijalarga to'liq mos
keldi.

### Vositalarni tanlash bo'yicha amaliy tavsiyalar

**Bazaviy daraja — tilga ixtisoslashgan tez vosita**, har bir o'zgarishda
ishlatiladi: Bandit sinovda soniyalar ichida tugadi va eng yuqori qoplamani
berdi, lekin uning yuqori ko'rsatkichi sinov korpusi tarkibining ta'siri
bo'lib, umumiy ustunlik dalili emas. **Chuqur tahlil** modullararo oqim
uchun kerak: CodeQL umumiy qoplama bo'yicha oldinda emas, lekin boshqa hech
bir vosita ko'rmagan zaiflikni topdi, shuning uchun u pull request yoki
muntazam to'liq skanerlash bosqichida qo'llanadi. **Bog'liqliklar tahlili**
esa almashtirilmaydigan alohida nazorat: statik tahlil vositalari
bog'liqliklardagi zaifliklarning birortasini ham topmadi va topishi mumkin
ham emas edi.

**Maxsus qoidalar — milliy tildagi kod bazalari uchun zarurat.** Xalqaro
vositalarning nomga tayanadigan qoidalari o'zbekcha nomlangan
identifikatorlarni o'tkazib yubordi, ishlab chiquvchi esa buni sezmaydi:
vosita xato bermaydi, shunchaki jim qoladi. **Yangi vosita** to'plamga
faqat boshqalar ko'rmaydigan sinf zaifliklarni topsagina qo'shilishi
kerak, **sifat darvozasi** chegarasi esa yolg'on ijobiy natijalar
tushmaydigan qilib tanlanadi.

**Boshqa usullar bilan birgalikda qo'llash zarurati.** Ishning asosiy
amaliy dalili vositalarni birgalikda qo'llash tahlilidan kelib chiqadi:
hech bir vosita yolg'iz 24 ta zaiflikdan 19 tasidan ko'pini topmadi,
uchtasi birgalikda esa to'liq qoplama berdi — eng yaxshi yakka vosita ham
etalon to'plamning beshdan bir qismini ko'rmay qoldi. Bu birinchi bobdagi
nazariy qoidani tasdiqlaydi: aniqlash usullari raqobatchi emas,
to'ldiruvchi. Statik tahlil konfiguratsiyani ko'rmaydi, dinamik tahlil kod
ichidagi manzilni bermaydi, interaktiv tahlil sinalmagan kodni
tekshirmaydi, bog'liqliklar tahlili esa loyihaning o'z kodiga qaramaydi.
Ishda sinalgan vositalar bu spektrning faqat ikki uchini qoplaydi, demak
to'liq qoplama uchun dinamik va interaktiv nazoratlar ham talab qilinadi.
Shu bilan birga, ko'proq vosita qo'shish o'z-o'zidan yechim emas: sinovda
to'rtinchi vosita qoplamaga hech narsa qo'shmagani holda ko'rib chiqilishi
kerak bo'lgan xabarlar sonini sezilarli oshirdi — vositalar soni bo'yicha
emas, qoplanmagan zaiflik sinflari bo'yicha tanlanishi kerak.

### Keyingi tadqiqot yo'nalishlari

Ishning ochiq qolgan masalalari to'rtta yo'nalish beradi. **Til
bog'liqligi bo'yicha nazorat tajribasi**: uchinchi bobda semantik tahlil
vositasining ikki o'tkazib yuborishi uchun til to'sig'i gipotezasi
qo'yildi, lekin tasdiqlanmadi — uni tekshirish uchun o'zgaruvchilarni
ingliz tiliga qayta nomlab tahlilni takrorlash yetarli. **Kattaroq va
muvozanatli etalon to'plam**: sinov korpusi kichik va tarkibi shablon
bilan ifodalanadigan zaifliklar tomon og'gan, bu metrikalarga bevosita
ta'sir qildi; kattaroq korpus vositalarni adolatliroq solishtirish va
tezlikni o'lchash imkonini beradi. **Dinamik va interaktiv nazoratlarni
qo'shish**: to'ldiruvchilik gipotezasi faqat statik tahlil doirasida
sinaldi, uni to'liq tekshirish uchun ayni bir obyektda boshqa usullarni
ham ishga tushirish va bog'liqliklarda aniqlangan zaifliklarning
erishib bo'ladiganligini baholash kerak. **Ochiq qoidalar to'plami**:
maxsus qoidalarni o'zbek tilidagi dasturlash amaliyotidagi nomlar
bo'yicha to'liq to'plamga keltirish mustaqil amaliy qiymatga ega
bo'lardi.
