<h1 align="center">🚀 Auto Laporan Tugas (BY MPRUYBOGOR )</h1>

<p align="center">
  <b>Tool otomatisasi berbasis Python untuk mempercepat pembuatan laporan tugas praktikum. Mendukung pengambilan screenshot halaman web secara otomatis maupun perangkuman source code ke dalam format Markdown.</b>
</p>

---

## 📌 Daftar Isi
- [Tentang Tool](#-tentang-tool)
- [Prasyarat Sistem](#-prasyarat-sistem)
- [Installation & Setup](#-installation--setup)
- [Cara Penggunaan (Usage)](#-cara-penggunaan-usage)
- [Struktur Folder Proyek](#-struktur-folder-proyek)

---

## 📖 Tentang Tool
Tool ini dirancang untuk memudahkan mahasiswa atau developer dalam merangkum tugas-tugas praktikum berbasis web. Daripada mengambil screenshot satu-satu secara manual atau menyalin kode secara melelahkan, tool ini akan memproses semuanya secara otomatis dalam hitungan detik.

---

## ⚙️ Prasyarat Sistem
Sebelum menggunakan tool ini, pastikan komputer/laptop lu sudah terinstal:
1. **Python** (Versi 3.x direkomendasikan)
2. **Git** (Untuk clone repository)

---

## 🛠️ Installation & Setup

1. **Clone Repository**
   Buka terminal, Command Prompt, atau PowerShell di komputer lu, lalu jalankan perintah berikut:
   ```bash
   git clone [https://github.com/silentorbit545-coder/auto-laporan-tugas.git](https://github.com/silentorbit545-coder/auto-laporan-tugas.git)
   cd auto-laporan-tugas

   python auto_ss.py --mode output --folder html
   python auto_ss.py --mode kode --folder html
2. **Install Dependensi yang Diperlukan**
   Tool ini menggunakan pustaka Playwright untuk merender halaman HTML secara otomatis. Jalankan perintah ini di terminal:
   ```bash
    pip install playwright
    pip install playwright

 ## 🚀 Cara Penggunaan (Usage)

   3.**Jalankan Tool Sesuai Kebutuhan Mode**
   📸 Mode Screenshot Output (--mode output)
   Digunakan untuk mengambil tangkapan layar (screenshot) visual dari semua file HTML di dalam folder secara otomatis.
   ```bash
    python auto_ss.py --mode output --folder html
   python auto_ss.py --mode kode --folder html
