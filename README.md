---
# Simple Google VRP Auto Passive Scanner

> **Passive JavaScript Reconnaissance Tool**  
> **Nusatenggara Timur Development**  
> **Coded By 𝕽𝖔𝖑𝖆𝖓𝖉𝖎𝖓𝖔**

---

## 📌 Deskripsi

**Simple Google VRP Auto Passive Scanner** adalah tools berbasis Python yang dirancang untuk melakukan **analisis pasif** terhadap file JavaScript publik pada domain Google dan resource terkait.

Tool ini bertujuan untuk:
- Mengidentifikasi **endpoint API**
- Menemukan **string ber-entropy tinggi** (token, key, hash)
- Mendeteksi **indikasi konfigurasi internal**
- Membantu proses **security research** tanpa eksploitasi

⚠️ **Tidak melakukan brute-force, fuzzing, ataupun eksploitasi aktif.**

---

## 🎯 Tujuan

- Membantu researcher & bug hunter dalam **Google VRP**
- Passive recon terhadap JavaScript publik
- Mengumpulkan data awal sebelum responsible disclosure

---

## ✨ Fitur Utama

- 🔍 Passive JavaScript scanning (inline & external)
- 🧠 Deteksi endpoint API & path sensitif
- 📊 Perhitungan entropy string
- 🎚️ Klasifikasi severity (INFO / LOW / MEDIUM)
- 🧱 Domain scope filtering (Google only)
- 🖥️ UI terminal interaktif (Rich)
- 📁 Output laporan otomatis (JSON)

---

## 🧰 Teknologi

- Python 3
- requests
- beautifulsoup4
- rich

---

## 📦 Instalasi

### 1️⃣ Clone Repository
```bash
git clone https://github.com/username/simple-google-vrp-passive-scanner.git
cd simple-google-vrp-passive-scanner

2️⃣ Install Dependency

pip install requests beautifulsoup4 rich


---

▶️ Cara Menjalankan

python scanner.py

Lalu masukkan target:

Target Url (Only Https) : https://developers.google.com


---

🧪 Cara Kerja Singkat

1. Mengambil HTML target


2. Mengekstrak semua <script>:

Inline JavaScript

External JavaScript (in-scope)



3. Melakukan pencocokan regex:

Endpoint API

Token / hash

Path konfigurasi



4. Menghitung entropy string


5. Memberikan severity berdasarkan skor


6. Menyimpan hasil ke file JSON




---

📊 Severity Level

Severity	Deskripsi

INFO	Endpoint umum / risiko rendah
LOW	Potensi internal reference
MEDIUM	Entropy tinggi / endpoint sensitif



---

📁 Struktur Output

vrp_output/
└── findings_YYYYMMDD_HHMM.json

Contoh Isi JSON

{
  "endpoint": "/internal/api/v1/users",
  "severity": "MEDIUM",
  "entropy": 4.12,
  "source": "inline"
}


---

🌐 Scope Domain

Tool ini hanya memproses domain yang termasuk scope, seperti:

google.com

googleapis.com

gstatic.com

firebaseio.com

developers.google.com

dan domain Google lainnya



---

⚠️ Disclaimer

> FOR EDUCATIONAL & AUTHORIZED SECURITY RESEARCH ONLY



Gunakan tool ini hanya pada domain yang kamu miliki izin

Jangan gunakan untuk aktivitas ilegal

Author tidak bertanggung jawab atas penyalahgunaan


Tool ini dibuat sesuai prinsip Google VRP:

Passive analysis

Public resources only

No exploitation

No auth bypass



---

🧠 Catatan Penting

Hasil scan BUKAN vulnerability final

Harus divalidasi manual

Gunakan untuk membantu responsible disclosure



---

📜 Lisensi

MIT License

Bebas digunakan, dimodifikasi, dan dibagikan
WAJIB menyertakan credit author


---

👤 Author

𝕽𝖔𝖑𝖆𝖓𝖉𝖎𝖓𝖔
Nusatenggara Timur Development
Security Researcher / Bug Hunter


---

⭐ Penutup

Kalau tools ini membantu:

⭐ Star repo ini

🍴 Fork & improve

🐞 Gunakan secara bertanggung jawab


Happy Hunting 🔥

---
