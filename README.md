# Simple Google VRP Auto Passive Scanner
<img src="hekers.jpg" alt="IP Result" width="50%">
---

## Deskripsi

**Simple Google VRP Auto Passive Scanner** Adalah Tools Berbasis Python Yang Digunakan Untuk Melakukan **Analisis Pasif** Terhadap JavaScript Publik Pada Domain Google Dan Resource Terkait

Tool Ini Membantu Security Researcher Dan Bug Hunter Untuk Menemukan
- Endpoint Api Tersembunyi
- Referensi internal
- Token/Key/Hash Ber-Entropy Tinggi
- Konfigurasi Sensitif Dari Resource Publik Dan Privte

Tool Ini **TIDAK Melakukan Eksploitasi Aktif**.

---

## Tujuan

- Passive Reconnaissance Untuk Google VRP
- Membantu Proses Vulnerability Discovery Awal
- Mendukung Responsible Disclosure

---

## Fitur

- Passive JavaScript Scanning (Inline & External)
- Deteksi Endpoint Api & Path Sensitif
- Perhitungan Entropy String
- Severity Classification (INFO/LOW/MEDIUM)
- Google Scope Domain Filtering
- Output Laporan Otomatis (JSON)

---

## Teknologi

- Python 3
- requests
- beautifulsoup4
- rich

---

## Instalasi

```bash
git clone https://github.com/username/simple-google-vrp-passive-scanner.git
cd simple-google-vrp-passive-scanner
pip install requests beautifulsoup4 rich
```
## Cara Kerja 
- Fetch HTML target
- Extract semua JavaScript (inline & external)
- Filter domain berdasarkan Google scope
- Regex matching endpoint, token, config
- Hitung entropy string
- Tentukan severity
- Simpan hasil ke JSON Untuk Report

---

## Severity Level
- INFO Endpoint Umum/Risiko Rendah
- LOW	Potensi Internal Reference
- MEDIUM	Entropy Tinggi/Endpoint Sensitif

---

## Disclaimer
FOR EDUCATIONAL & AUTHORIZED SECURITY RESEARCH ONLY, Gunakan Hanya Pada Domain Yang Diizinkan!
