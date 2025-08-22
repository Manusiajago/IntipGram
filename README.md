# IntipGram: Instagram Followers Analyzer


![Preview](./Screenshot%202025-08-22%20130323.png)



## Apa Itu IntipGram?
IntipGram adalah alat sederhana berbasis Python yang berjalan di terminal (CLI) untuk menganalisis data Instagram Anda. Alat ini dirancang khusus untuk membandingkan daftar **followers** (pengikut) dan **following** (yang Anda ikuti) dari file JSON yang diunduh resmi dari Instagram. Hasilnya? Anda bisa melihat siapa saja yang tidak mengikuti Anda balik (unfollowers), beserta ringkasan total followers, following, dan mutual follows.

Alat ini **ramah pemula**, hanya menggunakan library bawaan Python, dan menampilkan hasil dalam bentuk tabel yang mudah dibaca di terminal. Cocok untuk Anda yang ingin memeriksa akun Instagram tanpa ribet!

### Mengapa Menggunakan IntipGram?
- **Gratis dan Open-Source**: Jalankan di komputer Anda sendiri, tanpa biaya.
- **Privasi Terjaga**: Data Anda tetap lokal, tidak dikirim ke server mana pun.
- **Mudah Digunakan**: Cukup masukkan path file JSON, dan lihat hasilnya langsung.
- **Fokus pada Unfollowers**: Langsung tampilkan daftar orang yang Anda follow tapi tidak follow balik.

## Fitur Utama
- **Ringkasan Statistik**: Total followers, following, mutual follows, dan unfollowers.
- **Tabel Rapi**: Tampilkan daftar followers, following, dan unfollowers dalam format tabel ASCII (dengan username, tanggal follow, dan link profil). Tabel diurutkan dari yang terbaru.
- **Konversi Tanggal**: Timestamp dari JSON dikonversi menjadi format tanggal yang mudah dibaca (misalnya, "2025-08-22 14:30:00").
- **Pembatasan Panjang**: URL dan teks panjang dipotong agar tampilan tetap rapi di terminal.
- **Error Handling**: Pesan kesalahan yang jelas jika file tidak ditemukan atau format JSON salah.

## Persyaratan
- **Python 3**: Pastikan Anda punya Python versi 3.x terinstal (versi 3.6+ direkomendasikan). Unduh dari [python.org](https://www.python.org/downloads/) jika belum ada.
- **Tidak Ada Library Eksternal**: Semua menggunakan library bawaan Python seperti `json`, `os`, `sys`, dan `datetime`.
- **Sistem Operasi**: Bekerja di Windows, macOS, Linux, atau bahkan Termux di Android.

## Cara Mendapatkan Data JSON dari Instagram
Sebelum menggunakan IntipGram, Anda perlu mengunduh data dari Instagram. Ini proses resmi dan aman:

1. Buka aplikasi Instagram di ponsel atau website [instagram.com](https://www.instagram.com).
2. Masuk ke akun Anda.
3. Pergi ke **Settings** (Pengaturan) > **Your Activity** (Aktivitas Anda) > **Download Your Information** (Unduh Informasi Anda).
4. Pilih **Format: JSON** (bukan HTML).
5. Pilih data yang ingin diunduh (minimal pilih "Followers and Following").
6. Masukkan email Anda dan konfirmasi dengan password.
7. Tunggu email dari Instagram (bisa 1-48 jam, maksimal 30 hari). Klik link di email untuk unduh file ZIP.
8. Ekstrak ZIP: Cari folder `followers_and_following/`. Di dalamnya ada:
   - `followers_1.json` (daftar pengikut Anda).
   - `following.json` (daftar yang Anda ikuti).

**Tips Pemula**: Jika file ZIP besar, gunakan tools seperti WinRAR (Windows) atau unzip bawaan (Mac/Linux). Simpan file JSON di folder yang mudah diakses, misalnya Desktop.

## Cara Install dan Jalankan (Langkah demi Langkah)
### 1. Clone Repository dari GitHub
   - Buka terminal atau command prompt Anda.
   - Jalankan perintah ini untuk mengunduh proyek:
     ```
     git clone https://github.com/Manusiajago/IntipGram.git
     ```
     *(Ganti `[username-anda]` dengan username GitHub Anda jika Anda fork repo ini.)*
   - Masuk ke folder proyek:
     ```
     cd IntipGram
     ```

   **Tidak Punya Git?** Unduh ZIP repo dari GitHub dan ekstrak manual.

### 2. Jalankan Program
   - Di terminal, jalankan:
     ```
     python main.py
     ```
     (Atau `python3 main.py` jika Anda punya multiple versi Python.)
   - Program akan menampilkan banner keren!
   - Masukkan path ke file **followers JSON** (misalnya: `C:\Users\NamaAnda\Downloads\followers_1.json` atau `/home/namaanda/followers_1.json`).
   - Masukkan path ke file **following JSON** (misalnya: `C:\Users\NamaAnda\Downloads\following.json`).
   - Tunggu sebentar, dan lihat hasil analisis di terminal!

### Contoh Output
```
=== Analyzing Instagram Data ===

Total Followers: 50
Total Following: 60
Mutual Follows: 45
Unfollowers (You follow them, but they don't follow back): 15

Followers:
+----------+---------------------+-----------------------------+
| username | date                | href                        |
+----------+---------------------+-----------------------------+
| user1    | 2025-08-20 10:00:00 | https://www.instagram.co... |
| user2    | 2025-08-19 15:30:00 | https://www.instagram.co... |
... (daftar lengkap)

Following:
... (daftar lengkap)

Unfollowers:
... (daftar lengkap)
```

**Tips Pemula**: 
- Path file harus lengkap dan benar. Jika error "File not found", periksa path dengan copy-paste dari File Explorer.
- Jika terminal Anda kecil, scroll ke atas untuk lihat tabel lengkap.
- Jalankan ulang program jika ingin analisis file lain—tidak perlu restart terminal.

## Troubleshooting (Masalah Umum)
- **Error "File not found"**: Pastikan path benar dan file ada. Coba gunakan path absolut (lengkap dari root drive).
- **Error "Invalid JSON"**: Pastikan file adalah JSON asli dari Instagram, bukan yang rusak atau diedit.
- **Tabel Terpotong?**: Terminal Anda mungkin terlalu sempit—coba perbesar window atau gunakan terminal lain seperti Git Bash.
- **Timestamp Tidak Berubah Jadi Tanggal?**: Jika timestamp invalid, akan ditampilkan apa adanya.
- **Masalah Lain?**: Buka issue di GitHub repo ini, atau cek kode di `main.py` (mudah dibaca!).

## Kontribusi
Ingin tambah fitur? Fork repo ini, edit kode, dan buat Pull Request. Ide bagus: Tambah support untuk data lain seperti likes atau comments!

## Lisensi
MIT License – Bebas digunakan, modifikasi, dan distribusi. Lihat file `LICENSE` untuk detail.

Dibuat dengan ❤️ oleh Egal Assegaf. Jika suka, beri ⭐ di GitHub!

*Terakhir diperbarui: Agustus 2025*
