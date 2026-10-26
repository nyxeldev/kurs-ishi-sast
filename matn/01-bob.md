# I BOB. DASTURIY XAVFSIZLIK VA KODNI TAHLIL QILISH ASOSLARI

## 1.1. Dasturiy ta'minot zaifliklari va ularning tasnifi

### Zaiflik, ekspluatatsiya va xavf tushunchalari

Sohada bir-biriga yaqin, lekin aynan bir xil bo'lmagan uchta tushuncha
ishlatiladi: nuqson (weakness), zaiflik (vulnerability) va ekspluatatsiya
(exploit). Ularni farqlash statik tahlil vositalarining imkoniyatlarini
to'g'ri baholash uchun zarur, chunki bu vositalar aynan birinchi tushuncha
bilan ishlaydi.

MITRE korporatsiyasining ta'rifiga ko'ra, nuqson — dasturiy yoki apparat
ta'minotidagi shunday holatki, u ma'lum sharoitlarda zaiflik yuzaga
kelishiga hissa qo'shishi mumkin [1]. Nuqson o'zi hali hujum imkoniyatini
anglatmaydi: SQL so'rovini satrlarni ulash yo'li bilan shakllantirish —
nuqson; agar unga tashqaridan nazorat qilinadigan ma'lumot filtrlanmagan
holda tushsa, nuqson zaiflikka aylanadi. Zaiflik — maxfiylik, yaxlitlik
yoki foydalanuvchanlikni buzishga olib keladigan real kamchilik;
ekspluatatsiya — undan amalda foydalanish usuli.

Xavf (risk) — texnik emas, boshqaruv tushunchasi: zaiflikdan foydalanish
ehtimoli va zararning birgalikdagi bahosi. Shu sababli bir xil texnik
jiddiylikka ega zaiflik internetga ochiq to'lov xizmatida va ichki
yordamchi skriptda bir xil ustuvorlikka ega emas. Statik tahlil vositasi
nuqsonni aniqlaydi, lekin xavf darajasini mustaqil belgilay olmaydi — bu
qaror doimo kontekstni biladigan muhandisga qoladi.

### CWE tasnifi

Nuqsonlarni tizimli hisobga olish uchun CWE (Common Weakness Enumeration —
keng tarqalgan nuqsonlar ro'yxati) tasnifi ishlab chiqilgan. U jamoatchilik
tomonidan rivojlantiriladi, AQSh Kiberxavfsizlik va infratuzilma xavfsizligi
agentligi (CISA) homiyligida, MITRE boshqaradigan HSSEDI instituti
tomonidan yuritiladi [1]. 2026-yil oktabr holatiga ro'yxat 944 ta nuqson
turini o'z ichiga oladi va yiliga uch-to'rt marta yangilanadi [1].

CWE yozuvlari abstraksiya darajalari bo'yicha ierarxiya hosil qiladi: eng
umumiy ustun (pillar) yozuvlardan sinf (class) va bazaviy (base) yozuvlar
orqali aniq variantlarga (variant) qadar; turli maqsadlar uchun turli
ko'rinishlar (view) mavjud [1]. Statik tahlil vositalari topilmalarini
odatda bazaviy darajadagi yozuvlarga bog'laydi. Amaliy ahamiyati bo'yicha
ajralib turadigan nuqsonlar CWE Top 25 ro'yxatida jamlanadi [2]; uning
2025-yilgi tahriridagi birinchi o'nlik A ilovasida keltirilgan.

CWE vositalarni qiyoslash uchun umumiy til beradi, lekin bu til to'liq bir
xil tushunilmaydi: turli vositalar ayni bir topilmani turli CWE kodlari
bilan belgilaydi. Shu sababli natijalarni qiyoslashdan oldin
normallashtirish talab etiladi (3.3-band).

### OWASP Top 10

OWASP (Open Worldwide Application Security Project) jamg'armasining Top 10
ro'yxati veb-ilovalar uchun eng muhim xavfsizlik xavflarini jamlaydi [3].
Ro'yxatning 2025-yilgi tahriri 2,8 milliondan ortiq ilova bo'yicha
to'plangan ma'lumotlarga va taxminan 220 000 ta CVE yozuviga tayanadi;
tahlilga jalb qilingan 589 ta CWE dan 248 tasi o'nta toifaga
biriktirilgan [3]. Toifalarning to'liq ro'yxati A ilovasida keltirilgan.

Ikkita toifa 2025-yilgi tahrirda yangi: ta'minot zanjiridagi nuqsonlar
(A03) va istisno holatlarini noto'g'ri boshqarish (A10) [3]. Birinchisining
ro'yxatga kirishi bog'liqliklar tahlilining mustaqil nazorat turiga
aylanganini ko'rsatadi.

OWASP Top 10 — nuqsonlar tasnifi emas, xavf toifalarining ro'yxati. Har
bir toifa o'nlab CWE yozuvini birlashtiradi, shuning uchun vositaning
qamrovini bevosita OWASP toifalari bo'yicha o'lchab bo'lmaydi: avval
topilmalar CWE darajasiga keltiriladi. Ushbu ishda etalon to'plam ham,
vositalar natijalari ham aynan shu sababdan CWE kodlari asosida
solishtiriladi (3.1-band).

### CVE/NVD va CVSS

CWE nuqson turini tavsiflasa, CVE (Common Vulnerabilities and Exposures)
aniq mahsulotning aniq versiyasidagi aniq zaiflikka beriladigan noyob
identifikatordir. Bu farq amaliy: statik tahlil vositasi loyihaning o'z
kodidagi nuqsonni topadi va uni CWE bilan belgilaydi, bog'liqliklar tahlili
vositasi esa begona paketdagi ma'lum zaiflikni topadi va uni CVE bilan
belgilaydi. Kengaytirilgan ma'lumotlar — ta'sir doirasi, konfiguratsiyalar,
baholar — NIST yuritadigan NVD ma'lumotlar bazasida to'planadi [7].

Jiddiylikni miqdoriy baholash uchun CVSS (Common Vulnerability Scoring
System) qo'llanadi. Uni FIRST tashkiloti yuritadi; 4.0 versiyasining
birinchi nashri 2023-yil 1-noyabrda e'lon qilingan [8]. CVSS v4.0 to'rtta
metrik guruhdan iborat: bazaviy (Base), tahdid (Threat), muhit
(Environmental) va qo'shimcha (Supplemental); baho 0,0 dan 10,0 gacha
shkalada beriladi va sifat darajalariga bo'linadi: 0,0 — yo'q; 0,1–3,9 —
past; 4,0–6,9 — o'rta; 7,0–8,9 — yuqori; 9,0–10,0 — kritik [8]. Bazaviy
baho zaiflikning o'zgarmas texnik xossalarini aks ettiradi va foydalanish
kontekstini hisobga olmaydi; kontekst muhit guruhidagi metrikalar orqali
kiritiladi [8]. Shu sababli faqat bazaviy bahoga tayanib ustuvorlik
belgilash xatoga olib keladi — bu cheklov sifat darvozalarini sozlashda
ahamiyatga ega (1.3-band).

**Xulosa.** Nuqson, zaiflik va xavf bir-biridan farq qiladigan
tushunchalar bo'lib, statik tahlil vositalari ularning faqat birinchisi
bilan ishlaydi. CWE, OWASP Top 10, CVE/NVD va CVSS bir-birini
almashtirmaydi: CWE nuqson turini, CVE aniq zaiflikni, CVSS uning
jiddiyligini, OWASP Top 10 esa xavf toifasini ifodalaydi. Vositalarni
qiyoslash uchun yagona asos sifatida CWE tanlanadi, chunki faqat shu tasnif
kod darajasidagi topilmalarga bevosita bog'lanadi.

---

## 1.2. Zaifliklarni aniqlash usullari

Usullar ikki belgi bo'yicha farqlanadi: tahlil obyekti nima (manba kodi,
ishlayotgan ilova yoki bog'liqliklar ro'yxati) va dastur tahlil paytida
bajariladimi. Shu ikki belgi to'rtta asosiy usulni belgilaydi.

**Statik tahlil (SAST)** — dasturni ishga tushirmasdan, uning manba kodi
yoki baytkodi asosida nuqsonlarni aniqlash. Tahlil kodning matni ustida
emas, tuzilmaviy modellari — abstrakt sintaksis daraxti, boshqaruv oqimi
grafi, ma'lumotlar oqimi — ustida olib boriladi (II bob). Asosiy kuchli
tomoni miqyoslanuvchanlik: vositani katta hajmdagi kodga va har bir
yig'ishda takroran qo'llash mumkin [17]. Yana bir afzalligi — topilma aniq
fayl va qatorga bog'lanadi, ya'ni tuzatish manzili darhol ma'lum.

OWASP statik tahlilning cheklovlarini ochiq sanab o'tadi: ko'p turdagi
zaifliklarni, masalan autentifikatsiya muammolarini, avtomatik topish juda
qiyin; yolg'on ijobiy natijalar soni yuqori; konfiguratsiyaga oid muammolar
kodda aks etmagani uchun ko'pincha aniqlanmaydi; topilgan muammoning
haqiqiy zaiflik ekanini isbotlash qiyin; kompilyatsiya qilib bo'lmaydigan
kodni tahlil qilish bir qator vositalar uchun muammo [17]. Kirish nazorati
va kriptografiyani noto'g'ri qo'llash ham shu qiyin toifaga kiradi [17].
Python ekotizimida bu usulni turli chuqurlikda amalga oshiradigan
vositalarga Bandit [9], Semgrep [10] va CodeQL [11] misol bo'ladi.

**Dinamik tahlil (DAST)** ishlayotgan ilovaga tashqaridan so'rovlar
yuborish va javobni tahlil qilish orqali bajariladi. OWASP ta'rifiga ko'ra,
bunday vositalar veb-ilovalarni tashqaridan skanerlaydi va saytlararo
skript bajarish, SQL inyeksiyasi, buyruq inyeksiyasi hamda yo'l bo'ylab
harakatlanish kabi zaifliklarni qidiradi [18]. Kuchli tomoni — haqiqiy
ishlaydigan tizim sinaladi, shuning uchun topilma odatda amalda
tasdiqlangan bo'ladi va dasturlash tiliga bog'liq emas. Cheklovi — qamrov
skaner yetib bora olgan marshrutlar bilan chegaralanadi, topilma esa
zaiflikning kod ichidagi manzilini ko'rsatmaydi.

**Interaktiv tahlil (IAST)** ilova ichiga joylashtirilgan agent yordamida
uni ishlash paytida kuzatadi; bu usul OWASP DevSecOps qo'llanmasida va
NIST ning DevSecOps bo'yicha nashrida mustaqil nazorat turi sifatida
keltiriladi [15; 16]. U statik va dinamik yondashuvlarning kuchli
tomonlarini birlashtirishga intiladi: agent ilova ichida turgani uchun kod
ichidagi joylashuvni ko'rsata oladi, topilma esa haqiqiy ijro yo'lida qayd
etiladi. Cheklovi — natija butunlay sinov qamroviga bog'liq: chaqirilmagan
funksiya tekshirilmay qoladi. Bundan tashqari IAST instrumentatsiya
o'rnatishni talab qiladi.

**Bog'liqliklar tahlili (SCA)** loyihaning o'z kodini emas, tashqi
kutubxonalarni tekshiradi: bog'liqliklar ro'yxati va versiyalari ma'lum
zaifliklar bazalariga solishtiriladi [16]; Python ekotizimidagi tipik
vakili — pip-audit [12]. Zarurligini sanoat ma'lumotlari tasdiqlaydi:
Black Duck kompaniyasining 2026-yilgi OSSRA hisoboti 17 ta sohadagi 947 ta
kod bazasini tekshirib, ochiq kodli komponentlar kod bazalarining 98
foizida uchrashini aniqladi; bir kod bazasiga to'g'ri keladigan
zaifliklarning o'rtacha soni bir yil ichida 107 foizga oshgan [26]. Asosiy
cheklovi — paketning o'rnatilganini ko'radi, lekin zaif funksiya amalda
chaqiriladimi, odatda aniqlamaydi.

**Sirlarni skanerlash.** Amalda beshinchi nazorat turi keng qo'llanadi: u
kodni semantik tahlil qilmaydi, omborning butun tarixini qattiq kodlangan
maxfiy ma'lumotlar borligi uchun shablon bo'yicha tekshiradi [19]. OWASP
DevSecOps qo'llanmasida aynan shu bosqich quvurning birinchi qadami
sifatida ko'rsatilgan [16]; u eng arzon, chunki kod omborga tushishidan
oldin ishlaydi (3.5-band).

**1.1-jadval. SAST, DAST, IAST va SCA usullarining qiyosi**

| Mezon | SAST | DAST | IAST | SCA |
|---|---|---|---|---|
| Tahlil obyekti | manba kodi, baytkod | ishlayotgan ilova, tashqaridan | ishlayotgan ilova, ichdan | bog'liqliklar ro'yxati |
| Manba kodi kerakmi | ha | yo'q | instrumentatsiya kerak | manifest yetarli |
| Dastur bajariladimi | yo'q | ha | ha | yo'q |
| Nima topadi | inyeksiyalar, qattiq kodlangan sirlar, xavfli API chaqiruvlari [17] | XSS, SQL va buyruq inyeksiyasi, yo'l bo'ylab harakatlanish [18] | ijro yo'lida tasdiqlangan zaifliklar [15; 16] | bog'liqliklardagi ma'lum CVE lar [26] |
| Nimani topolmaydi | konfiguratsiya, autentifikatsiya va kirish nazorati mantig'i [17] | kod ichidagi manzilni, sinalmagan marshrutlarni | bajarilmagan kodni | o'z kodidagi nuqsonlarni |
| Qachon qo'llanadi | har bir o'zgarishda | ishlaydigan stend paydo bo'lgach | funksional sinovlar bilan | bog'liqliklar o'zgarganda |
| Asosiy cheklov | yolg'on ijobiy natijalar [17] | qamrovning to'liq emasligi | sinov qamroviga bog'liqlik | erishib bo'lishini baholamaslik |

"Nimani topolmaydi" ustunlari bir-birini qoplamaydi — bu usullarning
raqobatchi emas, to'ldiruvchi ekanini bildiradi. Shuning uchun zamonaviy
jarayonlarda ular birgalikda qo'llanadi (1.3-band).

**Xulosa.** To'rtta usul turli obyektlarni turli vaqtda tekshiradi va
shuning uchun turli sinf zaifliklarini aniqlaydi. Statik tahlil ularning
ichida eng erta qo'llanadigani va eng arzon takrorlanadigani bo'lib, uning
asosiy to'lovi — yolg'on ijobiy natijalar soni. Hech bir usul yolg'iz
to'liq qamrov bermaydi; ushbu ishda bu holat statik tahlil vositalarining
o'zaro munosabatida ham o'lchab ko'riladi (3.3-band).

---

## 1.3. Xavfsiz ishlab chiqish hayotiy sikli va DevSecOps

### SSDLC va "shift-left" tamoyili

Xavfsiz dasturiy ta'minot ishlab chiqish hayotiy sikli (Secure Software
Development Life Cycle, SSDLC) — xavfsizlik nazoratlarini barcha
bosqichlarga singdirish yondashuvi. Uning eng keng tarqalgan rasmiy
ifodasi NIST ning SP 800-218 nashrida bayon etilgan: Xavfsiz dasturiy
ta'minot ishlab chiqish asosi (SSDF), 1.1 versiyasi 2022-yil fevralida
chiqqan, mualliflari M. Souppaya, K. Scarfone va D. Dodson [5]. SSDF
amaliyotlarni to'rt guruhga ajratadi: tashkilotni tayyorlash (PO),
dasturiy ta'minotni himoyalash (PS), xavfsiz dasturiy ta'minot yaratish
(PW) va zaifliklarga javob berish (RV) [5].

Ushbu ish mavzusiga to'g'ridan-to'g'ri aloqador ikkita amaliyot PW
guruhida: PW.7 — inson o'qiy oladigan kodni ko'rib chiqish va tahlil
qilish, PW.8 — bajariladigan kodni sinash [5]. Shu bo'linishning o'zi
1.2-banddagi tasnifni takrorlaydi. SSDF ning muhim xossasi — u aniq
jarayon modeliga bog'lanmagan: amaliyotlar shelale modeliga ham, Agile
yondashuviga ham, DevOps quvuriga ham bir xilda tatbiq etiladi [5]. Ya'ni
"xavfsiz hayotiy sikl" alohida metodologiya emas, mavjud jarayonga
qo'shiladigan nazoratlar to'plamidir.

"Chapga surish" (shift-left) tamoyili nazoratlarni kechki bosqichlardan
erta bosqichlarga ko'chirishni anglatadi. OWASP DevSecOps qo'llanmasining
e'lon qilingan maqsadi — xavfsizlik muammolarini imkon qadar erta
aniqlash [16]. Qo'llanma namunaviy quvurni ketma-ket bosqichlar sifatida
tavsiflaydi: sirlarni skanerlash, bog'liqliklar tahlili, statik tahlil,
infratuzilma kodini skanerlash, ta'minot zanjiri xavfsizligi, interaktiv
tahlil, API xavfsizligi, dinamik tahlil va boshqalar [16]. Bu
ketma-ketlikda statik tahlil eng boshida — ilova hali ishga
tushirilmasdan oldin qo'llanadigan birinchi kod darajasidagi nazorat
sifatida turadi. Xavfsizlikni shu tarzda singdirish amaliyoti DevSecOps
deb ataladi; NIST ning SP 800-204C nashri (2022-yil mart, muallif
R. Chandramouli) CI/CD quvurini ishlab chiquvchining manba kodini qurish,
sinash, paketlash, joylashtirish va ekspluatatsiya bosqichlaridan
o'tkazadigan ish oqimi sifatida ta'riflaydi [15].

### CI/CD dagi o'rni va sifat darvozasi

Statik tahlilni quvurning bir necha nuqtasida ishga tushirish mumkin:
ishlab chiquvchining muhitida, omborga yuborishdan oldin, kod ko'rigi
paytida, asosiy shoxga birlashtirishda va kechki to'liq skanerlashda.
Google kompaniyasining ko'p yillik tajribasi asosida yozilgan tahlilga
ko'ra, kod ko'rigi bosqichi eng qulay nuqta: deyarli barcha kod
birlashtirishdan oldin ko'rikdan o'tadi, muallif allaqachon o'zgartirish
kayfiyatida bo'ladi va ko'rikchi ogohlantirishni e'tiborsiz
qoldirmaslikka undaydi [25]. IDE ga integratsiya faqat juda tez tahlillar
uchun mos — odatda bir soniyadan kam, ideal holda 100 millisekunddan
kam [25]. Kompilyator darajasidagi tekshiruvlar eng kuchli majburlash
vositasi, lekin ular mutlaqo yolg'on ijobiy natijasiz ishlashi shart;
oddiy kompilyator ogohlantirishlari esa amalda e'tiborga olinmaydi [25].
Miqyos haqida tasavvur beruvchi raqam: Google ning Tricorder platformasi
kuniga 50 000 dan ortiq kod ko'rigi o'zgarishini tahlil qiladi, mualliflar
avtomatik tuzatishlarni kuniga taxminan 3 000 marta qo'llaydi [25].

Bir necha vositani bitta quvurda birlashtirishda chiqish formatlarining
turlichaligi muammo tug'diradi. Bu masala SARIF (Static Analysis Results
Interchange Format) standarti orqali hal qilinadi [14]: har bir vosita
natijasini SARIF da chiqaradi, platforma esa ularni bitta interfeysda
jamlaydi (3.5-band).

Sifat darvozasi (quality gate) — yig'ish natijasiga qo'yiladigan,
oldindan belgilangan shartlar to'plami; shartlar bajarilmasa quvur
to'xtaydi. SonarQube kabi platformalarda bu mexanizm sozlanadigan shartlar
ro'yxati sifatida amalga oshirilgan [13]. Darvozani sozlash muvozanat
masalasi: juda qattiq darvoza jamoani uni chetlab o'tishga majbur qiladi,
juda yumshog'i esa hech narsani o'zgartirmaydi. Amalda ikki yechim
qo'llanadi — shartlarni faqat yangi kodga nisbatan qo'llash yoki jiddiylik
chegarasini belgilash. Ikkinchisida 1.1-bandda qayd etilgan cheklov
hisobga olinishi kerak: jiddiylik bahosi foydalanish kontekstini aks
ettirmaydi [8].

**Xulosa.** SSDF xavfsizlik amaliyotlarini jarayon modelidan mustaqil
belgilaydi va kodni statik tahlil qilishni alohida amaliyot (PW.7)
sifatida ajratadi. "Chapga surish" tamoyili bu amaliyotni quvurning eng
boshiga joylashtiradi, chunki statik tahlil ishlaydigan stend talab
qilmaydi. Statik tahlilning CI/CD dagi qiymati esa topilmalar sonida emas,
ularning qaror qabul qilinadigan nuqtada — kod ko'rigi va sifat
darvozasida — ko'rinishidadir.

---

## 1.4. Statik tahlilni qo'llashning iqtisodiy asoslanishi

### Tuzatish narxining o'sishi: bahsli da'vo

Statik tahlilni joriy etishni asoslashda eng ko'p keltiriladigan dalil —
zaiflikni kech aniqlash narxining keskin o'sishi haqidagi da'vo. Uning
manbasi B. Boehm va V. Basili ning 2001-yilda IEEE Computer jurnalida chop
etilgan maqolasi: mualliflar dasturiy muammoni mahsulot topshirilgandan
keyin topish va tuzatish ko'pincha uni talablar va loyihalash bosqichida
topish va tuzatishdan taxminan 100 barobar qimmatga tushishini
ta'kidlaydi [20].

Ushbu raqamni keltirishdan oldin uch holatni hisobga olish zarur.
Birinchidan, mualliflarning o'zlari da'voni yumshatgan: 2001-yilgi
tahrirda ular "ko'pincha" so'zini ataylab qo'shgan va kichik, kritik
bo'lmagan tizimlar uchun nisbat 100:1 emas, 5:1 ga yaqin ekanini alohida
qayd etgan [20]. Ikkinchidan, keyingi empirik tadqiqotlar effektni
tasdiqlamadi: T. Menzies, W. Nichols, F. Shull va L. Layman 2006–2014
yillarda bajarilgan 171 ta loyiha ma'lumotlarini tahlil qilib,
"kechiktirilgan muammo effekti" ga dalil topmaganlarini e'lon qildi —
muammoni kechki bosqichda hal qilishga sarflangan mehnat uni paydo
bo'lishidan ko'p o'tmay hal qilishga sarflangan mehnatdan izchil yoki
sezilarli darajada ko'p bo'lmagan [21]. Uchinchidan, da'voning dalil
bazasi metodologik tanqidga uchragan: L. Bossavit bu ko'rsatkichning
cheklangan empirik asosdan umumiy "o'zgarish narxi egri chizig'i" ga
aylanganini ko'rsatib bergan [22].

Shu sababli ushbu ishda 100 barobarlik ko'rsatkich dalil sifatida
ishlatilmaydi. Da'vo adabiyotda keng tarqalgani uchun bu yerda
keltirildi, lekin ikkala tomonga ham havola bilan va bahsli ekani ochiq
aytilgan holda.

### Tekshiriladigan asoslar va yolg'on ijobiy natijalarning narxi

100 barobarlik raqamdan voz kechish statik tahlilning iqtisodiy ma'nosini
inkor etmaydi — u boshqa, tekshirilishi mumkin bo'lgan asoslarga
tayanishini talab qiladi. Birinchisi — aniqlash amalining takrorlanish
narxi: qo'lda kod ko'rigi har safar muhandis vaqtini talab qiladi va kod
bazasi o'sgan sari qimmatlashadi, avtomatik tahlilni esa muntazam ravishda
qayta-qayta qo'llash mumkin [17] va takroriy ishga tushirishning
qo'shimcha narxi deyarli nolga teng (3.2-band). Ikkinchisi — qamrovning
bir xilligi: avtomatik vosita butun kod bazasini har safar bir xil
mezonlar bilan tekshiradi, qo'lda ko'rikning sifati esa ko'rikchining
tajribasiga va charchoqqa bog'liq. Uchinchisi — mehnat taqsimoti: statik
tahlil takrorlanuvchi, shablonli nuqsonlarni ishonchli topadi va muhandis
vaqtini avtomatika yetmaydigan masalalarga bo'shatadi. OWASP
ta'kidlaganidek, kirish nazorati mantig'i, autentifikatsiya va
kriptografiyaning noto'g'ri qo'llanishi avtomatik aniqlash uchun qiyin
bo'lib qolmoqda [17]. Demak to'g'ri nisbat — avtomatik tahlilni birinchi
filtr, qo'lda ko'rikni uning davomi sifatida qo'llash.

Statik tahlilning asosiy xarajati litsenziya emas, har bir ogohlantirishni
ko'rib chiqishga sarflanadigan muhandis vaqtidir. B. Johnson va
hammualliflarining 2013-yilgi tadqiqotida 20 ta ishlab chiquvchi bilan
o'tkazilgan suhbatlar shuni ko'rsatdiki, ishtirokchilar vositalarning
qiymatini tan olsalar-da, yolg'on ijobiy natijalar va natijalarning taqdim
etilish usuli ulardan foydalanishga to'siq bo'lmoqda [24]. Google
kompaniyasida bu muammo miqdoriy mezon ko'rinishiga keltirilgan: agar
ishlab chiquvchi ogohlantirishni ko'rgandan keyin hech qanday ijobiy
harakat qilmasa, topilma "samarali yolg'on ijobiy natija" deb hisoblanadi —
vosita texnik jihatdan haq bo'lgan taqdirda ham [23]. Yangi tekshiruvni
platformaga qo'shish uchun uning samarali yolg'on ijobiy natijalar ulushi
10 foizdan kam bo'lishi talab qilinadi; platforma bo'yicha umumiy
ko'rsatkich 5 foizdan biroz pastda turadi [25].

Iqtisodiy mantiq aniq: vositaning qiymati u topgan zaifliklar sonida emas,
balki shu topilmalarni ko'rib chiqishga ketgan vaqtga nisbatan o'lchanadi.
Aniqlik ko'rsatkichi past vosita ko'p zaiflik topsa ham, muhandislar unga
ishonishni to'xtatgan paytdan boshlab amalda foydasiz bo'lib qoladi — bu
hodisa ogohlantirishlardan charchash (alert fatigue) deb ataladi
(2.4-band). Aynan shu sababli ushbu ishda vositalar faqat topilmalar soni
bo'yicha emas, Precision, Recall va F1 ko'rsatkichlari bo'yicha ham
qiyoslanadi.

**Xulosa.** Statik tahlilni asoslashda keng tarqalgan 100 barobarlik
ko'rsatkich zamonaviy empirik tadqiqotlarda tasdiqlanmagan va shu sababli
dalil sifatida ishlatilmaydi. Usulning iqtisodiy ma'nosi boshqa,
tekshiriladigan asoslarda — avtomatik tekshiruvning deyarli bepul
takrorlanishida, qamrovning bir xilligida va muhandis vaqtini avtomatika
yetmaydigan masalalarga bo'shatishida. Bu foydani yolg'on ijobiy natijalar
ulushi bevosita kamaytiradi, shuning uchun vositani tanlashda aniqlik
ko'rsatkichi topilmalar sonidan muhimroqdir.
