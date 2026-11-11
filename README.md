# Portofolio — Fathir Atha Rizki Tasril

Website portofolio pribadi, dibangun murni pakai HTML & CSS (tanpa framework, tanpa JavaScript). Isinya tentang perkenalan aku, skill teknis yang aku kuasai, pengalaman organisasi, sampai testimoni dari orang-orang yang pernah kerja bareng aku.

---

## Fitur

- **Sticky header** dengan efek blur (`backdrop-filter`) yang nempel di atas saat di-scroll, dengan link navigasi ke tiap section (`#profile`, `#skills`, `#experience`, `#contact`) plus efek underline glow merah saat di-hover.
- **Hero / About section** — nama & identitas dengan animasi 3D flip sekali muncul (`flip3D`), foto profil dengan efek "lampu" blur merah di belakangnya yang menyala lebih terang saat di-hover (`lampGlow`), serta info NPM dan program studi dalam bentuk `<dl>`.
- **Skills section** — daftar tech stack ditampilkan sebagai _logo marquee_ yang bergeser otomatis tanpa henti (infinite scroll pakai `@keyframes`), dengan efek fade transparan di kedua ujung (`mask-image`) dan otomatis berhenti saat kursor diarahkan ke situ.
- **Experience section** — 4 kartu pengalaman organisasi/kepanitiaan, masing-masing punya _mini image slider_ 3 foto yang bergantian otomatis tiap beberapa detik (`expSlide`), lengkap dengan badge status (Active Member/Volunteer) dan deskripsi peran.
- **Contact section** — dua kolom: kiri berisi daftar testimoni/peer review (scrollable, dengan custom scrollbar merah gelap), kanan berisi ajakan kolaborasi dan tombol ikon bulat menuju GitHub, LinkedIn, dan email.
- **Fully responsive** — grid hero berubah jadi satu kolom di bawah 600px, sedangkan grid experience dan contact berubah jadi satu kolom di bawah 768px.

## Tech Stack

- HTML5 semantic markup
- CSS3 (custom properties/CSS variables, Grid, Flexbox, keyframe animation, `mask-image`)
- Google Fonts — _Space Grotesk_
- Tanpa JavaScript, tanpa build tool, tanpa framework

## Struktur Proyek

```
├── templates
|   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
│       ├── poto.jpg
│       ├── javascript-original.svg, python-original.svg, html5-original.svg, ...
│       ├── google12.png, kantorGoogle.jpg, Google.jpg
│       ├── Compest 18 1.jpeg, Compest 18 2.jpeg, Compest 18 3.jpeg
│       ├── Speaker (1).jpeg, acasia.jpg
│       └── Forkoma.jpg, Forkoma 2.jpg, Forkoma 3.jpg
└── README.md
```

## Cara Menjalankan

Karena ini murni HTML/CSS statis, nggak perlu install dependency apa pun.

1. Clone repo ini
   ```bash
   git clone <url-repo-kamu>
   cd <nama-folder>
   ```
2. Pastikan folder `static/img/` sudah berisi semua asset gambar yang dipakai di `index.html` (foto profil, logo skill, dan foto-foto experience).
3. Buka `index.html` langsung di browser, **atau** jalankan local server biar path relatif jalan dengan benar:
   ```bash
   npx serve .
   # atau
   python3 -m http.server
   ```
4. Akses di `http://localhost:<port>`.

## Progress Pengerjaan

Hari 1

Sesi pagi — Setup struktur HTML dasar (header/nav, section profile, skills, experience, contact) dan nentuin color palette dark-red theme (--paper, --accent, --accent-dark). Commit awal: kerangka halaman masih polos, belum ada styling detail. Sesi siang — Bangun hero section: grid 2 kolom (identity, photo, details), styling avatar foto beserta efek glow merah di belakangnya (photo-block + animasi lampGlow saat di-hover), lanjut styling navbar sticky dengan efek blur (backdrop-filter) dan underline glow di tiap link saat di-hover. Sesi sore — Bangun Skills section: slider logo tech stack yang bergeser otomatis tanpa henti, termasuk benerin loop-nya biar mulus (dua set logo digandakan) dan efek fade transparan di kedua ujung pakai mask-image. Sesi malam — Bangun Experience section: grid 2 kolom untuk kartu pengalaman, bikin mini image slider otomatis di tiap kartu (exp-slider-track), isi konten 4 pengalaman (GDG UI, COMPFEST 18, Acasia Campus Expo, Forkoma UI Banten), sekaligus iterasi timing animasi slider gambarnya biar nggak kepotong-potong.

Hari 2

Sesi pagi — Bangun Contact section: kolom kiri untuk daftar peer review/testimoni (scrollable dengan custom scrollbar merah gelap), kolom kanan untuk ajakan kolaborasi dan tombol ikon sosial (GitHub, LinkedIn, Email). Sesi siang — Kejar isu responsive: pasang breakpoint 600px untuk hero-grid dan 768px untuk experience-grid & contact-grid, testing di beberapa ukuran layar. Sesi sore–malam — Polishing keseluruhan: rapihin CSS variable biar konsisten antar section, cek alt text & aria-label buat aksesibilitas dasar, final review sebelum commit terakhir sebelum deploy.

## Pertanyaan Reflektif

### Tugas 1

1. Iya, aku pakai elemen semantik HTML5, tapi nggak semua jenis semantik aku pakai. Struktur utama halaman ini terdiri dari `<header>` untuk navbar, `<main>` sebagai pembungkus konten inti, empat buah `<section>` (profile, skills, experience, contact), `<nav>` untuk menu, dan `<footer>`. Aku pilih `<section>` karena tiap bagian ini memang punya topik dan tujuan yang jelas berbeda satu sama lain, dan masing-masing dirujuk lewat anchor id (`#profile`, `#skills`, dst) yang dipakai navbar — jadi bukan cuma soal "kelihatan semantik", tapi memang fungsional buat navigasi.

   Yang nggak aku pakai adalah `<article>` dan `<aside>`. Sebenarnya kartu experience di section Experience itu kandidat kuat buat jadi `<article>` — tiap kartu punya judul, gambar, badge, dan deskripsi yang secara konten bisa berdiri sendiri kalau dipisah dari halaman (mirip entri blog/portofolio proyek). Aku akui ini titik lemah struktur HTML aku: idealnya kartu experience dan mungkin kartu testimoni di Contact section pakai `<article>`, bukan cuma `<div class="skill-card exp-card">`. Untuk `<aside>`, aku memang nggak pakai karena nggak ada konten tangensial/pelengkap semacam sidebar di halaman ini — semua yang tampil adalah konten inti portofolio, jadi maksa masukin `<aside>` justru nggak akan merepresentasikan isi dengan tepat.

2. Tantangan responsive terbesarku justru bukan di grid utama, tapi di **navbar**. Menu navigasi aku posisikan `position: absolute` dan di-center pakai `left: 50%; transform: translateX(-50%)` supaya persis di tengah header. Ini enak dilihat di layar lebar, tapi begitu aku evaluasi dengan resize browser pelan-pelan dari lebar penuh ke ukuran HP, ternyata navbar ini yang paling duluan "pecah" — di layar sempit, brand name, menu yang di-center absolute, dan potensi elemen lain gampang bertabrakan atau overflow, dan sejauh ini aku belum menaruh media query khusus untuk navbar itu sendiri (beda dengan `.hero-grid`, `.experience-grid`, dan `.contact-grid` yang masing-masing sudah aku kasih breakpoint).

   Cara aku evaluasi elemen mana yang harus diprioritaskan: aku cek satu per satu section dari lebar penuh sampai ~360px sambil mencatat di lebar berapa layout mulai terlihat rusak. Hasilnya, breakpoint yang sudah aku pasang juga nggak konsisten — `.hero-grid` berubah jadi satu kolom di `600px`, sementara `.experience-grid` dan `.contact-grid` baru berubah di `768px`. Untuk iterasi berikutnya, dua hal yang paling perlu aku benerin: (1) tambahin breakpoint khusus untuk header/nav (kemungkinan diubah jadi hamburger menu atau menu yang di-stack), dan (2) menyamakan angka breakpoint di semua section supaya transisi antar section di ukuran layar menengah (misalnya tablet, 600–768px) nggak terasa lompat-lompat.

3. Karena ini static web murni tanpa server-side apa pun, keterbatasan yang paling terasa ada di dua hal: pertama, form kontak beneran nggak ada — satu-satunya jalur kontak langsung cuma lewat `mailto:` di tombol email, jadi pengunjung harus keluar dari halaman dan buka aplikasi email mereka sendiri, nggak ada validasi ataupun konfirmasi pengiriman pesan di halaman itu sendiri. Kedua, semua konten — bio, daftar skill, daftar pengalaman organisasi, bahkan testimoni dari orang lain — itu hardcoded langsung di `index.html`. Setiap kali ada pengalaman baru atau testimoni baru yang mau ditambahkan, aku harus buka dan edit HTML-nya lagi, lalu re-deploy, nggak ada cara mengubah konten tanpa menyentuh kode. Ini juga berarti data testimoni yang ditampilkan nggak bisa diverifikasi atau diperbarui secara independen dari pemilik website.

   Untuk iterasi selanjutnya, dua fungsionalitas dinamis yang paling ingin aku siapkan: (1) form kontak fungsional (misalnya lewat layanan seperti Formspree, atau backend kecil sendiri) supaya pengunjung bisa langsung mengirim pesan tanpa pindah aplikasi, dan (2) daftar experience serta testimoni yang datanya diambil dari file data terpisah (JSON) atau headless CMS ringan, supaya menambah pengalaman atau testimoni baru nggak perlu mengubah struktur HTML setiap kali, dan idealnya ke depan testimoni bisa dikonfirmasi/di-submit langsung oleh yang bersangkutan, bukan sekadar teks yang aku tempel manual.

## AI Disclosure

Aku pakai AI (ChatGPT/Claude) sebagai _pair programmer_, terutama di tahap drafting awal untuk bagian-bagian yang butuh eksperimen animasi CSS — bukan buat generate satu website jadi sekali klik.

**Bagian yang dibantu AI:**

- Ide struktur awal grid 2 kolom untuk hero section (`hero-identity`, `hero-photo`, `hero-details`)
- Draft pertama logika _infinite scroll marquee_ untuk slider logo tech stack di Skills section
- Saran pendekatan slider gambar otomatis di tiap kartu Experience (`exp-slider-track`) dan efek glow di belakang foto profil (`photo-block` + `lampGlow`)
- Penyusunan kalimat di README ini sendiri — poin-poin dan progres di atas aku yang menentukan, tapi AI bantu merapikan cara penyampaiannya biar sesuai struktur bacaan

**Bagian yang aku kerjain/perbaiki manual:**

- **Loop marquee tanpa "patah"** — draft awal AI untuk slider logo cuma satu set logo dengan `translateX` sampai habis, jadi keliatan jeda/lompatan pas animasi mengulang dari awal. Aku ubah sendiri jadi dua set logo yang sama ditaruh berurutan dengan `width: max-content`, terus animasi cuma geser sampai `-50%`, jadi looping-nya mulus tanpa keliatan sambungannya.
- **Timing slider foto Experience** — versi awal `@keyframes expSlide` dari AI transisinya kepotong-potong (langsung ganti gambar tanpa jeda "diam" buat dilihat). Aku hitung ulang persentasenya sendiri (misalnya `0%–28%` diam di gambar 1, baru geser di `33%–61%`) supaya tiap foto ada waktu cukup buat dilihat sebelum gonta-ganti.
- **Efek glow foto profil** — nilai `blur()`, `opacity`, dan `box-shadow` di `lampGlow` hasil AI awalnya kelihatan terlalu flat/statis pas di-hover. Aku iterasi manual kombinasi blur–opacity–scale-nya biar efeknya lebih hidup.
- **Konsistensi visual** — nilai warna, radius, dan shadow yang disaranin AI awalnya nggak konsisten antar section (beda-beda opacity shadow di skill-card, exp-card, dan contact-card). Aku rapiin sebagian jadi CSS variables (`--accent`, `--accent-dark`, `--line`, `--radius`) biar ada satu sumber kebenaran, meskipun aku sadar belum semua nilai warna di file ini konsisten pakai variable (masih ada beberapa hex value ditulis langsung di rule tertentu).
- **Aksesibilitas dasar** — nambahin `alt` text deskriptif di tiap `<img>` (termasuk gambar-gambar di slider Experience) dan `aria-label` di social icon button, yang di draft awal AI kosong atau generic.

---

# tugas 2

# pertanyaan refleksif

1. Alurnya kira-kira gini: begitu user ngetik URL atau klik link ke halaman portofolio baru, request itu pertama kali nyampe ke urls.py proyek (root URLconf). Tugas dia di sini cuma jadi "resepsionis" — dia cek prefix path-nya, terus kalau cocok, dia include() request itu ke urls.py punya aplikasi yang relevan, bukan langsung nentuin view. Nah, urls.py aplikasi ini yang lebih spesifik mecah path sampai ke akhir dan nyocokinnya ke satu view tertentu. Sampai di view, di situlah logic-nya jalan: view manggil model buat ambil data yang dibutuhin (misalnya Portfolio.objects.all() atau .get(id=...)), data hasil query ini biasanya berbentuk queryset/object Python. Data itu terus dibungkus dalam bentuk context (dictionary), lalu view manggil render() sambil nunjuk ke file template mana yang mau dipakai plus context-nya. Di tahap ini, template engine Django gabungin markup HTML yang ada tag {{ }} / {% %} dengan data dari context, jadi satu HTML utuh. Hasil HTML itu yang dikirim balik sebagai HTTP response ke browser, dan browser tinggal render ke layar user. Jadi urutannya: urls.py proyek → urls.py app → view → model (ambil data) → template (gabung data + markup) → balik ke view → response ke browser.

2. Karena kalau data ditulis langsung di template, itu artinya kontennya nge-hardcode di markup — setiap kali ada portofolio baru yang mau ditambah, aku harus buka dan edit file HTML-nya lagi satu-satu, padahal boleh jadi data yang sama juga mau dipakai di halaman lain (misal halaman list & halaman detail). Ini gampang bikin data jadi nggak konsisten dan gampang typo karena diketik manual berkali-kali di tempat berbeda. Kalau datanya disimpan di model, ada satu source of truth — data hidup di database, bukan di markup. Efeknya ke maintainability: nambah/edit/hapus portofolio cukup lewat query atau bahkan admin panel Django, nggak perlu sentuh kode template sama sekali, dan perubahan itu otomatis kereflect ke semua tempat yang manggil data itu. Efeknya ke development: ada pemisahan tanggung jawab yang jelas — yang ngurusin logic/data (model & view) bisa kerja terpisah dari yang ngurusin tampilan (template), jadi lebih gampang di-testing, di-scale (misal portofolionya nambah jadi ratusan), dan divalidasi (tipe data, relasi field, dll dikontrol di level model, bukan ngandelin ketikan manual di HTML).

3. makemigrations itu tugasnya "bikin rencana" — Django bakal bandingin kondisi models.py sekarang sama migration terakhir yang tercatat, terus kalau ada perbedaan (field baru, field dihapus, tipe data berubah, dst), dia generate file migration baru (kode Python) yang isinya instruksi perubahan skema itu. Di tahap ini, database aslinya belum berubah sama sekali, yang ada cuma file instruksi baru nangkring di folder migrations/. migrate itu baru tahap "eksekusi rencana" — perintah ini yang beneran jalanin instruksi dari file-file migration yang belum diterapkan ke database, dalam bentuk SQL kayak ALTER TABLE atau CREATE TABLE. Jadi migrate yang benar-benar mengubah struktur database di level fisik. Contoh konkretnya: misal aku mau nambahin field baru di model Project, katakanlah:

class Project(models.Model):
       ...
       thumbnail_url = models.URLField(blank=True)

Setelah nulis field itu, aku jalanin python manage.py makemigrations — Django bakal generate file baru semacam 0004_project_thumbnail_url.py yang isinya instruksi AddField. Tapi kolom thumbnail_url itu belum ada di database sungguhan sampai aku jalanin python manage.py migrate, baru di situ Django beneran nambahin kolom itu ke tabel Project di database.


## AI Disclosure — Tugas 2

Di tugas ini AI (Gemini/Claude) aku pakai lagi sebagai _pair programmer_, tapi porsinya lebih ke bagian backend Django — beda sama tugas sebelumnya yang fokusnya di eksperimen CSS/animasi.

**Bagian yang kebantu AI:**

- Diskusi awal soal struktur model baru — field apa aja yang relevan dan tipe data yang cocok (`CharField`, `TextField`, `DateField`, dll) buat merepresentasikan bagian portofolio yang aku pilih
- Penjelasan alur `makemigrations` vs `migrate` pas aku masih bingung kapan harus jalanin yang mana setelah ubah model
- Draft awal struktur `view` buat ambil data dari model dan masukin ke `context`, termasuk pola penanganan kondisi data kosong (`{% if %}` / `{% else %}` di template)
- Saran struktur unit test — pembagian tiga skenario (URL & template kepake, data muncul kalau ada, pesan kosong muncul kalau nggak ada) pakai `TestCase` dan `self.client`
- Bantu ngerapiin kalimat di README ini, termasuk jawaban Pertanyaan Reflektif Tugas 2

**Bagian yang aku kerjain/perbaiki manual:**

- **Penentuan field & validasi model** — draft awal AI kadang kasih field yang generic banget (mis. `CharField` semua tanpa `max_length` yang masuk akal atau tanpa mikirin field mana yang wajib/opsional). Aku sesuaikan sendiri field mana yang butuh `blank=True`, `null=True`, atau `max_length` spesifik biar sesuai kebutuhan data asli.
- **Routing & named URL** — AI kasih pola umum buat `urls.py`, tapi penamaan `name=` route, penyesuaian ke `main/urls.py` yang udah ada, dan integrasinya ke navbar pakai `{% url %}` aku sesuaikan sendiri biar konsisten sama halaman lain (nggak numbrek sama nama route experience yang udah ada).
- **Template & empty state** — struktur `{% for %}` dari AI aku sesuaikan lagi ke markup dan class CSS yang udah ada di project (biar tampilannya konsisten sama section lain), termasuk nulis ulang pesan kondisi kosong biar nggak generic ("Belum ada data" polos) tapi sesuai konteks halamannya.
- **Unit test** — kerangka test dari AI aku jalanin, cek satu-satu mana yang gagal, terus benerin sendiri assertion yang kurang tepat (misalnya cek `response.status_code` doang tapi lupa cek `assertTemplateUsed`, atau lupa bikin test case buat kondisi data kosong).
- **Debugging error migrasi** — sempet ada error pas `makemigrations` gara-gara ada field yang aku tambahin belakangan tanpa default value buat baris data yang udah ada; ini aku telusuri dan benerin sendiri (kasih `default=` atau jalanin migrasi tambahan), bukan langsung nyalin solusi dari AI mentah-mentah.

Dalam membuat tugas ini aku masi memvalidasi apakah kode yg aku buat bener atau salah 



# Tugas 3 

## Fitur
- Fungsionalitas CRUD (Create, Read, Update, Delete) — Penambahan fitur untuk menambah, melihat, mengubah, dan menghapus entri pengalaman (Experience) dan organisasi (Organization) secara dinamis tanpa perlu mengubah file HTML secara manual.

- Data Delivery API — Menyediakan endpoint (URL routing) untuk mengembalikan data portofolio dalam format JSON dan XML, yang bisa diakses secara terpisah oleh klien atau dites menggunakan Postman.
   
- Django Forms dengan Validasi — Penggunaan form bawaan Django untuk menangani input user secara aman (termasuk validasi tipe data) baik saat pembuatan data baru maupun pengeditan data.

- Keamanan Data (UUID & CSRF) — Penggunaan UUID (Universally Unique Identifier) sebagai primary key untuk mengamankan ID objek agar tidak mudah ditebak, serta proteksi CSRF pada setiap form pengiriman data.

- Interactive Modals — Penggunaan modal HTML/CSS khusus untuk konfirmasi penghapusan data (experience_delete_modal.html, organization_delete_modal.html) demi mencegah data terhapus secara tidak sengaja.

## Tech Stack
- Backend / Web Framework: Django (Python)
- Database: SQLite3 (db.sqlite3)
- Frontend: HTML5, CSS3, Django Templates
- Data Formats: JSON, XML
- Testing API: Postman

## Strukutur proyek yang baru
myportofolio/
├── main/
├── organization_images/
├── portofolio/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── static/
├── staticfiles/
├── templates/
│   ├── components/
│   │   ├── experience_delete_modal.html
│   │   └── organization_delete_modal.html
│   ├── base.html
│   ├── experience_edit_form.html
│   ├── experience_form.html
│   ├── experience.html
│   ├── index.html
│   ├── organization_edit_form.html
│   ├── organization_form.html
│   └── organization.html
├── .env
├── .env.prod
├── .gitignore
├── db.sqlite3
├── experience.json
├── manage.py
├── README.md
└── requirements.txt

# Progres Pengerjaan
Hari 1
- Sesi Pagi — Melakukan migrasi database untuk mengubah Primary Key model menjadi UUID. Bikin forms.py menggunakan ModelForm dari Django agar form input HTML tidak perlu dibuat manual satu-satu.

- Sesi Siang — Menyusun views.py untuk fungsionalitas Create dan Read. Membangun kerangka HTML form (experience_form.html, organization_form.html) yang memanfaatkan tag {{ form.as_p }} beserta token CSRF.Sesi Malam — Mengerjakan routing di urls.py dan menyesuaikan tautan tombol di halaman utama agar bisa mengarahkan user ke halaman pembuatan entri baru.

Hari 2
- Sesi Pagi — Membangun fungsionalitas Update dan Delete. Menulis logika untuk mengambil instance data spesifik berdasarkan UUID di views, lalu melemparnya kembali ke dalam form edit (experience_edit_form.html, organization_edit_form.html).

- Sesi Siang — Merancang dan styling modal konfirmasi hapus (_delete_modal.html) di folder components/ agar user experience lebih baik, alih-alih langsung menghapus data saat tombol di-klik.
Sesi Malam — Uji coba CRUD secara menyeluruh via browser. Melakukan debugging pada isu saat data di-update namun field tertentu menjadi kosong.

Hari 3
- Sesi Pagi — Mengerjakan fitur Data Delivery. Membuat fungsi di views.py yang me-return HttpResponse dengan menyematkan serializers dari Django untuk mengubah data QuerySet menjadi format XML dan JSON.

- Sesi Siang — Mengonfigurasi path URL baru (/xml/, /json/, /xml/[id]/, /json/[id]/) dan melakukan testing endpoint menggunakan Postman untuk memastikan response datanya valid. Mem-backup data format .json untuk referensi eksternal (experience.json).

- Sesi Malam — Finalisasi kode, merapikan struktur folder template, dan menulis pelaporan README.md untuk tugas 3 ini.

## Pertanyaan Reflektif

Q1:
Jelaskan mengapa kita menggunakan ModelForm Django alih-alih membuat formulir HTML secara manual. Selain itu, jelaskan mengapa kita harus menambahkan {% csrf_token %} pada formulir-formulir tersebut!
A1:
Menurut saya, cara itu jauh lebih praktis. Menulis kode HTML secara manual merupakan proses yang repetitif, sedangkan data dari Django sudah melalui proses validasi yang lebih baik.

Q2:
Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan dengan XML?
A1:
Saya perlu melakukan pencarian di Google untuk hal ini dan membandingkannya dengan pengetahuan saya. Sejauh pemahaman saya, JSON jauh lebih sederhana untuk digunakan.

Q3:
Jelaskan alur yang terjadi saat Anda menggunakan fungsi *view* untuk mengembalikan data portofolio dalam format JSON. Mengapa kita perlu melakukan proses serialisasi pada model Django sebelum mengembalikan data tersebut?
A3:
Klien mengirimkan permintaan ke `views.py`, lalu basis data memberikan respons. (sejujurnya, saya masih berusaha memahaminya)

## AI Disclosure
Bagian yang dibantu AI:

- Mendiskusikan best practices perbandingan antara auto-increment ID standar vs UUID pada model Django, yang akhirnya memutuskan aku pakai UUID.
- Membantu menjelaskan cara kerja serializers.serialize() di Django ketika aku stuck mencari cara merubah QuerySet menjadi format XML/JSON tanpa harus me-loop manual datanya.
- Memberikan snippet cara menangkap UUID melalui endpoint di urls.py (<uuid:id>)
- Menyunting draft progres pengerjaan harian agar lebih sistematis dan mudah dibaca.

## Bagian yang aku kerjain/perbaiki manual:

- Pembuatan form & Modals — Integrasi antara Django Forms dengan layout CSS/HTML custom yang sudah kubuat di tugas 1 (seperti form input dan delete modal) kuatur manual, tidak menggunakan template bawaan AI yang biasanya memakai bootstrap.

- Logika View & Error Handling — Logika pada views saat mengembalikan object atau 404 (via get_object_or_404), serta cara menyuntikkan id ke masing-masing tombol edit/hapus pada iterasi data di template.

- Testing via Postman — Instalasi, eksekusi request URL (GET ke endpoint /xml dan /json), dan verifikasi bahwa data yang aku input tampil dengan akurat aku tes sendiri secara lokal.



# Tugas 4

## Fitur

- **Sistem Otorisasi Berbasis Peran (Role-Based Authorization)** — Menerapkan 4 tingkat hak akses (Pengunjung tanpa login, Pengguna biasa, Editor, Pemilik portofolio/superuser) yang membatasi siapa yang boleh membaca, memberi *star*, mengubah, atau menghapus data Experience dan Organization.

- **Peran Editor via Django Group & Permission** — Membuat *Group* "Editor" lewat *data migration* Django yang otomatis diberi *permission* `change_experience` dan `change_organization` saja (tanpa `add_*`/`delete_*`), sehingga Editor bisa mengubah data tapi tidak bisa membuat atau menghapusnya. Penetapan user ke dalam grup ini dilakukan lewat Django Admin.

- **Proteksi Server-Side (bukan sekadar UI)** — Setiap *view* yang mengubah data (create/update/delete) dilindungi dua lapis: `@login_required` untuk mengarahkan pengunjung yang belum login ke halaman `/login/`, dan pengecekan *permission* (`can_edit_data`, `can_create_or_delete_data`) yang melempar `PermissionDenied` (403 Forbidden) kalau user sudah login tapi tidak punya hak.

- **Context Processor Kustom** — Membuat `main/context_processors.py` yang menyuntikkan variabel `is_editor` ke *semua* template secara global (mirip cara Django menyuntikkan `user` lewat *auth context processor*), supaya template bisa menampilkan/menyembunyikan tombol tanpa perlu mengirim variabel itu manual di tiap `view`.

- **UI Adaptif per Peran** — Tombol "Tambah" hanya muncul untuk superuser, tombol "Edit" muncul untuk superuser *dan* Editor, tombol "Hapus" hanya untuk superuser, sementara tombol *Star* tetap terlihat untuk siapa pun (tapi memaksa login kalau diklik saat belum login). Navbar juga menampilkan label peran (`Owner`/`Editor`/`User`) di samping username untuk memudahkan pengujian manual.

- **Fitur Star yang Sudah Ada Sejak Tutorial 4 Diverifikasi Ulang** — Relasi `ManyToManyField` ke model `User` (`starred_by`) pada `Experience` dan `Organization`, beserta *view* `toggle_star` (POST + `{% csrf_token %}`) yang membatasi maksimal satu *star* per pengguna dan menampilkan jumlah total *star*, sudah ada dari implementasi Tutorial 4 dan dipastikan tetap berfungsi normal setelah penambahan sistem peran.

- **Keamanan Endpoint API** — Endpoint `/api/experience/` dan `/api/organization/` tetap publik (bisa dibaca tanpa login), tapi memakai `use_natural_foreign_keys=True` supaya relasi `starred_by` tampil sebagai *username*, bukan *id* database mentah — mencegah kebocoran informasi internal.

## Tech Stack

Tidak ada penambahan *dependency* baru di tugas ini — tetap menggunakan Django (Python) dan SQLite3 seperti Tugas 3, ditambah pemanfaatan modul bawaan `django.contrib.auth` (`Group`, `Permission`) untuk sistem otorisasi.

## Struktur Proyek yang Diperbarui

myportofolio/
├── main/
│ ├── migrations/
│ │ ├── 0001_initial.py
│ │ ├── 0002_experience_starred_by_organization_starred_by.py
│ │ └── 0003_create_editor_group.py # BARU — data migration Group Editor
│ ├── context_processors.py # BARU — expose is_editor ke semua template
│ ├── admin.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py # DIUBAH — helper role-check & permission guard
├── portofolio/
│ └── settings.py # DIUBAH — daftarkan context processor baru
├── templates/
│ ├── base.html # DIUBAH — badge peran di navbar
│ ├── experience.html # DIUBAH — visibility tombol per peran
│ └── organization.html # DIUBAH — visibility tombol per peran
└── ...


## Progres Pengerjaan

**Hari 1**

- Sesi Pagi — Menganalisis ulang target tugas dan memetakan matriks hak akses 4 peran (baca, *star*, ubah, buat/hapus) ke dalam kebutuhan teknis: siapa butuh `login_required`, siapa butuh pengecekan *permission* tambahan.
- Sesi Siang — Membuat `main/context_processors.py` untuk *flag* `is_editor`, mendaftarkannya di `TEMPLATES['OPTIONS']['context_processors']` pada `settings.py`, dan menulis *data migration* `0003_create_editor_group.py` yang membuat *Group* "Editor" beserta *permission*-nya secara otomatis saat `migrate` dijalankan.
- Sesi Sore — Menulis tiga fungsi *helper* di `views.py` (`is_editor_user`, `can_edit_data`, `can_create_or_delete_data`) dan menerapkannya ke enam *view*: `add_experience`, `edit_experience`, `delete_experience`, `add_organization`, `edit_organization`, `delete_organization`.

**Hari 2**

- Sesi Pagi — Mengubah `experience.html`, `organization.html`, dan `base.html` supaya tombol Edit/Tambah/Hapus dan badge peran di navbar menyesuaikan status login dan grup pengguna.
- Sesi Siang — Menjalankan `python manage.py migrate` untuk menerapkan *migration* Editor, membuat beberapa akun uji (pengguna biasa, editor, superuser) lewat `/register/` dan Django Admin (`/admin/`), lalu menetapkan salah satu akun ke Group "Editor".
- Sesi Sore — Melakukan pengujian manual menyeluruh untuk **keempat peran** secara bergantian (mode Incognito untuk tiap akun): mengecek visibilitas tombol di UI, mencoba akses langsung `/experience/add/`, `/edit/`, dan `/delete/` lewat *address bar* untuk memastikan proteksi *server-side* benar-benar menolak (403 Forbidden) — bukan cuma menyembunyikan tombol di tampilan.
- Sesi Malam — Menemukan dan memperbaiki dua bug kecil di luar cakupan otorisasi: (1) halaman utama tidak menampilkan NPM/Program Studi/Bio karena `view show_main` belum mengirim variabel itu ke *context*, dan (2) karakter *backtick* (`` ` ``) tersangkut di `index.html` yang menyebabkan simbol aneh muncul di tampilan. Commit dan push final ke GitHub dengan pesan *commit* deskriptif per perubahan (`feat:`, `fix:`, `chore:`).


## AI Disclosure

Di tugas ini aku pakai AI (Claude) sebagai *pair programmer* untuk topik yang relatif baru buatku — sistem *permission* dan *Group* di Django — sambil tetap coba pahami dan verifikasi sendiri tiap bagian sebelum dipakai.

**Bagian yang dibantu AI:**

- Pola *data migration* (`RunPython` dengan fungsi *reverse*) untuk membuat *Group* "Editor" secara otomatis — ini konsep yang belum pernah aku pakai sebelumnya.
- Desain fungsi *helper* di `views.py` (`is_editor_user`, `can_edit_data`, `can_create_or_delete_data`) dan pola *context processor* kustom (`role_flags`) supaya variabel `is_editor` tersedia di semua template tanpa dikirim manual di tiap *view*.
- Penjelasan konsep beda "redirect ke login" (302, belum login) vs "403 Forbidden" (sudah login tapi tidak berhak), termasuk *checklist* skenario pengujian 4 peran yang aku pakai sebagai panduan.
- Bantu melacak akar masalah saat *debugging* — misalnya error `ImproperlyConfigured` waktu aku tidak sengaja klik tombol "Run" di VS Code untuk `views.py` (bukan lewat `manage.py runserver`), dan dua bug kecil di luar topik otorisasi (NPM tidak muncul di halaman utama, karakter *backtick* nyangkut di `index.html`).

**Bagian yang aku kerjain/verifikasi sendiri:**

- Analisis awal terhadap kode `views.py`, `models.py`, dan template dari Tutorial 4, untuk memetakan bagian mana yang sudah memenuhi target tugas (misalnya `starred_by` dan `toggle_star` ternyata sudah ada, jadi tidak perlu dibuat ulang) dan mana yang masih kurang (peran Editor).

- **Keputusan *permission* final** — Aku sendiri yang memutuskan dan memverifikasi lewat `python manage.py shell` bahwa *Group* "Editor" di database beneran cuma berisi `change_experience` dan `change_organization`, tidak lebih.
- **Penerapan ke tiap *view* & template** — Aku pasang sendiri pengecekan *helper* itu ke enam *view* (`add_experience`, `edit_experience`, `delete_experience`, `add_organization`, `edit_organization`, `delete_organization`) dan sesuaikan sendiri logika `{% if %}` di `experience.html`, `organization.html`, `base.html` biar tampilannya konsisten.
- **Eksekusi & penetapan Group lewat Django Admin** — Proses klik demi klik (pilih user, pindahkan grup dari kolom kiri ke kanan, Save) aku lakukan sendiri di `/admin/`, termasuk sempat salah klik checkbox user alih-alih klik nama usernya, dan aku sadari sendiri kesalahannya.
- **Pengujian manual menyeluruh** — Login-logout bergantian dengan banyak akun berbeda (Incognito Window), ketik URL manual satu-satu di *address bar* untuk pastikan proteksi *server-side* beneran nolak (403), bukan cuma tombolnya disembunyikan di UI. Beberapa kali hasil awal tidak sesuai ekspektasi karena aku lupa logout dari sesi sebelumnya — itu aku temukan dan perbaiki sendiri lewat proses coba-coba.
- **Disiplin Git** — Pembuatan *branch* terpisah dan pemecahan *commit* jadi beberapa bagian logis (`feat:`, `fix:`, `chore:`) aku jalankan dan verifikasi sendiri lewat `git status` dan `git log --oneline` di tiap tahap.


Dalam Menyusun Readme ini , masi dibantu oleh AI untuk menyusun kata katanya agar mudah dan enak dibaca, ide nya tetap dari aku.

---

# Tugas 5 — Web Interactivity with JavaScript

Di tugas ini halaman daftar **Experience** dan **Organization** dibuat interaktif memakai AJAX: halaman hanya merender kerangka, lalu datanya diambil dari endpoint JSON lewat `fetch()`. Hak akses tetap berlaku ,pengunjung yang belum login bisa membaca data, tapi menambah data hanya bisa dilakukan oleh Owner (superuser), dan itu dicek **di dalam view**, bukan sekadar menyembunyikan tombol.

## Fitur

- **Menampilkan data dengan AJAX** — `experience.html` dan `organization.html` hanya berisi kerangka (`#loading`, `#error`, `#empty`, `#grid`). Data diambil dari `/api/experience/` dan `/api/organization/` memakai `fetch()`. Respons JSON disusun manual dengan `JsonResponse` dan memuat informasi star `star_count`, `is_starred` (status star untuk user yang sedang login; selalu `false` untuk pengunjung), dan `starred_by_names`.

- **Tiga kondisi tampilan** — fungsi `displayPageSection()` mengatur kondisi *loading* , *data kosong*, dan *error*.

- **Pencarian dengan debouncing** — kolom cari memanggil API (`?title=` untuk Experience, `?name=` untuk Organization, filter `icontains`) tanpa reload. Permintaan baru dikirim 300 ms setelah user berhenti mengetik (`setTimeout` + `clearTimeout`), dan request lama dibatalkan dengan `AbortController` supaya respons yang telat tidak menimpa hasil terbaru.

- **Tambah data lewat modal + AJAX** — form tambah ada di dalam modal (Popover API) di halaman daftar, bukan di halaman terpisah. Form dikirim dengan `fetch()` ke `create_experience_ajax` / `create_organization_ajax`. View tersebut memakai `@require_POST`, memeriksa `is_superuser` di dalam view (**403** untuk pengunjung, user biasa, dan Editor), memvalidasi dengan `ModelForm` (**400** + `errors` berformat JSON), dan membalas **201** saat sukses. Setelah sukses, modal menutup, form di-reset, dan daftar dimuat ulang tanpa reload halaman.

- **CSRF** — permintaan POST menyertakan header `X-CSRFToken` (dibaca dari cookie `csrftoken` lewat `getCookie`) dan form juga memuat `csrfmiddlewaretoken` dari `{% csrf_token %}`. POST tanpa token ditolak Django dengan 403.

- **Notifikasi toast** — `showToast()` (dari `static/js/toast.js`) menampilkan toast sukses saat data berhasil ditambahkan dan toast error saat gagal, termasuk pesan validasi dari server.

- **Perlindungan XSS (dua lapis)** — (1) sisi JavaScript: setiap nilai teks yang disisipkan ke HTML lewat template literal/`innerHTML` dibungkus `escapeHtml()`, dan toast memakai `textContent`; (2) sisi server: `strip_tags` di method `clean_<field>` pada `ExperienceForm` dan `OrganizationForm`.

- **JavaScript bersama** — `getCookie` dan `escapeHtml` dipindahkan ke `static/js/utils.js` yang dimuat dari `base.html`, jadi tidak diduplikasi di tiap halaman.

- **Skrip yang aman untuk semua peran** — elemen yang hanya dirender untuk Owner (tombol tambah, modal, form) dicek dulu sebelum dipasangi event listener (`if (addForm) addForm.addEventListener(...)`), sehingga skrip tidak berhenti di tengah jalan untuk pengunjung/user lain.

## Tech Stack

Tidak ada dependency baru. Tetap Django + SQLite3, ditambah JavaScript (Fetch API, Popover API, `AbortController`) tanpa library tambahan.

## Struktur Proyek yang Diperbarui

```
myportofolio/
├── main/
│   ├── forms.py            # DIUBAH — pesan error clean_title diperbaiki
│   ├── tests.py            # DIUBAH — Class AjaxTest
│   ├── urls.py             # endpoint add-ajax & api JSON
│   └── views.py            # JsonResponse + create_*_ajax (403/400/201)
├── static/js/
│   ├── toast.js            # showToast
│   └── utils.js            # BARU — getCookie & escapeHtml bersama
├── templates/
│   ├── base.html           # DIUBAH — memuat utils.js
│   ├── experience.html     # DIUBAH — memakai utils.js
│   ├── organization.html   # DIUBAH — memakai utils.js
│   └── components/
│       ├── experience_form_modal.html
│       └── organization_form_modal.html
└── e2e_selenium.py         # GANTI NAMA dari test_e2e.py
```

## Cara Menjalankan & Menguji

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py test
```

**Uji manual XSS:** login sebagai Owner → klik **Tambah Experience** / **Tambah Organization** → isi judul/nama dengan `<img src="x" onerror="alert('XSS!')">` → server menolak (toast error, alert tidak muncul). Isi deskripsi dengan `Halo <img src="x" onerror="alert('XSS!')">` → tersimpan sebagai teks biasa `Halo`.

**Uji per peran:** buka `/experience/` dan `/organization/` sebagai pengunjung (Incognito), user biasa, Editor, dan Owner — data harus termuat di semua peran, tombol Tambah hanya untuk Owner.

## Progres Pengerjaan

- **Tahap 1 — Audit.** Membaca ulang instruksi tugas dan membandingkannya dengan kode dari Tutorial 5. Hasilnya, sebagian besar checklist sudah terpenuhi di Experience dan Organization;
- **Tahap 2 — Verifikasi perilaku.** Menjalankan aplikasi di database baru dan menguji semua peran (pengunjung, user biasa, Editor, Owner): kode status 201/400/403, POST tanpa token CSRF, payload XSS, struktur JSON beserta data star, pencarian, serta kondisi loading/kosong/error di sisi JavaScript.
- **Tahap 3 — Perbaikan & perapian.** Memperbaiki pesan error validasi yang tertukar (Experience menyebut "Nama proyek", Organization menyebut "Judul pengalaman"), memindahkan `getCookie`/`escapeHtml` ke `static/js/utils.js`, mengganti nama `test_e2e.py` karena membuat `manage.py test` crash (butuh `selenium` yang tidak ada di `requirements.txt`), dan menambah 6 tes otomatis.

## Pertanyaan Reflektif

1. **Debouncing** adalah teknik menunda eksekusi sebuah fungsi sampai pemicunya berhenti terjadi selama jangka waktu tertentu: setiap ada event baru, timer direset, dan fungsi hanya dijalankan jika timer sempat habis tanpa event baru. Pada pencarian AJAX, tanpa debouncing setiap ketikan (`input` event) langsung mengirim request, jadi mengetik "magang" menghasilkan 6 request padahal hanya hasil terakhir yang dibutuhkan. Akibatnya server dan database terbebani, bandwidth terbuang, tampilan berkedip karena daftar dirender ulang terus-menerus, dan muncul *race condition* — respons untuk "mag" bisa tiba setelah respons untuk "magang" sehingga hasil lama menimpa hasil baru. Di proyek ini aku memakai `setTimeout` 300 ms yang di-`clearTimeout` pada tiap ketikan, ditambah `AbortController` untuk membatalkan request yang sudah tidak relevan.

2. **`await`** menjeda eksekusi fungsi `async` sampai `Promise` yang dikembalikan `fetch()` selesai (*resolved*), lalu memberikan nilainya — objek `Response` — ke kode berikutnya. Penjedaan ini tidak memblokir *main thread*, jadi halaman tetap responsif selama menunggu jaringan. `await` juga dipakai pada `response.json()` karena membaca body juga asinkron. Kalau `await` tidak dipakai, variabel `response` hanya berisi `Promise` yang belum selesai, bukan `Response`: `response.ok` bernilai `undefined` (sehingga kode salah mengira request gagal), `response.json()` dijalankan terlalu dini atau menghasilkan `Promise` lagi, dan baris setelahnya berjalan sebelum data tiba. Selain itu, error jaringan tidak tertangkap oleh `try/catch` karena penolakan `Promise` terjadi belakangan, sehingga muncul *unhandled promise rejection* dan kondisi loading/error tidak pernah diperbarui dengan benar.

3. **XSS (Cross-Site Scripting)** adalah serangan di mana penyerang menyisipkan kode JavaScript berbahaya ke dalam halaman yang kemudian dijalankan di browser korban, dengan hak akses yang sama seperti halaman itu sendiri. Dampaknya antara lain pencurian cookie/sesi, melakukan aksi atas nama korban (misalnya mengirim POST dengan CSRF token korban), dan mengubah tampilan halaman. Data lewat AJAX/JavaScript lebih rentan karena template Django melakukan *auto-escaping* pada `{{ variabel }}` secara default, sedangkan di JavaScript kita menyusun string HTML sendiri (template literal lalu `innerHTML`) sehingga browser mengurai data itu sebagai HTML, dan tidak ada perlindungan otomatis. Payload seperti `<img src="x" onerror="alert('XSS!')">` bahkan berjalan tanpa tag `<script>`. Perlindungan jadi bergantung pada disiplin developer: satu nilai yang lupa di-escape sudah cukup menjadi celah. Karena itu di proyek ini kutetapkan beberapa lapis pertahanan: `escapeHtml()` untuk setiap nilai, `textContent` untuk toast, dan `strip_tags` di sisi server.

## AI Disclosure

Di tugas ini aku pakai **Gemini** sebagai pendamping, dan teman berdiskusi.

## Bagian yang dibantu AI:

- Brainstorming & Draf Awal kerangka dasar penjelasan teori.
- Mendapatkan rekomendasi terkait implementasi debouncing pada fitur pencarian dan saran arsitektur
- Menggunakan simulasi lingkungan virtual (seperti jsdom)
- membantu mengidentifikasi blind spot pada kondisi state antarmuka (loading/kosong/error).
- Mendapatkan referensi payload XSS yang aman digunakan untuk menguji celah keamanan pada input form.

## Bagian yang aku kerjain sendiri:

- Menulis dan mengintegrasikan kode AJAX secara langsung ke dalam views, forms, dan template (base.html, experience.html, organization.html).
- Melakukan pengujian menyeluruh terhadap endpoint API untuk memastikan response status code (201/400/403) sudah tepat. Menguji POST request tanpa CSRF token untuk memverifikasi proteksi keamanan, dan menyuntikkan payload XSS melalui modal untuk memastikan fungsi escape HTML bekerja.
- Menemukan dan memperbaiki pesan error validasi yang tertukar di forms.py. Melakukan refactoring dengan membuat static/js/utils.js untuk fungsi utilitas dan membersihkan fungsi-fungsi JavaScript yang duplikat di berbagai template.
- Menyunting, menulis ulang, dan menyesuaikan draf README.

Dalam menyusun bahasa pada readme ini masi menggunakana AI ,tetapi ide yang ingin disampaikan dan alurnya dari aku sendiri , dan aku juga memperbaiki bahasa yang tidak sesuai agar mudah di ikuti alurnya.



# Tugas 6 — Django REST Framework Implementation

# Fitur

1. Serializer — OrganizationSerializer dan ExperienceSerializer di main/serializers.py memakai fields yang ditulis eksplisit
2. Validasi di serializer — validate_name, validate_role, validate_status, dan validate_description (Organization) serta validate_title dan validate_description (Experience) membersihkan input dengan strip_tags
3. Permission 4 peran — IsPortfolioOwnerOrEditorOrReadOnly di main/permissions.py dipasang di endpoint daftar dan detail. Endpoint star memakai IsAuthenticated, dan akun pemberi star selalu diambil dari request.user.
4. API view berbasis fungsi — @api_view + SessionAuthentication di main/api_views.py.
5. Modal edit lewat PATCH — tombol Edit di halaman Organization dan Experience membuka modal yang langsung terisi data kartu, lalu mengirim PATCH ke API dengan fetch().
6. Browsable API  setiap endpoint bisa dibuka langsung di browser. Form POST/PUT/PATCH dan tombol DELETE hanya muncul untuk akun yang memang punya izin,

# Struktur Proyek yang Diperbarui

myportofolio/
├── main/
│   ├── serializers.py      # BARU — ExperienceSerializer & OrganizationSerializer
│   ├── permissions.py      # BARU — IsPortfolioOwnerOrReadOnly & IsPortfolioOwnerOrEditorOrReadOnly
│   ├── api_views.py        # BARU — daftar, detail, star (@api_view + SessionAuthentication)
│   ├── api_urls.py         # BARU — /api/v1/experiences/ & /api/v1/organizations/
│   ├── tests_api.py        # BARU — 21 test APITestCase (Experience & Organization)
│   ├── tests.py            # DIUBAH — 2 assertion menunjuk ke URL API baru
│   └── urls.py             # DIUBAH — route media hanya untuk folder gambar
├── portofolio/
│   ├── settings.py         # DIUBAH — "rest_framework" di INSTALLED_APPS
│   └── urls.py             # DIUBAH — include api/v1/ dan api-auth/
├── templates/
│   ├── experience.html     # DIUBAH — memakai /api/v1/, tombol Edit membuka modal PATCH
│   ├── organization.html   # DIUBAH — memakai /api/v1/, tombol Edit membuka modal PATCH
│   └── components/
│       ├── experience_edit_modal.html    # BARU
│       └── organization_edit_modal.html  # BARU
└── requirements.txt        # DIUBAH — djangorestframework~=3.18.3

# Cara Menjalankan & Menguji

python -m venv env
env\Scripts\activate            # Windows (macOS/Linux: source env/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py test main      # 40 test: 21 test API + 19 test lama

# Uji manual
1. Pemilik: tambah data (POST 201), tambah dengan nama <b></b> (POST 400 + toast), edit (PATCH 200), star (POST 200), hapus (DELETE 204).
2. Editor: hanya ada tombol Star dan Edit. Edit berhasil (PATCH 200), nama <b></b> ditolak (PATCH 400, modal tetap terbuka).
3. Pengguna biasa: hanya tombol Star.
4. Tanpa login: daftar tetap tampil, tombol star berubah jadi "Login untuk star".
5. Browsable API: buka /api/v1/organizations/<id>/ sebagai Editor. Ada tombol PUT dan PATCH, tapi tidak ada DELETE.

# Progres Pengerjaan
Memasang DRF, membuat serializer, permission, API view, dan api_urls.py, lalu mengganti AJAX di experience.html dan organization.html ke /api/v1/. Sempat kena ModuleNotFoundError: No module named 'main.api_urls' karena menjalankan check sebelum file itu dibuat. /api/v1/ juga sempat 404 saat runserver walaupun test lulus. Penyebabnya route media "tangkap semua" di main/urls.py, yang kemudian diperbaiki. Menguji Browsable API dengan akun superuser (POST 201 → PATCH 200 → DELETE 204 → GET 404) dan memastikan akun biasa tidak mendapat form POST.

# Pertanyaan Reflektif

1. REST (Representational State Transfer) adalah gaya arsitektur untuk merancang web API, bukan library atau format data. Data diperlakukan sebagai resource yang punya alamat sendiri (/api/v1/organizations/ untuk kumpulan, /api/v1/organizations/3/ untuk satu data), tindakan dinyatakan lewat HTTP method (GET membaca, POST membuat, PUT/PATCH mengubah, DELETE menghapus), klien dan server bertukar representasi data seperti JSON, dan setiap respons memakai status code yang bermakna (201, 204, 400, 403, 404). Karena itu JSON saja belum cukup. Endpoint Tugas 5-ku juga mengembalikan JSON, tapi tindakannya ditulis di URL dan semuanya memakai POST (/organization/add-ajax/, /organization/<id>/delete/), dan hapus data malah membalas redirect. Itu gaya RPC, bukan REST. (Proyekku memakai SessionAuthentication, jadi belum sepenuhnya stateless. Untuk klien AJAX di website yang sama, ini masih wajar.) PUT mengirim representasi pengganti yang lengkap, jadi semua field wajib harus dikirim. PATCH hanya mengirim field yang ingin diubah, dan field lain tetap. Contoh di test-ku: PUT {"title": "Incomplete"} ditolak 400 karena description tidak dikirim, sedangkan PATCH {"role": "Ketua Divisi"} hanya mengubah role. PUT cocok untuk form yang selalu mengirim semua field sebagai pengganti utuh. PATCH cocok untuk perubahan sebagian, misalnya hanya mengganti status aktif. Modal edit-ku memakai PATCH supaya tetap aman kalau suatu saat form-nya hanya mengirim sebagian field.

2. Serializer adalah "kontrak data" antara model dan klien, dan bekerja dua arah. Saat GET, serializer mengubah objek model menjadi tipe data Python yang lalu dirender menjadi JSON. Saat POST/PUT/PATCH, serializer membaca request.data, memvalidasinya (is_valid()), menyediakan validated_data, lalu save() memanggil create() atau update(). Dibanding merakit dictionary manual dengan JsonResponse seperti di Tutorial 05, keuntungannya:

- Field yang dikirim ditentukan di satu tempat (fields), sehingga data sensitif tidak bocor karena lupa.
- Validasi terpusat. validate_name membersihkan input dengan strip_tags, ChoiceField menolak kategori yang tidak ada, dan is_valid(raise_exception=True) otomatis membalas 400 dengan error per field.
- Field hasil perhitungan seperti star_count otomatis read-only, jadi tidak bisa dipalsukan (test_computed_fields_are_read_only).
- Satu serializer dipakai untuk input dan output sekaligus. Dulu output dirakit manual di get_organization_json, sedangkan input divalidasi terpisah lewat OrganizationForm.
- Lewat context, serializer bisa menghitung is_starred sesuai akun yang sedang melihat.

3. Autentikasi menjawab "siapa kamu". Di DRF, SessionAuthentication membaca cookie session dan mengisi request.user. Otorisasi menjawab "kamu boleh melakukan apa". Permission class seperti IsPortfolioOwnerOrEditorOrReadOnly memutuskan apakah request boleh diteruskan berdasarkan request.user dan HTTP method-nya. Urutannya: autentikasi dulu, lalu permission, baru isi view. Itu sebabnya pengguna biasa yang mengubah data yang tidak ada mendapat 403, bukan 404. Hak akses harus dicek di server karena menyembunyikan tombol hanya mengubah tampilan, bukan aturan. Siapa pun bisa mengirim request langsung lewat Console browser, Browsable API, atau curl tanpa menyentuh tombol. Contohnya, Editor tidak melihat tombol Hapus, tapi kalau ia mengirim DELETE langsung, server tetap menolak dengan 403 karena permission class. Ini dibuktikan oleh test_editor_can_update_but_not_create_or_delete, yang juga mengecek datanya tidak terhapus. Template hanyalah tampilan untuk pengguna; sumber kebenaran tetap di server.

4. SessionAuthentication mengandalkan cookie session yang dikirim otomatis oleh browser ke situsku, termasuk ketika request itu dipicu dari situs lain. Tanpa CSRF, situs jahat bisa membuat form tersembunyi yang mengirim POST atau DELETE ke /api/v1/organizations/ atas nama korban yang sedang login. Token CSRF mencegah hal ini: token ada di cookie csrftoken yang hanya bisa dibaca halaman dari origin yang sama, lalu dikirim ulang lewat header X-CSRFToken. Situs lain tidak bisa membaca cookie itu, jadi tidak bisa membuat header yang benar. Karena itu DRF mewajibkan token CSRF untuk POST, PUT, PATCH, dan DELETE dari pengguna yang terautentikasi lewat session. force_authenticate melewati proses autentikasi sepenuhnya: request.user langsung diisi tanpa session, tanpa cookie, dan tanpa pemeriksaan CSRF. Test seperti itu tetap lulus walaupun perlindungan CSRF rusak, jadi tidak membuktikan apa-apa soal CSRF. Untuk membuktikannya aku memakai APIClient(enforce_csrf_checks=True) dan .login() yang membuat session sungguhan: PATCH tanpa token ditolak 403 dan datanya tidak berubah (test_session_patch_without_csrf_is_rejected), sedangkan PATCH dengan token dari Browsable API berhasil 200 (test_session_patch_with_csrf_succeeds_for_editor).

# AI Disclosure
Di tugas ini aku pakai Gemini

# Bagian yang dibantu AI:
1. Memetakan contoh di Tutorial 7
2. Menemukan penyebab /api/v1/ 404 saat runserver
3. Membantu membaca pesan error saat debugging

# Dalam menyusun README dan jawaban pertanyaan reflektif ini aku masih dibantu AI untuk merangkai kata-katanya.