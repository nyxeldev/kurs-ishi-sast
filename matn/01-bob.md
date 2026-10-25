# I BOB. DASTURIY XAVFSIZLIK VA KODNI TAHLIL QILISH ASOSLARI

## 1.1. Dasturiy ta'minot zaifliklari va ularning tasnifi

### Zaiflik, ekspluatatsiya va xavf tushunchalari

Dasturiy ta'minot xavfsizligi sohasida bir-biriga yaqin, lekin aynan bir xil
bo'lmagan uchta tushuncha ishlatiladi: nuqson (weakness), zaiflik
(vulnerability) va ekspluatatsiya (exploit). Ularni farqlash statik tahlil
vositalarining imkoniyatlarini to'g'ri baholash uchun zarur, chunki bu
vositalar aynan birinchi tushuncha bilan ishlaydi.

MITRE korporatsiyasining ta'rifiga ko'ra, nuqson — dasturiy yoki apparat
ta'minotidagi shunday holatki, u ma'lum sharoitlarda zaiflik yuzaga
kelishiga hissa qo'shishi mumkin [1]. Nuqson kodning tuzilishidagi
kamchilikdir va o'zi hali hujum imkoniyatini anglatmaydi. Masalan, SQL
so'rovini satrlarni ulash yo'li bilan shakllantirish — nuqson; agar bu
so'rovga tashqaridan nazorat qilinadigan ma'lumot tushsa va u filtrlanmasa,
nuqson zaiflikka aylanadi.

Zaiflik — tizimning buzg'unchi tomonidan foydalanilishi mumkin bo'lgan,
ya'ni maxfiylik, yaxlitlik yoki foydalanuvchanlikni buzishga olib keladigan
real kamchiligi. Ekspluatatsiya — zaiflikdan amalda foydalanishga qaratilgan
aniq usul, ma'lumotlar to'plami yoki dastur. Bitta zaiflik uchun bir nechta
ekspluatatsiya mavjud bo'lishi mumkin, ayrim zaifliklar uchun esa umuman
ishlaydigan ekspluatatsiya topilmaydi.

Xavf (risk) — texnik emas, boshqaruv tushunchasi. U zaiflikdan foydalanish
ehtimoli va bundan kelib chiqadigan zararning birgalikdagi bahosi sifatida
qaraladi. Shu sababli bir xil texnik jiddiylikka ega ikki zaiflik turli
tizimlarda butunlay boshqacha xavf darajasiga ega bo'lishi mumkin: internetga
ochiq to'lov xizmatidagi zaiflik va ichki tarmoqdagi yordamchi skriptdagi
o'sha zaiflik bir xil ustuvorlikka ega emas. Statik tahlil vositasi nuqsonni
aniqlaydi, lekin xavf darajasini mustaqil ravishda belgilay olmaydi — bu
qaror doimo kontekstni biladigan muhandisga qoladi.

### CWE tasnifi va uning tuzilishi

Nuqsonlarni tizimli hisobga olish uchun CWE (Common Weakness Enumeration —
keng tarqalgan nuqsonlar ro'yxati) tasnifi ishlab chiqilgan. U jamoatchilik
tomonidan rivojlantiriladi, AQSh Ichki xavfsizlik vazirligining
Kiberxavfsizlik va infratuzilma xavfsizligi agentligi (CISA) homiyligida,
MITRE korporatsiyasi boshqaradigan HSSEDI instituti tomonidan yuritiladi [1].
2026-yil oktabr holatiga ko'ra ro'yxat 944 ta nuqson turini o'z ichiga oladi
va yiliga uch-to'rt marta yangilanadi [1].

CWE yozuvlari abstraksiya darajalari bo'yicha ierarxiya hosil qiladi: eng
umumiy ustun (pillar) yozuvlardan sinf (class) va bazaviy (base) yozuvlar
orqali aniq variantlarga (variant) qadar. Bir xil ro'yxat turli maqsadlar
uchun turli ko'rinishlarda (view) taqdim etiladi: tadqiqot maqsadlari uchun
CWE-1000 (Research Concepts), dasturiy ta'minot ishlab chiqish uchun CWE-699
(Software Development), apparat loyihalash uchun CWE-1194 (Hardware Design)
[1]. Statik tahlil vositalari o'z topilmalarini odatda bazaviy darajadagi
yozuvlarga bog'laydi.

Amaliy ahamiyati bo'yicha ajralib turadigan nuqsonlar CWE Top 25 ro'yxatida
jamlanadi. Uning 2025-yilgi tahriridagi birinchi o'nlik 1.1-jadvalda
keltirilgan.

**1.1-jadval. CWE Top 25 (2025) ro'yxatining birinchi o'nligi**

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

Manba: [2].

CWE tasnifi vositalarni qiyoslash uchun umumiy til beradi, lekin bu til
to'liq bir xil tushunilmaydi: amaliyotda turli vositalar ayni bir topilmani
turli CWE kodlari bilan belgilashi mumkin, ayrim qoidalarga esa bir vaqtning
o'zida bir nechta kod biriktiriladi. Shu sababli vositalar natijalarini
qiyoslashdan oldin ularni normallashtirish talab etiladi; bu masalaning
amaliy yechimi 3.3-bandda ko'rib chiqiladi.

### OWASP Top 10 — asosiy toifalar

OWASP (Open Worldwide Application Security Project) jamg'armasi chiqaradigan
Top 10 ro'yxati veb-ilovalar uchun eng muhim xavfsizlik xavflarini
jamlaydi [3]. Ro'yxatning 2025-yilgi tahriri 2,8 milliondan ortiq ilova
bo'yicha to'plangan ma'lumotlarga va taxminan 220 000 ta CVE yozuviga
tayanadi; tahlilga jalb qilingan 589 ta CWE dan 248 tasi o'nta toifaga
biriktirilgan [3]. Toifalar 1.2-jadvalda keltirilgan.

**1.2-jadval. OWASP Top 10:2025 toifalari**

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

Manba: [3].

2025-yilgi tahrirda ikkita toifa yangi: ta'minot zanjiridagi nuqsonlar (A03)
va istisno holatlarini noto'g'ri boshqarish (A10) [3]. Birinchisining
ro'yxatga kirishi bog'liqliklar tahlilining (1.2-band) mustaqil nazorat
turiga aylanganini ko'rsatadi.

Shuni ta'kidlash kerakki, OWASP Top 10 — nuqsonlar tasnifi emas, balki xavf
toifalarining ro'yxati. Har bir toifa o'nlab CWE yozuvini birlashtiradi,
shuning uchun statik tahlil vositasining qamrovini bevosita OWASP toifalari
bo'yicha o'lchab bo'lmaydi: avval topilmalar CWE darajasiga keltiriladi.
Ushbu ishda etalon to'plam ham, vositalar natijalari ham aynan shu sababdan
CWE kodlari asosida solishtiriladi (3.1-band).

### CVE/NVD ekotizimi va CVSS baholash tizimi

CWE nuqson turini tavsiflasa, CVE (Common Vulnerabilities and Exposures)
aniq mahsulotning aniq versiyasidagi aniq zaiflikka beriladigan noyob
identifikatordir. Bu farq amaliy ahamiyatga ega: statik tahlil vositasi
loyihaning o'z kodidagi nuqsonni topadi va uni CWE bilan belgilaydi,
bog'liqliklar tahlili vositasi esa ishlatilayotgan begona paketdagi ma'lum
zaiflikni topadi va uni CVE bilan belgilaydi. Ikkala natija ham zarur, lekin
ular bir xil savolga javob bermaydi.

CVE yozuvlari to'g'risidagi kengaytirilgan ma'lumotlar — jumladan ta'sir
doirasi, konfiguratsiyalar va baholar — AQSh Milliy standartlar va
texnologiyalar instituti yuritadigan NVD (National Vulnerability Database)
ma'lumotlar bazasida to'planadi [7]. Bog'liqliklar tahlili vositalari aynan
shunday bazalarga murojaat qiladi.

Zaifliklarning jiddiyligini miqdoriy baholash uchun CVSS (Common
Vulnerability Scoring System) tizimi qo'llanadi. Uni FIRST nodavlat
tashkiloti yuritadi; 4.0 versiyasining birinchi nashri 2023-yil 1-noyabrda
e'lon qilingan [8]. CVSS v4.0 to'rtta metrik guruhdan iborat: bazaviy
(Base), tahdid (Threat), muhit (Environmental) va qo'shimcha (Supplemental)
[8]. Yakuniy baho 0,0 dan 10,0 gacha bo'lgan shkalada beriladi va sifat
darajalariga bo'linadi: 0,0 — yo'q; 0,1–3,9 — past; 4,0–6,9 — o'rta;
7,0–8,9 — yuqori; 9,0–10,0 — kritik [8].

CVSS ning bazaviy bahosi zaiflikning o'zgarmas texnik xossalarini aks
ettiradi va foydalanish kontekstini hisobga olmaydi; kontekst muhit
guruhidagi metrikalar orqali kiritiladi [8]. Shu sababli faqat bazaviy
bahoga tayanib ustuvorlik belgilash xatoga olib keladi — bu cheklov sifat
darvozalarini sozlashda alohida ahamiyatga ega (1.3-band).

**Xulosa.** Nuqson, zaiflik va xavf bir-biridan farq qiladigan tushunchalar
bo'lib, statik tahlil vositalari ularning faqat birinchisi bilan ishlaydi.
CWE, OWASP Top 10, CVE/NVD va CVSS bir-birini almashtirmaydi: CWE nuqson
turini, CVE aniq zaiflikni, CVSS uning jiddiyligini, OWASP Top 10 esa xavf
toifasini ifodalaydi. Vositalarni qiyoslash uchun yagona asos sifatida CWE
tanlanadi, chunki faqat shu tasnif kod darajasidagi topilmalarga bevosita
bog'lanadi.

---

## 1.2. Zaifliklarni aniqlash usullari

Zaifliklarni avtomatik aniqlash usullari bir-biridan ikki belgi bo'yicha
farqlanadi: tahlil obyekti sifatida nima olinadi (manba kodi, ishlayotgan
ilova yoki bog'liqliklar ro'yxati) va dastur tahlil paytida bajariladimi
yoki yo'qmi. Shu ikki belgi to'rtta asosiy usulni belgilaydi.

### Statik tahlil (SAST) — mohiyati va qamrovi

Statik ilova xavfsizligini sinash (Static Application Security Testing,
SAST) — dasturni ishga tushirmasdan, uning manba kodi, oraliq ko'rinishi
yoki baytkodi asosida nuqsonlarni aniqlash usuli. Tahlil kodning matni
ustida emas, balki uning tuzilmaviy modeli — abstrakt sintaksis daraxti,
boshqaruv oqimi grafi va ma'lumotlar oqimi — ustida olib boriladi; bu
modellar II bobda batafsil ko'rib chiqiladi.

SAST ning asosiy kuchli tomoni — miqyoslanuvchanlik: vositani katta hajmdagi
kodga qo'llash va uni muntazam, masalan har bir yig'ishda takroran ishga
tushirish mumkin [17]. Vosita yuqori ishonch bilan avtomatik aniqlay
oladigan nuqsonlar uchun bu usul samarali hisoblanadi [17]. SAST ning yana
bir muhim afzalligi — topilma aniq fayl va qatorga bog'lanadi, ya'ni
tuzatish manzili darhol ma'lum bo'ladi.

OWASP statik tahlilning cheklovlarini ochiq sanab o'tadi: ko'p turdagi
xavfsizlik zaifliklarini, masalan autentifikatsiya muammolarini, avtomatik
topish juda qiyin; yolg'on ijobiy natijalar soni yuqori; konfiguratsiyaga
oid muammolar kodda aks etmagani uchun ko'pincha aniqlanmaydi; topilgan
muammoning haqiqiy zaiflik ekanini isbotlash qiyin; kompilyatsiya qilib
bo'lmaydigan kodni tahlil qilish bir qator vositalar uchun muammo bo'lib
qoladi [17]. Kirish nazorati va kriptografiyani noto'g'ri qo'llash ham shu
qiyin toifaga kiradi [17].

Python ekotizimida bu usulni turli chuqurlikda amalga oshiradigan
vositalarga Bandit [9], Semgrep [10] va CodeQL [11] misol bo'ladi; ularning
ishlash prinsipi 2.3-bandda ko'rib chiqiladi.

### Dinamik tahlil (DAST)

Dinamik ilova xavfsizligini sinash (Dynamic Application Security Testing,
DAST) ishlayotgan ilovaga tashqaridan so'rovlar yuborish va uning javobini
tahlil qilish orqali amalga oshiriladi. OWASP ta'rifiga ko'ra, bunday
vositalar veb-ilovalarni odatda tashqaridan skanerlaydi va saytlararo skript
bajarish, SQL inyeksiyasi, buyruq inyeksiyasi hamda yo'l bo'ylab
harakatlanish kabi zaifliklarni qidiradi [18].

DAST ning kuchli tomoni — u haqiqiy ishlaydigan tizimni sinaydi, shuning
uchun topilgan zaiflik odatda amalda tasdiqlangan bo'ladi va manba kodiga
ham, dasturlash tiliga ham bog'liq emas. Cheklovi esa shundaki, qamrov
skaner yetib bora olgan marshrutlar bilan chegaralanadi: autentifikatsiya
talab qiladigan yoki murakkab ketma-ketlik orqali ochiladigan bo'limlar
sinovdan tashqarida qolishi mumkin. Bundan tashqari, DAST topilmasi zaiflik
kodning qaysi qatorida joylashganini ko'rsatmaydi — tuzatish manzilini
muhandis o'zi izlashi kerak.

### Interaktiv tahlil (IAST)

Interaktiv ilova xavfsizligini sinash (Interactive Application Security
Testing, IAST) ilova ichiga joylashtirilgan agent yoki instrumentatsiya
yordamida uni ishlash paytida kuzatadi. Bu usul OWASP DevSecOps
qo'llanmasida va NIST ning DevSecOps bo'yicha nashrida mustaqil nazorat
turi sifatida keltiriladi [15; 16].

IAST statik va dinamik yondashuvlarning kuchli tomonlarini birlashtirishga
intiladi: agent ilova ichida turgani uchun u zaiflikning kod ichidagi
joylashuvini ko'rsata oladi, ayni paytda topilma haqiqiy ijro yo'lida qayd
etilgani uchun uning ishonchliligi yuqori bo'ladi. Cheklovi — natija
butunlay sinov qamroviga bog'liq: agent faqat bajarilgan kodni ko'radi,
hech qachon chaqirilmagan funksiya esa tekshirilmay qoladi. Bundan tashqari,
IAST ishlaydigan muhitni va ilovaga instrumentatsiya o'rnatish imkonini
talab qiladi, bu esa uni SAST ga qaraganda qimmatroq joriy etiladigan
nazoratga aylantiradi.

### Bog'liqliklar tahlili (SCA)

Dasturiy ta'minot tarkibini tahlil qilish (Software Composition Analysis,
SCA) loyihaning o'z kodini emas, balki u foydalanadigan tashqi
kutubxonalarni tekshiradi: bog'liqliklar ro'yxati va ularning versiyalari
ma'lum zaifliklar bazalariga solishtiriladi [16]. Python ekotizimidagi
tipik vakili — pip-audit [12].

Bu nazoratning zarurligini sanoat ma'lumotlari tasdiqlaydi. Black Duck
kompaniyasining 2026-yilgi OSSRA hisoboti 17 ta sohadagi 947 ta kod bazasini
tekshirib, ochiq kodli komponentlar kod bazalarining 98 foizida uchrashini
aniqladi; bir kod bazasiga to'g'ri keladigan zaifliklarning o'rtacha soni
bir yil ichida 107 foizga oshgan, litsenziya ziddiyatlari esa 56 foizdan
68 foizga ko'tarilgan [26]. Ya'ni zamonaviy ilovaning xavfsizligi sezilarli
darajada o'zga mualliflar yozgan kodga bog'liq, bu kodni esa statik tahlil
vositalari odatda umuman skanerlamaydi.

SCA ning asosiy cheklovi — u paketning o'rnatilganini ko'radi, lekin zaif
funksiya amalda chaqiriladimi yoki yo'qmi, odatda aniqlamaydi. Shu sababli
SCA topilmalari ko'p bo'ladi va ularni ustuvorlashtirish alohida ish talab
qiladi.

### Sirlarni skanerlash

Yuqoridagi to'rtlikdan tashqari amalda beshinchi nazorat turi — sirlarni
skanerlash (secret scanning) keng qo'llanadi. U kodni semantik tahlil
qilmaydi, balki omborning butun tarixini qattiq kodlangan maxfiy
ma'lumotlar — API kalitlari, parollar va tokenlar — borligi uchun shablon
bo'yicha tekshiradi [19]. OWASP DevSecOps qo'llanmasida aynan shu bosqich
quvurning birinchi qadami sifatida ko'rsatilgan [16]. Bu nazorat eng
arzon, chunki u kod omborga tushishidan oldin ishlashi mumkin; ushbu
ishning amaliy qismida uning amalda ishlagani qayd etilgan (3.5-band).

### Qiyosiy jadval

To'rtta asosiy usulning qiyosiy tavsifi 1.3-jadvalda keltirilgan.

**1.3-jadval. SAST, DAST, IAST va SCA usullarining qiyosi**

| Mezon | SAST | DAST | IAST | SCA |
|---|---|---|---|---|
| Tahlil obyekti | manba kodi, baytkod | ishlayotgan ilova, tashqaridan | ishlayotgan ilova, ichdan | bog'liqliklar ro'yxati |
| Manba kodi kerakmi | ha | yo'q | yo'q, lekin instrumentatsiya kerak | yo'q, manifest yetarli |
| Dastur bajariladimi | yo'q | ha | ha | yo'q |
| Nima topadi | inyeksiyalar, qattiq kodlangan sirlar, xavfli API chaqiruvlari, zaif kriptografiya [17] | XSS, SQL inyeksiyasi, buyruq inyeksiyasi, yo'l bo'ylab harakatlanish [18] | ijro yo'lida tasdiqlangan zaifliklar, kod manzili bilan [15; 16] | bog'liqliklardagi ma'lum CVE lar, litsenziya ziddiyatlari [26] |
| Nimani topolmaydi | konfiguratsiya muammolari, autentifikatsiya va kirish nazorati mantig'i [17] | zaiflikning kod ichidagi manzilini, sinovdan o'tmagan marshrutlarni | bajarilmagan kodni, sinov qamrovidan tashqaridagini | loyihaning o'z kodidagi nuqsonlarni |
| Qachon qo'llanadi | kod yozilishi bilan, har bir o'zgarishda | ishlaydigan stend paydo bo'lgach | funksional sinovlar bilan birga | bog'liqliklar o'zgarganda va muntazam |
| Topilmaning manzili | fayl va qator | so'rov va javob | fayl va qator | paket va versiya |
| Asosiy cheklov | yolg'on ijobiy natijalar [17] | qamrovning to'liq emasligi | sinov qamroviga bog'liqlik | zaif kodga erishib bo'lishini baholamaslik |

1.3-jadvaldan ko'rinadiki, usullarning "nimani topolmaydi" ustunlari
bir-birini qoplamaydi. Bu ularning raqobatchi emas, to'ldiruvchi ekanini
bildiradi: SAST konfiguratsiyani ko'rmaydi, DAST kod manzilini bermaydi,
IAST sinalmagan kodni tekshirmaydi, SCA esa loyihaning o'z kodiga umuman
qaramaydi. Shuning uchun zamonaviy xavfsiz ishlab chiqish jarayonlarida
ular birgalikda qo'llanadi (1.3-band).

**Xulosa.** To'rtta usul turli obyektlarni turli vaqtda tekshiradi va
shuning uchun turli sinf zaifliklarini aniqlaydi. Statik tahlil ularning
ichida eng erta qo'llanadigani va eng arzon takrorlanadigani bo'lib, uning
asosiy to'lovi — yolg'on ijobiy natijalar soni. Hech bir usul yolg'iz
to'liq qamrov bermaydi; ushbu ishda bu holat statik tahlil vositalarining
o'zaro munosabatida ham o'lchab ko'riladi (3.3-band).

---

## 1.3. Xavfsiz ishlab chiqish hayotiy sikli va DevSecOps

### SSDLC bosqichlari

Xavfsiz dasturiy ta'minot ishlab chiqish hayotiy sikli (Secure Software
Development Life Cycle, SSDLC) — xavfsizlik nazoratlarini loyihaning
boshidan oxirigacha barcha bosqichlarga singdirish yondashuvi. Uning eng
keng tarqalgan rasmiy ifodasi — NIST ning SP 800-218 nashrida bayon etilgan
Xavfsiz dasturiy ta'minot ishlab chiqish asosi (Secure Software Development
Framework, SSDF). Hujjatning 1.1 versiyasi 2022-yil fevralida chiqqan,
mualliflari — M. Souppaya, K. Scarfone va D. Dodson [5].

SSDF amaliyotlarni to'rt guruhga ajratadi [5]:

- **PO (Prepare the Organization)** — tashkilotni tayyorlash: talablarni
  belgilash, rollarni taqsimlash, asboblar majmuasini joriy etish;
- **PS (Protect the Software)** — dasturiy ta'minotni himoyalash: kod va
  artefaktlarning yaxlitligini ta'minlash;
- **PW (Produce Well-Secured Software)** — xavfsiz dasturiy ta'minot
  yaratish: loyihalash, kod yozish va kodni tekshirish amaliyotlari;
- **RV (Respond to Vulnerabilities)** — zaifliklarga javob berish: ularni
  aniqlash, tuzatish va kelib chiqish sabablarini bartaraf etish.

Ushbu ish mavzusiga to'g'ridan-to'g'ri aloqador ikkita amaliyot PW guruhida
joylashgan: PW.7 — inson o'qiy oladigan kodni ko'rib chiqish va tahlil
qilish, PW.8 — bajariladigan kodni sinash [5]. Shu bo'linishning o'zi
1.2-banddagi tasnifni takrorlaydi: PW.7 statik, PW.8 esa dinamik
nazoratlarga mos keladi.

SSDF ning muhim xossasi — u aniq jarayon modeliga bog'lanmagan: amaliyotlar
shelale modeliga ham, Agile yondashuviga ham, DevOps quvuriga ham bir xilda
tatbiq etiladi [5]. Ya'ni "xavfsiz hayotiy sikl" alohida metodologiya emas,
mavjud jarayonga qo'shiladigan nazoratlar to'plamidir.

### "Shift-left" tamoyili

"Chapga surish" (shift-left) tamoyili xavfsizlik nazoratlarini hayotiy
siklning kechki bosqichlaridan (sinov, ekspluatatsiya) erta bosqichlariga
(loyihalash, kod yozish) ko'chirishni anglatadi. OWASP DevSecOps
qo'llanmasining e'lon qilingan maqsadi — xavfsizlik muammolarini,
loyihalashdagi yoki ilovadagi zaifliklarni, imkon qadar erta aniqlash [16].

Qo'llanma namunaviy quvurni ketma-ket bosqichlar sifatida tavsiflaydi: git
omborlarini maxfiy ma'lumotlarning sizib chiqishi uchun skanerlash,
bog'liqliklar tahlili (SCA), statik tahlil (SAST), infratuzilma kodini (IaC)
skanerlash, ta'minot zanjiri xavfsizligi, interaktiv tahlil (IAST), API
xavfsizligi, dinamik tahlil (DAST), bulutli muhit himoyasi (CNAPP),
infratuzilmani skanerlash, boshqa vositalar bilan uzluksiz skanerlash va
muvofiqlikni tekshirish [16]. Bu ketma-ketlikda statik tahlil eng boshida —
ilova hali ishga tushirilmasdan oldin qo'llanadigan birinchi kod darajasidagi
nazorat sifatida turadi.

Xavfsizlikni ishlab chiqish va ekspluatatsiya jarayonlariga shu tarzda
singdirish amaliyoti DevSecOps deb ataladi. NIST ning SP 800-204C nashri
(2022-yil mart, muallif R. Chandramouli) DevSecOps ni bulutga mo'ljallangan,
mikroservislardan tashkil topgan ilovalar uchun imkoniyat yaratuvchi
paradigma sifatida tavsiflaydi va CI/CD quvurini ishlab chiquvchining manba
kodini qurish, sinash, paketlash, joylashtirish va ekspluatatsiya
bosqichlaridan o'tkazadigan ish oqimi sifatida ta'riflaydi [15].

### Statik tahlilning CI/CD quvuridagi o'rni

Statik tahlilni quvurning bir necha nuqtasida ishga tushirish mumkin: ishlab
chiquvchining muhitida (IDE), o'zgarishni omborga yuborishdan oldin
(pre-commit), kod ko'rigi (pull request) paytida, asosiy shoxga
birlashtirishda va kechki to'liq skanerlashda. Bu nuqtalar bir-birini
istisno qilmaydi, lekin ularning narxi va ta'siri turlicha.

Google kompaniyasining ko'p yillik tajribasi asosida yozilgan tahlilga
ko'ra, kod ko'rigi bosqichi tahlil natijalari uchun eng qulay nuqta
hisoblanadi: deyarli barcha kod birlashtirishdan oldin ko'rikdan o'tadi,
muallif allaqachon o'zgartirish kayfiyatida bo'ladi va ko'rikchi
ogohlantirishni e'tiborsiz qoldirmaslikka undaydi [25]. IDE ga integratsiya
faqat juda tez tahlillar uchun mos keladi — odatda bir soniyadan kam, ideal
holda 100 millisekunddan kam [25]. Kompilyator darajasidagi tekshiruvlar eng
kuchli majburlash vositasi, chunki qurilishni to'xtatadigan ogohlantirishni
e'tiborsiz qoldirib bo'lmaydi; lekin ular mutlaqo yolg'on ijobiy natijasiz
ishlashi shart, oddiy kompilyator ogohlantirishlari esa amalda e'tiborga
olinmaydi [25].

Bunday integratsiyaning miqyosi haqida tasavvur beruvchi raqamlar ham
keltirilgan: Google ning Tricorder platformasi kuniga 50 000 dan ortiq kod
ko'rigi o'zgarishini tahlil qiladi, mualliflar avtomatik taklif qilingan
tuzatishlarni kuniga taxminan 3 000 marta qo'llaydi, ko'rikchilar esa
"Please Fix" tugmasini kuniga minglab marta bosadi [25].

Bir necha vositani bitta quvurda birlashtirishda ularning chiqish
formatlari turlicha bo'lishi muammo tug'diradi. Bu masala natijalarni yagona
ko'rinishga keltiruvchi SARIF (Static Analysis Results Interchange Format)
standarti orqali hal qilinadi [14]: har bir vosita o'z natijasini SARIF da
chiqaradi, platforma esa ularni bitta interfeysda jamlaydi. Ushbu ishning
amaliy qismida to'rtta vosita natijasi aynan shu tarzda birlashtirilgan
(3.5-band).

### Sifat darvozasi tushunchasi

Sifat darvozasi (quality gate) — yig'ish natijasiga qo'yiladigan, oldindan
belgilangan shartlar to'plami. Shartlar bajarilmasa, quvur to'xtaydi va
o'zgarish keyingi bosqichga o'tkazilmaydi. SonarQube kabi platformalarda bu
mexanizm sozlanadigan shartlar ro'yxati sifatida amalga oshirilgan [13].

Darvozani sozlash amalda muvozanat masalasidir. Juda qattiq darvoza — har
qanday jiddiylikdagi har qanday topilmada qurilishni to'xtatish — jamoani
uni chetlab o'tish yo'llarini izlashga majbur qiladi. Juda yumshoq darvoza
esa hech narsani o'zgartirmaydi. Amalda qo'llanadigan ikki yechim mavjud:
birinchidan, shartlarni faqat yangi yoki o'zgargan kodga nisbatan qo'llash —
bunda mavjud texnik qarz quvurni bloklamaydi, lekin yangi qarz to'planmaydi;
ikkinchidan, jiddiylik chegarasini belgilash — masalan, faqat yuqori va
kritik darajadagi topilmalar qurilishni to'xtatadi. Ikkinchi yechimda
1.1-bandda qayd etilgan cheklov hisobga olinishi kerak: jiddiylik bahosi
foydalanish kontekstini o'zida aks ettirmaydi [8].

Ushbu ishning amaliy qismida shunday darvoza amalda sinovdan o'tkazilgan:
GitHub Actions quvurida yuqori jiddiylikdagi statik tahlil topilmasi va zaif
bog'liqlik aniqlanganda qurilish ataylab to'xtatilgan (3.5-band).

**Xulosa.** SSDF xavfsizlik amaliyotlarini jarayon modelidan mustaqil
ravishda belgilaydi va kodni statik tahlil qilishni alohida amaliyot (PW.7)
sifatida ajratadi. "Chapga surish" tamoyili bu amaliyotni quvurning eng
boshiga joylashtiradi, chunki statik tahlil ishlaydigan stend talab
qilmaydi. Statik tahlilning CI/CD dagi qiymati esa topilmalar sonida emas,
ularning qaror qabul qilinadigan nuqtada — kod ko'rigi va sifat darvozasida
— ko'rinishidadir.

---

## 1.4. Statik tahlilni qo'llashning iqtisodiy asoslanishi

### Tuzatish narxining bosqichlar bo'yicha o'sishi: bahsli da'vo

Statik tahlilni joriy etishni asoslashda eng ko'p keltiriladigan dalil —
zaiflikni kech aniqlash narxining keskin o'sishi haqidagi da'vo. Uning
manbasi B. Boehm va V. Basili ning 2001-yilda IEEE Computer jurnalida chop
etilgan maqolasidir: mualliflar dasturiy muammoni mahsulot topshirilgandan
keyin topish va tuzatish ko'pincha uni talablar va loyihalash bosqichida
topish va tuzatishdan taxminan 100 barobar qimmatga tushishini
ta'kidlaydi [20].

Ushbu raqamni keltirishdan oldin uch holatni hisobga olish zarur.

Birinchidan, mualliflarning o'zlari da'voni yumshatgan. 2001-yilgi tahrirda
ular ro'yxatning 1987-yilgi dastlabki shakliga "ko'pincha" so'zini ataylab
qo'shgan va kichik, kritik bo'lmagan tizimlar uchun nisbat 100:1 emas, 5:1
ga yaqin ekanini alohida qayd etgan [20]. Ya'ni 100 barobarlik ko'rsatkich
universal emas, u yirik va yuqori mas'uliyatli tizimlarga tegishli.

Ikkinchidan, keyingi empirik tadqiqotlar bu effektni tasdiqlamadi.
T. Menzies, W. Nichols, F. Shull va L. Layman 2006–2014-yillarda bajarilgan
171 ta loyiha ma'lumotlarini tahlil qilib, "kechiktirilgan muammo effekti"
ga dalil topmaganlarini e'lon qildi: muammoni kechki bosqichda hal qilishga
sarflangan mehnat uni paydo bo'lishidan ko'p o'tmay hal qilishga sarflangan
mehnatdan izchil yoki sezilarli darajada ko'p bo'lmagan [21]. Mualliflarning
xulosasiga ko'ra, bu effekt barcha loyihalarga xos doimiy qonuniyat emas,
balki ayrim turdagi loyihalarda vaqti-vaqti bilan namoyon bo'ladigan
holatdir [21].

Uchinchidan, da'voning dalil bazasi metodologik tanqidga uchragan.
L. Bossavit o'z tadqiqotida bu ko'rsatkichning cheklangan empirik asosdan
qanday qilib umumiy "o'zgarish narxi egri chizig'i" ga aylanganini va
dastlabki manbalarning talqinida yo'l qo'yilgan noaniqliklarni ko'rsatib
bergan [22].

Shu sababli ushbu ishda 100 barobarlik ko'rsatkich statik tahlilni joriy
etish foydasiga dalil sifatida ishlatilmaydi. Da'vo adabiyotda keng
tarqalgani uchun bu yerda keltirildi, lekin ikkala tomonga ham havola bilan
va bahsli ekani ochiq aytilgan holda.

### Tekshiriladigan iqtisodiy asoslar

100 barobarlik raqamdan voz kechish statik tahlilning iqtisodiy ma'nosini
inkor etmaydi — u shunchaki boshqa, tekshirilishi mumkin bo'lgan asoslarga
tayanishini talab qiladi.

Birinchi asos — aniqlash amalining takrorlanish narxi. Qo'lda kod ko'rigi
har safar muhandis vaqtini talab qiladi va kod bazasi o'sgan sari
qimmatlashadi. Avtomatik tahlilni esa katta hajmdagi kodga va muntazam
ravishda, masalan har bir yig'ishda qayta-qayta qo'llash mumkin [17];
takroriy ishga tushirishning qo'shimcha narxi deyarli nolga teng. Ushbu
ishning amaliy qismida o'lchangan ishga tushirish vaqtlari bu xususiyatni
bevosita ko'rsatadi (3.2-band).

Ikkinchi asos — qamrovning bir xilligi. Avtomatik vosita butun kod bazasini
har safar bir xil mezonlar bilan tekshiradi; qo'lda ko'rikning sifati esa
ko'rikchining tajribasiga, charchoqqa va o'zgarish hajmiga bog'liq.

Uchinchi asos — mehnat taqsimoti. Statik tahlil takrorlanuvchi, shablonli
nuqsonlarni — qattiq kodlangan maxfiy ma'lumotlar, xavfli API chaqiruvlari,
zaif xesh funksiyalari — ishonchli topadi va muhandis vaqtini aynan
avtomatika yetmaydigan masalalarga bo'shatadi. OWASP ta'kidlaganidek, kirish
nazorati mantig'i, autentifikatsiya va kriptografiyaning noto'g'ri qo'llanishi
kabi muammolar avtomatik aniqlash uchun qiyin bo'lib qolmoqda [17]. Demak
to'g'ri nisbat — avtomatik tahlilni birinchi filtr, qo'lda ko'rikni esa
uning o'rnini bosuvchi emas, davomi sifatida qo'llash.

### Yolg'on ijobiy natijalarning narxi

Statik tahlilning asosiy xarajati litsenziya yoki hisoblash resursi emas,
balki har bir ogohlantirishni ko'rib chiqishga sarflanadigan muhandis
vaqtidir. Shu sababli vositaning iqtisodiy samaradorligini belgilovchi
asosiy parametr — yolg'on ijobiy natijalar ulushi.

B. Johnson va hammualliflarining 2013-yilgi tadqiqotida 20 ta ishlab
chiquvchi bilan o'tkazilgan suhbatlar shuni ko'rsatdiki, ishtirokchilar
statik tahlil vositalarining qiymatini tan olsalar-da, yolg'on ijobiy
natijalar va natijalarning taqdim etilish usuli ulardan foydalanishga
to'siq bo'lmoqda [24].

Google kompaniyasida bu muammo miqdoriy mezon ko'rinishiga keltirilgan.
U yerda "samarali yolg'on ijobiy natija" (effective false positive)
tushunchasi qo'llanadi: agar ishlab chiquvchi ogohlantirishni ko'rgandan
keyin hech qanday ijobiy harakat qilmasa, topilma shunday deb hisoblanadi —
vosita texnik jihatdan haq bo'lgan taqdirda ham [23]. Yangi tekshiruvni
platformaga qo'shish uchun uning samarali yolg'on ijobiy natijalar ulushi
10 foizdan kam bo'lishi talab qilinadi, ya'ni ishlab chiquvchi tekshiruv
hech bo'lmaganda o'n holatning to'qqiztasida haqiqiy muammoni
ko'rsatayotganini his qilishi kerak; platforma bo'yicha umumiy ko'rsatkich
5 foizdan biroz pastda turadi [25]. Ishlab chiquvchilar fikrini qaytarish
mexanizmi ham mavjud: topilmani foydasiz deb belgilash tugmasi kuniga
250 marta bosiladi [25].

Bu yondashuvning iqtisodiy mantig'i aniq: vositaning qiymati u topgan
zaifliklar sonida emas, balki shu topilmalarni ko'rib chiqishga ketgan
vaqtga nisbatan o'lchanadi. Aniqlik ko'rsatkichi past vosita ko'p zaiflik
topsa ham, muhandislar unga ishonishni to'xtatgan paytdan boshlab amalda
foydasiz bo'lib qoladi — bu hodisa adabiyotda ogohlantirishlardan charchash
(alert fatigue) deb ataladi va 2.4-bandda batafsil ko'rib chiqiladi.

Aynan shu sababli ushbu ishda vositalar faqat topilmalar soni bo'yicha emas,
Precision, Recall va F1 ko'rsatkichlari bo'yicha ham qiyoslanadi: bu
metrikalar vositaning muhandis vaqtini qanchalik tejashi yoki aksincha
sarflashini bevosita aks ettiradi (2.4- va 3.3-bandlar).

**Xulosa.** Statik tahlilni asoslashda keng tarqalgan 100 barobarlik
ko'rsatkich zamonaviy empirik tadqiqotlarda tasdiqlanmagan va shu sababli
ushbu ishda dalil sifatida ishlatilmaydi. Usulning iqtisodiy ma'nosi boshqa,
tekshiriladigan asoslarda — avtomatik tekshiruvning deyarli bepul
takrorlanishida, qamrovning bir xilligida va muhandis vaqtini avtomatika
yetmaydigan masalalarga bo'shatishida. Bu foydani esa yolg'on ijobiy
natijalar ulushi bevosita kamaytiradi, shuning uchun vositani tanlashda
aniqlik ko'rsatkichi topilmalar sonidan muhimroqdir.
