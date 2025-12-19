# Simple Google VRP Auto Passive Scanner
---

## 📌 Deskripsi

**Simple Google VRP Auto Passive Scanner** adalah tools berbasis Python yang digunakan untuk melakukan **analisis pasif** terhadap JavaScript publik pada domain Google dan resource terkait.

Tool ini membantu security researcher dan bug hunter untuk menemukan:
- Endpoint API tersembunyi
- Referensi internal
- Token / key / hash ber-entropy tinggi
- Konfigurasi sensitif dari resource publik

⚠️ Tool ini **TIDAK melakukan eksploitasi aktif**.

---

## 🎯 Tujuan

- Passive reconnaissance untuk Google VRP
- Membantu proses vulnerability discovery awal
- Mendukung responsible disclosure

---

## ✨ Fitur

- 🔍 Passive JavaScript scanning (inline & external)
- 🧠 Deteksi endpoint API & path sensitif
- 📊 Perhitungan entropy string
- 🎚️ Severity classification (INFO / LOW / MEDIUM)
- 🧱 Google scope domain filtering
- 🖥️ Terminal UI interaktif (Rich)
- 📁 Output laporan otomatis (JSON)

---

## 🧰 Teknologi

- Python 3
- requests
- beautifulsoup4
- rich

---

## 📦 Instalasi

```bash
git clone https://github.com/username/simple-google-vrp-passive-scanner.git
cd simple-google-vrp-passive-scanner
pip install requests beautifulsoup4 rich
