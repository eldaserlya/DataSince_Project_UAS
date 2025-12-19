# Perbandingan Metode Machine Learning dan Deep Learning untuk Klasifikasi Target pada Dataset TAE

## 👤 Informasi
- **Nama:** *Elda Serlya Dwi Seviana*
- **NIM:** *233307044*
- **Mata Kuliah:** TI22406 – Data Science
- **Dosen Pengampu:** Gus Nanang Syaifuddiin, S.Kom., M.Kom.
- **Link GitHub Repository:** https://github.com/eldaserlya/DataSince_Project_UAS
- **Link Video Penjelasan:** *(tempel link video kamu di sini)*

---

## 1. 🎯 Ringkasan Proyek
Proyek ini membandingkan performa **Machine Learning** dan **Deep Learning** untuk tugas **klasifikasi** pada **Teaching Assistant Evaluation (TAE) dataset**.
Eksperimen mencakup:
- Data understanding & data preparation (encoding + scaling + split)
- Minimal **3 visualisasi EDA**
- Pelatihan **3 model**: **Baseline**, **Advanced ML**, dan **Deep Learning (MLP)**
- Evaluasi performa dan pemilihan model terbaik

---

## 2. 📌 Problem & Goals

### Problem Statements
1. Bagaimana memprediksi **target evaluasi asisten dosen (1/2/3)** berdasarkan fitur perkuliahan dengan performa yang baik?
2. Metode mana yang lebih efektif untuk dataset tabular kecil: **ML klasik** atau **Deep Learning**?
3. Bagaimana perbandingan trade-off **akurasi vs kompleksitas vs waktu training** antar model?

### Goals
1. Membangun 3 model klasifikasi (baseline, advanced ML, deep learning).
2. Menilai performa model menggunakan metrik klasifikasi (Accuracy, Precision, Recall, F1-Score).
3. Menentukan model terbaik dan memberikan insight dari data + hasil modeling.

---

## 3. 📊 Dataset
- **Nama Dataset:** Teaching Assistant Evaluation (TAE)
- **Jumlah Data:** 151 baris
- **Target/Kelas:** 3 kelas (1 = Poor, 2 = Average, 3 = Good)
- **File:** `data/tae.data`

### Fitur
| Kolom | Tipe | Deskripsi Singkat |
|---|---|---|
| `english_speaker` | kategorikal | status english speaker |
| `instructor` | kategorikal | ID instructor |
| `course` | kategorikal | ID mata kuliah |
| `semester` | kategorikal | semester (summer/regular) |
| `class_size` | numerik | jumlah mahasiswa |
| `target` | label | kelas evaluasi (1/2/3) |

---

## 4. 🧹 Data Preparation
Ringkas proses yang dilakukan (lihat notebook untuk detail):
- Pengecekan missing value & duplikasi
- Encoding fitur kategorikal (mis: One-Hot Encoding)
- Scaling fitur numerik (`class_size`) jika diperlukan
- Train-test split (disarankan stratify)

---

## 5. 🤖 Modeling
Model yang digunakan (sesuaikan dengan implementasi kamu di notebook):
1. **Model 1 – Baseline:** Logistic Regression (baseline linear)
2. **Model 2 – Advanced ML:** Decision Tree / Random Forest (non-linear)
3. **Model 3 – Deep Learning:** MLP (Multilayer Perceptron) untuk tabular

---

## 6. 🧪 Evaluation
Gunakan metrik klasifikasi:
- Accuracy
- Precision
- Recall
- F1-Score

### Ringkasan Hasil (isi dari output notebook)
| Model | Accuracy | Precision | Recall | F1-Score | Catatan |
|---|---:|---:|---:|---:|---|
| Baseline (LogReg) | *(isi)* | *(isi)* | *(isi)* | *(isi)* | |
| Advanced (Tree/RF) | *(isi)* | *(isi)* | *(isi)* | *(isi)* | |
| Deep Learning (MLP) | *(isi)* | *(isi)* | *(isi)* | *(isi)* | |

> Tambahkan juga confusion matrix / classification report di notebook untuk bukti evaluasi.

---

## 7. 📈 Hasil EDA (Minimal 3)
File visualisasi disimpan di folder `images/` (contoh):
- `images/eda_1_target_distribution.png`
- `images/eda_2_class_size_by_target.png`
- `images/eda_3_target_by_semester.png`

---

## 8. 🏁 Kesimpulan
- **Model terbaik:** *(isi hasil akhir dari evaluasi)*
- **Alasan:** *(contoh: performa tertinggi + stabil, tidak overfitting, waktu training efisien, dsb.)*
- **Insight penting:** *(contoh: ketidakseimbangan kelas, pengaruh class_size, dsb.)*

---

## 9. 🔁 Reproducibility (WAJIB)

### 9.1 Struktur Folder
```
DataSince_Project_UAS/
├── data/                  # dataset lokal (lihat catatan di bawah)
│   └── tae.data
├── images/                # hasil EDA & plot
├── models/                # model tersimpan (.pkl / .keras / .h5)
├── notebooks/             # notebook eksperimen
├── src/                   # (opsional) code modular
├── requirements.txt
├── .gitignore
└── README.md
```

### 9.2 Cara Menjalankan (Colab)
```bash
!git clone https://github.com/eldaserlya/DataSince_Project_UAS.git
%cd DataSince_Project_UAS
!pip install -r requirements.txt
```

Pastikan dataset ada di:
```bash
!ls -lah data
!head -n 3 data/tae.data
```

### Catatan penting (biar tidak error kalau refresh / offline)
Runtime Colab bisa reset, jadi file upload manual bisa “hilang”.
Solusi aman:
- Simpan `tae.data` di folder `data/` (ukuran kecil, aman), **atau**
- Download ulang dataset otomatis tiap runtime (lebih disarankan jika data besar).

---

## 10. 📎 Requirements
Dependensi ada di `requirements.txt`.
Jika perlu versi spesifik, ganti isinya menjadi versi yang muncul dari:
```bash
!pip freeze | grep -E "numpy|pandas|scikit-learn|matplotlib|tensorflow|joblib"
```
