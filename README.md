# Chatbot E-Commerce (Tugas UAS)
Proyek ini adalah Chatbot cerdas untuk melayani pelanggan toko online secara otomatis.
Dibuat untuk memenuhi tugas UAS Mata Kuliah Pengantar Kecerdasan Buatan.
<img width="1054" height="580" alt="Screenshot SHOFFLE" src="https://github.com/user-attachments/assets/62f9f904-8a49-4893-9a99-6afc6d1fb754" />

## Demo Aplikasi
<div align="center">
  <video src="https://github.com/user-attachments/assets/fab9d7d8-c1db-449c-8b4a-f5864b82b5f3" controls="controls" style="max-width: 80%; border-radius: 10px;">
    Your browser does not support the video tag.
  </video>
  <p><i>Cuplikan interaksi Chatbot Shoffle dalam melayani pelanggan secara real-time.</i></p>
</div>

## Anggota Kelompok
1. Aliya Arta Paramita Purnomo (M0125005)
2. Fatihah Muthmainnah (M0125014)
3. Althif Shoffa Hidayatina (M0125029)

## Fitur Utama Chatbot Shoffle
Chatbot ini dirancang untuk memberikan pengalaman berbelanja yang responsif. Berikut adalah rincian fitur yang tersedia:
| Kategori Fitur | Nama Fitur | Deskripsi Singkat |
| :--- | :--- | :--- |
| **Layanan Dasar** | **Greeting & Closing** | Menangani sapaan awal dan ucapan terima kasih dengan bahasa yang ramah. |
| **Produk** | **Manajemen Stok** | Memberikan informasi mengenai ketersediaan barang, keaslian produk (original), dan jadwal *restock*. |
| | **Verifikasi Produk** | Meyakinkan pelanggan melalui konfirmasi bahwa foto produk adalah *Real Picture* (foto asli). |
| **Fashion & Style** | **Rekomendasi Tren** | Memberikan saran gaya kekinian . |
| | **Gender Style** | Memberikan rekomendasi OOTD spesifik untuk Pria dan Wanita . |
| **Ukuran (Sizing)** | **Size Consultant** | Membantu menentukan ukuran (S-XXL) berdasarkan berat badan, tinggi badan, dan lingkar dada . |
| **Transaksi** | **Informasi Harga** | Memberikan rincian harga produk . |
| | **Sistem Promo** | Menjelaskan ketersediaan diskon dan cara penggunaan kode promo saat pembayaran . |
| | **Metode Bayar** | Menginformasikan pilihan pembayaran via Transfer Bank atau E-Wallet (tanpa sistem COD). |
| **Operasional** | **Logistik** | Memberikan estimasi waktu pengiriman, pilihan jasa ekspedisi (JNE/J&T), dan info resi . |
| | **Kebijakan Retur** | Menjelaskan syarat penukaran barang cacat/salah kirim . |

## Struktur Folder Proyek
Berikut adalah penjelasan mengenai file-file utama yang ada dalam repositori ini:
| Nama File / Folder | Deskripsi |
| :--- | :--- |
| `app.py` | File utama yang berfungsi untuk menjalankan antarmuka pengguna (UI) menggunakan framework **Streamlit**. |
| `train_bot.py` | Skrip Python yang digunakan untuk mengolah data dan melatih model AI (*Neural Network*). |
| `intents.json` | Basis pengetahuan chatbot yang berisi kumpulan *tags*, *patterns*, dan *responses*. |
| `requirements.txt` | Daftar *library* Python yang wajib diinstal agar aplikasi dapat berjalan (Dependencies). |

## Cara Menjalankan
1. Install library:
   ```bash
   pip install scikit-learn nltk streamlit
2. Latih model
   ```bash
   python train_bot.py
3. Jalankan aplikasi
   ```bash
   python -m streamlit run app.py
