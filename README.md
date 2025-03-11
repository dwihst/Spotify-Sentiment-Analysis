# Spotify-Sentiment-Analysis

# Spotify Sentiment Analysis using LSTM and Transfer Learning

## Deskripsi

Spotify adalah salah satu layanan streaming musik terbesar di dunia yang terus menghadapi persaingan ketat, baik dari layanan streaming musik lainnya maupun kemajuan dalam teknologi seperti Dolby Atmos dan audio lossless. Untuk tetap unggul, Spotify perlu memahami perasaan dan opini penggunanya terkait berbagai fitur yang mereka tawarkan, seperti musik, podcast, audiobook, dan pengalaman penggunaan secara keseluruhan. 

Proyek ini bertujuan untuk melakukan analisis sentimen terhadap ulasan pengguna Spotify dengan menggunakan model **Long Short-Term Memory (LSTM)**. Model ini kemudian diimprovisasi dengan menggunakan **transfer learning** untuk meningkatkan hasil prediksi. Dengan menggunakan analisis sentimen, Spotify dapat lebih mudah menyesuaikan strategi dan fitur mereka untuk meningkatkan pengalaman pengguna dan tetap unggul di pasar yang semakin kompetitif.

**Sumber**: [CNET - Best Music Streaming Service](https://www.cnet.com/tech/services-and-software/best-music-streaming-service/)

---

## Dataset

Dataset yang digunakan berasal dari **Kaggle**, yang berisi ulasan Spotify yang diambil melalui scrapping dari Google Play Store. Dataset ini mencakup berbagai elemen ulasan yang relevan untuk analisis sentimen.

Link Dataset: [Spotify Reviews 2022 - Kaggle](https://www.kaggle.com/datasets/mfaaris/spotify-app-reviews-2022)

| Column               | Description                                               |
|----------------------|-----------------------------------------------------------|
| Time_submitted       | Waktu saat ulasan diajukan.                               |
| Review               | Teks ulasan yang diberikan oleh pengguna.                 |
| Rating               | Rating yang diberikan (1-5).                              |
| Total_thumbsup       | Jumlah orang yang menganggap ulasan ini berguna.         |
| Reply                | Balasan atas ulasan dari tim Spotify.                     |

---

## Proses Analisis

1. **Preprocessing Data**:  
   Ulasan pengguna dibersihkan dan diproses untuk mengekstrak informasi yang relevan, seperti tokenisasi teks dan penghapusan kata yang tidak perlu (stopwords).

2. **Model LSTM**:  
   Jaringan LSTM digunakan untuk memprediksi sentimen dari ulasan pengguna. LSTM efektif untuk menangani data urutan, memungkinkan model untuk menangkap ketergantungan jangka panjang dalam teks.

3. **Transfer Learning**:  
   Transfer learning diterapkan pada model LSTM untuk meningkatkan akurasi, dengan menggunakan model yang sudah dilatih pada dataset besar dan kemudian disesuaikan dengan data ulasan Spotify.

4. **Evaluasi Model**:  
   Akurasi model diuji menggunakan data pengujian dan diperbaiki dengan mengoptimalkan parameter model dan arsitektur.

---

## Analisis

### Distribusi Rating
- Pengguna cenderung memberikan rating yang ekstrem (5 atau 1), menunjukkan bahwa mereka memiliki opini yang kuat, baik sangat puas atau sangat tidak puas.

### Kata-kata Positif dan Negatif
- Kata-kata yang sering muncul dalam ulasan positif: "love," "great," "easy," "awesome," "best," "premium."
- Kata-kata yang sering muncul dalam ulasan negatif: "issue," "problem," "fix," "bug," "crashes."

### Akurasi Model
- **LSTM tanpa Transfer Learning**: Akurasi pada data pelatihan 100%, namun sedikit lebih rendah pada data pengujian dengan akurasi 87%. Model kemungkinan mengalami overfitting.
- **LSTM dengan Transfer Learning**: Akurasi 78% pada data uji, yang cukup baik untuk klasifikasi sentimen biner.

### Masalah yang Dihadapi
- Model kesulitan dalam menangani ekspresi sentimen yang halus, seperti sarkasme atau bahasa figuratif, contohnya "this app is bad" yang terkadang diberi sentimen positif oleh model.

---

## Saran Perbaikan

1. **Pengenalan Sarkasme**:
   - Untuk meningkatkan pengenalan sarkasme, dapat menggunakan model berbasis transformer seperti **BERT** atau **RoBERTa**, yang lebih efektif dalam memahami konteks dan nuansa bahasa, termasuk sarkasme.
   - Menggunakan **linguistic features** dan **semantic embeddings** untuk mendeteksi pola bahasa yang lebih halus.
   
   **Sumber**: [ScienceDirect - Improving Sentiment Analysis](https://www.sciencedirect.com/science/article/abs/pii/S0925231220304689)

2. **Optimasi Model LSTM**:
   - Percobaan dengan **activation functions** (misalnya, **tanh**, **ReLU**, **Leaky ReLU**, atau **Elu**).
   - Mengubah ukuran batch (misalnya, 64, 128, atau 256) untuk melihat dampaknya terhadap kinerja model.
   - Menambah **hidden layers**, seperti **Bidirectional LSTM** untuk menangani urutan teks lebih baik.
   - Mengatur **DropOut** (misalnya, 0.3 atau 0.5) untuk mengurangi overfitting.

---
