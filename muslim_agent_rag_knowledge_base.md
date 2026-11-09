# Muslim Agent — RAG Knowledge Base
**Versiya:** 1.0  
**Til:** O‘zbek tili  
**Maqsad:** Muslim Agent foydalanuvchi haqida, uning kasbiy faoliyati, texnologik tajribasi, loyihalari, afzalliklari va agentning texnik tuzilishi haqidagi savollarga kontekstga asoslangan javob berishi uchun bilimlar bazasi.

> Ushbu hujjat RAG (Retrieval-Augmented Generation) tizimiga indekslash uchun tayyorlangan. Undagi ma’lumotlar turli manbalardan yig‘ilgan: foydalanuvchi ilgari bergan ma’lumotlar va yuklangan `main.py` faylida bevosita ko‘rinadigan texnik implementatsiya. Vaqt o‘tishi bilan o‘zgarishi mumkin bo‘lgan ma’lumotlarni doimiy fakt sifatida talqin qilmang.

---

## CHUNK 01 — Shaxsiy va professional profil

**Kategoriya:** `user_profile`  
**Kalit so‘zlar:** Muslimbek Baratov, Muslim, backend developer, mentor, Uzbekistan, IT

Foydalanuvchining ismi Muslimbek Baratov. Unga murojaat qilishda “Muslim” shakli ma’qul. To‘liq ism-sharifi Baratov Muslimbek Alidjon o‘g‘li.

Foydalanuvchi o‘zining oilaviy holati haqida quyidagi ma’lumotni bergan: u uylangan. Bu ma’lumot foydalanuvchi tomonidan o‘zi berilgan bo‘lib, bazada “user-provided” sifatida qayd etiladi.

Muslimbek O‘zbekistonda yashaydi va IT sohasida faoliyat yuritadi. Uning asosiy kasbiy yo‘nalishi backend dasturlash, dasturiy mahsulotlar yaratish, texnik jamoalarda ishlash va mentorlikdir. U O‘zbekiston uchun foydali raqamli platformalar va avtomatlashtirish yechimlarini ishlab chiqishga qiziqadi.

U 2022-yilda Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universitetining Telekommunikatsiya yo‘nalishi bo‘yicha bakalavr bosqichini tamomlagan.

Muslimbek Najot Ta’limda algoritmlar va dasturlash asoslari bo‘yicha dars berish/mentorlik tajribasiga ega bo‘lgan. Sifatdev kompaniyasida Software Engineer va Team Lead sifatida ishlagani, davlat loyihalarida qatnashgani haqida ma’lumot bergan.

**Javob berish qoidasi:** foydalanuvchining aniq lavozimi yoki hozirgi ish joyi so‘ralsa, eski ma’lumotni avtomatik ravishda hozirgi holat deb aytma. Zarur bo‘lsa, ma’lumotning sanasi yoki dolzarbligini aniqlashtir.

---

## CHUNK 02 — Ta’lim va tillar

**Kategoriya:** `education_languages`  
**Kalit so‘zlar:** universitet, bakalavr, telekommunikatsiya, ingliz tili, rus tili

- Oliy ta’lim: Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti.
- Mutaxassislik: Telekommunikatsiya.
- Daraja: bakalavr.
- Bitirgan yil: 2022.
- Ingliz tili darajasi: B2.
- Rus tili darajasi: A2.

Muslimbek odatda texnik va o‘quv mavzularini o‘zbek tilida tushuntirishni afzal ko‘radi. Ruscha yoki inglizcha matn kerak bo‘lsa, alohida so‘rashi mumkin.

---

## CHUNK 03 — Dasturlash va texnologik ko‘nikmalar

**Kategoriya:** `technical_skills`  
**Kalit so‘zlar:** Python, Django, DRF, FastAPI, Flask, Aiogram, PostgreSQL, Redis, Celery, Docker

Muslimbek ishlatgan yoki tajribasi borligini bildirgan texnologiyalar:

### Backend va dasturlash
- Python
- Django
- Django REST Framework (DRF)
- FastAPI
- Flask
- Aiogram 3
- C++
- C#
- JavaScript

### Frontend asoslari
- HTML
- CSS
- JavaScript

### Ma’lumotlar bazalari va qidiruv
- PostgreSQL
- MySQL
- SQLite
- Redis
- ChromaDB
- FAISS

### DevOps va infratuzilma
- Linux
- Docker
- Docker Compose
- Nginx
- Gunicorn
- Uvicorn
- Celery
- Git
- systemd

### Qo‘shimcha vositalar
- Selenium
- Web scraping
- WebSocket
- MoviePy
- FFmpeg
- openpyxl
- xlsxwriter

**Muhim izoh:** ro‘yxat foydalanuvchi ilgari ishlatgan yoki muhokama qilgan texnologiyalarni bildiradi. Har bir texnologiya bo‘yicha ekspertlik darajasi alohida tasdiqlanmagan.

---

## CHUNK 04 — AI, LLM va RAG tajribasi

**Kategoriya:** `ai_llm_rag`  
**Kalit so‘zlar:** LLM, RAG, embeddings, vector database, FAISS, ChromaDB, OpenAI API, Anthropic

Muslimbek LLM asosidagi yordamchilar, hujjatlarni tahlil qilish va semantik qidiruv tizimlari ustida ishlagan yoki prototiplar yaratgan.

U muhokama qilgan texnologiyalar va yondashuvlar:
- Sentence Transformers, jumladan `all-MiniLM-L6-v2`.
- FAISS `IndexFlatL2` orqali vektorlarni qidirish.
- ChromaDB persistent storage.
- OpenAI `text-embedding-3-small` embeddings.
- RAG asosida FAQ assistant yaratish.
- LLM API bilan ishlash.
- Hujjatlardan ma’lumot ajratish, chunking, embedding va retrieval.
- RAG natijalarini LLM kontekstiga qo‘shish.

Oldingi tajribalaridan biri: FAQ ma’lumotlarini ChromaDB bazasiga yuklash va semantik qidiruvga tayyorlash. Shuningdek, `google/flan-t5-base` modelidan CPU muhitida foydalanish va 512 tokenlik kontekst cheklovi bilan bog‘liq masalalarni ko‘rib chiqqan.

Muslimbek OpenAI API va Anthropic API bilan ishlash masalalarini ham muhokama qilgan. API kalitlari, billing yoki quota holati vaqtga bog‘liq bo‘lib, ularni ushbu hujjatdan aniqlab bo‘lmaydi.

### RAG bo‘yicha agentga tavsiya
RAG javobi topilgan kontekstga tayanishi kerak. Agar qidiruv natijasida javob bo‘lmasa:
1. Ma’lumot bazasida bu haqda yetarli ma’lumot yo‘qligini ayt.
2. Taxminni fakt sifatida ko‘rsatma.
3. Zarur bo‘lsa, foydalanuvchidan qo‘shimcha ma’lumot so‘ra.
4. Umumiy bilimdan foydalanilsa, uni bilimlar bazasidan olingan faktlardan ajratib ko‘rsat.

---

## CHUNK 05 — Muslim Agent loyihasining maqsadi

**Kategoriya:** `agent_overview`  
**Kalit so‘zlar:** Muslim Agent, personal AI assistant, terminal agent, Claude, Anthropic

`Muslim Agent` — Python tilida yozilgan terminal orqali ishlaydigan shaxsiy AI agent prototipi. Uning asosiy vazifasi foydalanuvchi bilan tabiiy tilda muloqot qilish, suhbat tarixini saqlash, ayrim fayl amallarini bajarish va foydalanuvchi loyihasining tuzilishini tahlil qilishdir.

Loyiha Anthropic Python SDK orqali Claude Messages API bilan ishlaydi. Model nomi kodda `claude-haiku-5-5` sifatida ko‘rsatilgan. API kaliti `.env` faylidan `ANTHROPIC_API_KEY` nomi bilan olinadi.

Agentning boshlang‘ich system prompt qoidalari:
- Savol va javoblar aniq va tushunarli bo‘lishi.
- O‘zbek tilida javob berish.
- Fayl bilan ishlashda `/read`, `/write`, `/append`, `/ls` buyruqlaridan foydalanish.
- Noma’lum ma’lumotni ochiq aytish.
- Loyiha haqida savol berilsa, loyiha katalogini ko‘rib, muhim fayllar asosida javob berish.

---

## CHUNK 06 — Yuklangan main.py faylida mavjud funksiyalar

**Kategoriya:** `agent_implementation`  
**Manba:** `main.py`  
**Kalit so‘zlar:** MuslimAgent, read_file, write_file, append_file, list_dir, project_context

`main.py` faylida `MuslimAgent` nomli klass mavjud.

### Konstruktor
`__init__()`:
- Anthropic API kaliti mavjudligini tekshiradi.
- `anthropic.Anthropic` client obyektini yaratadi.
- `conversation` nomli bo‘sh suhbat tarixini yaratadi.
- System promptni belgilaydi.

### Fayl yo‘lini aniqlash
`_resolve_path(raw_path)`:
- Berilgan yo‘lni `Path` obyektiga aylantiradi.
- Nisbiy yo‘lni loyiha katalogiga nisbatan yechadi.
- Bo‘sh yo‘l berilsa xatolik chiqaradi.

### Faylni o‘qish
`read_file(file_path)`:
- Fayl mavjudligini tekshiradi.
- Matnni UTF-8 kodlashida o‘qiydi.
- Fayl topilmasa `FileNotFoundError` chiqaradi.

### Fayl yozish
`write_file(file_path, content)`:
- Kerakli ota kataloglarni yaratadi.
- Matnni UTF-8 formatida faylga yozadi.
- Natijada yozilgan fayl yo‘lini qaytaradi.

### Fayl oxiriga matn qo‘shish
`append_file(file_path, content)`:
- Faylni append rejimida ochadi.
- Berilgan matnni fayl oxiriga qo‘shadi.

### Katalog tarkibini ko‘rish
`list_dir(dir_path=".")`:
- Katalog mavjudligini tekshiradi.
- Ichidagi element nomlarini tartiblangan ko‘rinishda qaytaradi.

### Loyiha fayllarini yig‘ish
`collect_project_files(root=None, max_files=30)`:
- Loyiha ichidagi fayllarni rekursiv qidiradi.
- `.git`, `.venv`, `venv`, `__pycache__`, `.idea`, `.mypy_cache`, `.pytest_cache` kataloglarini chetlab o‘tadi.
- Ko‘pi bilan 30 ta fayl nomini yig‘adi.

### Loyiha kontekstini yaratish
`build_project_context()`:
- Loyiha fayllari ro‘yxatini yig‘adi.
- `README.md`, `README`, `main.py`, `requirements.txt`, `pyproject.toml`, `package.json`, `.env.example` kabi muhim fayllarni qidiradi.
- Topilgan fayllarning ayrim qismlarini kontekstga qo‘shadi.
- Yakuniy kontekst hajmini 6000 belgigacha cheklaydi.

### Buyruqlarni qayta ishlash
`process_command(user_input)` quyidagi buyruqlarni qo‘llaydi:
- `/read path` — faylni o‘qish.
- `/write path || content` — faylga yozish.
- `/append path || content` — fayl oxiriga yozuv qo‘shish.
- `/ls [path]` — katalog tarkibini ko‘rish.

### Loyiha haqidagi savolni aniqlash
`should_inspect_project(user_input)` foydalanuvchi savolida loyiha haqida tushuntirish so‘ralayotganini aniqlash uchun inglizcha va o‘zbekcha iboralarni tekshiradi.

### LLM chaqiruvi
`run_inference()` suhbat tarixini Anthropic Messages API ga yuboradi. `display_response()` text turidagi javob bloklarini terminalda chiqaradi.

### Asosiy ish sikli
`run()` foydalanuvchidan terminal orqali xabar oladi, buyruq bo‘lsa bajaradi, loyiha haqida savol bo‘lsa loyiha kontekstini qo‘shadi, boshqa holatda suhbat tarixidan foydalanib modelga so‘rov yuboradi.

---

## CHUNK 07 — Hozirgi agent va RAG o‘rtasidagi farq

**Kategoriya:** `agent_architecture_status`  
**Kalit so‘zlar:** current architecture, RAG integration, conversation memory, retrieval

Yuklangan `main.py` faylida to‘liq RAG pipeline hali ko‘rinmaydi.

Hozirgi kodda:
- `conversation` ro‘yxati suhbat xabarlarini Python xotirasida saqlaydi.
- Loyiha haqida maxsus savol berilganda fayllardan cheklangan hajmda kontekst yig‘iladi.
- Anthropic modeliga system prompt va messages yuboriladi.
- Embedding modeli chaqirilmaydi.
- Vector database yoki persistent knowledge store bilan retrieval amalga oshirilmaydi.
- Chunking, semantic search, top-k retrieval, similarity threshold va reranking implementatsiyasi ko‘rinmaydi.

Demak, `build_project_context()` — bu loyiha fayllaridan kontekst yig‘ish mexanizmi; uni to‘liq RAG deb atash to‘g‘ri emas.

### RAG qo‘shilganda tavsiya etiladigan oqim
1. Bilim manbalarini Markdown, TXT, PDF yoki boshqa qo‘llab-quvvatlanadigan formatda tayyorlash.
2. Matnlarni tozalash va mazmuniy chunklarga ajratish.
3. Har bir chunk uchun metadata saqlash: `source`, `category`, `chunk_id`, `updated_at`.
4. Chunklarni embedding modelidan o‘tkazish.
5. Vektorlarni ChromaDB yoki FAISS kabi vector store ga saqlash.
6. Foydalanuvchi savoli uchun embedding yaratish.
7. Eng mos `top_k` chunklarni qidirish.
8. Keraksiz yoki past o‘xshashlikdagi natijalarni threshold orqali chiqarib tashlash.
9. Topilgan kontekstni Claude promptiga qo‘shish.
10. Javobni faqat topilgan dalillarga tayangan holda shakllantirish.

Bu tavsiya etilgan arxitektura; u yuklangan `main.py` faylida allaqachon mavjud deb talqin qilinmasin.

---

## CHUNK 08 — Muslimbekning asosiy loyihalari

**Kategoriya:** `user_projects`  
**Kalit so‘zlar:** Legal Bridge, Tanlov AI, MaterialAI, E-Bridge, HR platform, FAQ assistant

Muslimbek ilgari quyidagi loyiha va g‘oyalarni muhokama qilgan yoki ular ustida ishlagan:

### Legal Bridge
Shartnomalarni LLM va RAG yordamida tahlil qilishga mo‘ljallangan yechim. Maqsad — hujjat matnini tekshirish, xatolarni aniqlash, huquqiy yoki biznes xavflarini ajratib ko‘rsatish va foydalanuvchiga tahliliy natija berish.

### Tanlov AI
Tender yoki tanlov jarayonlarini AI yordamida tahlil qilish g‘oyasi. Muhokama qilingan imkoniyatlar qatoriga tender ma’lumotlarini tekshirish va nomzodlarni saralash/ranking qilish kiradi. ChatGPT API bilan integratsiya haqida ham gaplashilgan.

### MaterialAI
Qurilish loyihalarida material hajmlarini prognoz qilish g‘oyasi. Random Forest Regression yordamida beton hajmi (m³), armatura (kg), sement, qum va shag‘al miqdorini baholash ko‘zda tutilgan. Kutilgan maqsad — ortiqcha yoki kam baholash xatolarini kamaytirish. Bu natijalar loyiha maqsadi sifatida aytilgan, amalda erishilgan natija sifatida ko‘rsatilmasin.

### E-Bridge va raqamlashtirish
Ko‘prikqurilish AJ faoliyatidagi raqamlashtirish tashabbuslari, jumladan E-Bridge, E-Xodim, HRM va E-Ombor kabi tizimlar muhokama qilingan. Muslimbek raqamlashtirish bo‘limidagi ish faoliyati haqida ma’lumot bergan.

### FAQ RAG assistant
FAQ savol-javoblarini embedding va vector database yordamida qidirish, so‘ng LLM orqali javob shakllantirishga qaratilgan loyiha.

**Javob berish qoidasi:** loyihalarning holati, ishlab chiqarishga chiqarilgani, foydalanuvchilar soni yoki moliyaviy natijalari haqida hujjatda dalil yo‘q. Bunday ma’lumotlarni to‘qib chiqarmaslik kerak.

---

## CHUNK 09 — Ilmiy tadqiqot va ko‘priklar seysmik xavfsizligi

**Kategoriya:** `research_bridge_seismic`  
**Kalit so‘zlar:** doktorantura, seysmik barqarorlik, ko‘prik, elastomer tayanch, rubber bearing, CSiBridge

Muslimbek seysmik xavfsizlik va ko‘prik konstruksiyalari yo‘nalishida doktorantura tadqiqoti olib borishi haqida ma’lumot bergan.

Dissertatsiya mavzusining inglizcha nomi:

“Investigation of the Seismic Resistance of Widely Distributed Highway Bridges with Rubber Bearing Supports Under Seismic Excitations of Varying Intensity (Case Study of Infrastructure Facilities in the Republic of Uzbekistan)”.

Tadqiqotning asosiy yo‘nalishi — O‘zbekiston infratuzilmasidagi avtomobil yo‘llari ko‘priklarining rezina-elastomer tayanchlar bilan jihozlangan holatida turli intensivlikdagi seysmik ta’sirlarga qarshiligini o‘rganish.

Muhokama qilingan ilmiy masalalar:
- Elastomer tayanchlarning ishlash prinsipi.
- Tayanchlarning bog‘langan (bonded) va bog‘lanmagan (unbonded) konstruktiv yechimlari.
- Seysmik ta’sir ostida ko‘prik ustki qurilmasining siljishi.
- Ko‘prik tayanchlari va oraliq qurilmalarining o‘zaro ta’siri.
- Seysmik hisoblash usullari, jumladan spektral va to‘g‘ridan-to‘g‘ri dinamik usullar.
- Turli mamlakatlardagi ko‘prik shikastlanishlari va zilzila tajribasi.
- CSiBridge dasturida hisobiy model yaratish.

### Muhokama qilingan model parametrlari
- Umumiy uzunlik: 48 m.
- Oraliqlar soni: 2 ta.
- Har bir oraliq: 24 m.
- Ko‘prik eni: 7.2 m.
- Qatnov qismi/plita qalinligi sifatida berilgan qiymat: 10 (birligi va o‘lchov talqini alohida tekshirilishi kerak).
- Beton sinfi: B30.
- Armatura: A500.
- Rubber Bearing: mavjud.
- Dastur: CSiBridge 26.

**Javob berish qoidasi:** ilmiy savollarda terminologiyani aniq ishlat. Manba ko‘rsatmasdan standart, formula, me’yoriy talab yoki tajriba natijasini uydirma. Model parametrlaridagi o‘lchov birligi noaniq bo‘lsa, aniqlashtir.

---

## CHUNK 10 — Ta’lim va mentorlik faoliyati

**Kategoriya:** `teaching_mentoring`  
**Kalit so‘zlar:** mentor, Foundation, Back-end, algoritm, 3-Renessans IT Academy

Muslimbek dasturlashni o‘rgatish va o‘quv dasturlari tuzish bilan shug‘ullangan. U Najot Ta’limda algoritmlar va dasturlash asoslari bo‘yicha mentorlik tajribasini tilga olgan.

3-Renessans IT Academy uchun quyidagi kurslar va o‘quv yo‘nalishlari muhokama qilingan:
- Foundation
- Front-end
- Back-end
- Kompyuter savodxonligi
- Olimpiadaga tayyorlash

Foundation kursi dasturi 2 oy va 24 dars shaklida muhokama qilingan, keyinchalik Foundation Pro uchun 25 darslik reja haqida so‘ralgan. Shuningdek, o‘quvchilar uchun loyiha, oraliq test va ERD tayyorlash masalalari ko‘rilgan.

---

## CHUNK 11 — Ish uslubi va javob berish afzalliklari

**Kategoriya:** `response_preferences`  
**Kalit so‘zlar:** Uzbek language, step-by-step, code examples, technical explanation

Agent quyidagi muloqot uslubiga amal qilishi kerak:

1. Asosiy til — o‘zbek tili.
2. Javob aniq, tushunarli va amaliy bo‘lsin.
3. Texnik savollarda bosqichma-bosqich tushuntirish ber.
4. Kod so‘ralganda, imkon qadar to‘liq ishlaydigan misol taqdim et.
5. Koddagi muhim qismlarning vazifasini tushuntir.
6. Xatolik tahlilida traceback yoki logdagi aniq sababni ajrat.
7. Taxminni fakt sifatida ko‘rsatma.
8. Zarur bo‘lsa, foydalanuvchidan bitta aniq savol so‘ra.
9. Tarjima so‘ralganda, asl mazmun va terminologiyani saqla.
10. Ilmiy matnda rasmiy-akademik uslub, dasturlashda esa amaliy va texnik uslubdan foydalan.

---

## CHUNK 12 — Agent uchun ishonchlilik va maxfiylik qoidalari

**Kategoriya:** `agent_policy`  
**Kalit so‘zlar:** grounding, hallucination, privacy, source attribution, confidence

Muslim Agent quyidagi qoidalarga rioya qilishi kerak:

- RAG orqali topilgan ma’lumotni manbasi bilan bog‘la.
- Retrieval natijasida topilmagan shaxsiy ma’lumotni o‘zingdan to‘qima.
- Bir-biriga zid ma’lumotlar topilsa, ziddiyatni yashirma; manbalar va sanalarni ko‘rsat.
- Vaqtga bog‘liq ma’lumotni “oldingi suhbatlarda aytilgan” deb belgilash mumkin.
- API kalitlari, parollar, tokenlar, maxfiy konfiguratsiyalarni bilimlar bazasiga joylama.
- Shaxsiy ma’lumotni faqat savolga javob berish uchun zarur bo‘lgan darajada ishlat.
- Foydalanuvchi haqida so‘ralmagan nozik yoki aloqasiz tafsilotlarni javobga kiritma.
- Hujjatda yo‘q bo‘lgan aniq sana, raqam, natija, lavozim yoki loyiha holatini uydirma.
- RAG konteksti yetarli bo‘lmasa, “Menda bu haqda yetarli ma’lumot yo‘q” deb ayt.

---

## CHUNK 13 — RAG metadata namunasi

**Kategoriya:** `rag_metadata_schema`  
**Kalit so‘zlar:** metadata, chunk, source, category, vector database

Har bir chunkni vector database ga quyidagi metadata bilan yozish tavsiya etiladi:

```json
{
  "chunk_id": "user_profile_001",
  "source": "muslim_agent_knowledge_base.md",
  "category": "user_profile",
  "language": "uz",
  "version": "1.0",
  "updated_at": "2026-11-09",
  "confidence": "user-provided"
}
```

Tavsiya etiladigan metadata maydonlari:
- `chunk_id`: chunk uchun yagona identifikator.
- `source`: ma’lumot olingan fayl yoki manba.
- `category`: ma’lumot turi.
- `language`: matn tili.
- `version`: bilimlar bazasi versiyasi.
- `updated_at`: oxirgi yangilangan sana.
- `confidence`: `user-provided`, `source-code`, `inferred` kabi kelib chiqish belgisi.

---

## CHUNK 14 — Agent o‘zini qanday tanishtirishi kerak?

**Kategoriya:** `agent_identity`  
**Kalit so‘zlar:** agent identity, introduction, Muslim Agent

Agar foydalanuvchi “Sen kimsan?” yoki “O‘zingni tanishtir” deb so‘rasa, agent quyidagi mazmunda javob berishi mumkin:

“Men Muslim Agent — Muslimbek uchun ishlab chiqilayotgan shaxsiy AI yordamchiman. Vazifam savollarga o‘zbek tilida aniq javob berish, dasturlash va texnologik masalalarda yordam berish, loyiha fayllarini tahlil qilish hamda bilimlar bazasidan tegishli ma’lumotlarni topishdir. Men Anthropic Claude API bilan ishlaydigan Python agenti sifatida boshlanganman. RAG integratsiyasi orqali Muslimbek haqidagi tasdiqlangan ma’lumotlar, loyihalar va texnik hujjatlardan kontekst topib javob berishim mumkin. Bilmagan narsamni taxmin qilib aytmayman.”

---

## Yakuniy eslatma

Ushbu hujjat boshlang‘ich RAG knowledge base hisoblanadi. Yangi loyiha, ish joyi, texnik stack, dissertatsiya natijalari yoki shaxsiy afzalliklar o‘zgarganda tegishli chunkni yangilash kerak. RAG bazasiga `.env`, API key, parol, SSH private key yoki boshqa maxfiy fayllarni qo‘shmang.
