# Prediksi Penjualan Menggunakan Machine Learning

## Deskripsi Proyek

Proyek ini bertujuan untuk memprediksi jumlah penjualan berdasarkan data transaksi historis menggunakan algoritma Machine Learning yaitu Linear Regression. Model dilatih menggunakan beberapa fitur penting seperti jumlah barang yang dibeli, harga per barang, bulan, dan tahun transaksi.

Selain itu, proyek ini juga dilengkapi dengan aplikasi web interaktif menggunakan Streamlit yang memungkinkan pengguna memasukkan data dan mendapatkan hasil prediksi secara langsung.

---

## Tujuan Proyek

Tujuan dari proyek ini adalah:

- Melakukan analisis data penjualan
- Membangun model Machine Learning untuk prediksi penjualan
- Mengevaluasi performa model
- Membuat aplikasi interaktif untuk prediksi menggunakan Streamlit
- Mempersiapkan portfolio Data Scientist

---

## Dataset

Fitur yang digunakan dalam model:

- QUANTITYORDERED : jumlah barang yang dibeli
- PRICEEACH : harga per barang
- MONTH_ID : bulan transaksi
- YEAR_ID : tahun transaksi

Target:

- SALES : total penjualan

---

## Model Machine Learning

Algoritma yang digunakan:

Linear Regression

Alasan menggunakan Linear Regression:

- Cocok untuk prediksi nilai numerik
- Mudah dipahami
- Cepat dalam proses training dan prediksi

---

## Evaluasi Model

Hasil evaluasi model:

Mean Absolute Error (MAE): 772.91

R2 Score: 0.6886

Interpretasi:

- Model mampu menjelaskan sekitar 68% variasi data penjualan
- Error prediksi relatif kecil dan model cukup baik digunakan untuk prediksi

---

## Aplikasi Web (Streamlit)

Aplikasi Streamlit memungkinkan pengguna untuk:

- Memasukkan jumlah barang
- Memasukkan harga barang
- Memilih bulan transaksi
- Memilih tahun transaksi
- Melihat hasil prediksi penjualan
- Melihat grafik simulasi prediksi

---

## Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit

---

## Demo Aplikasi

Aplikasi prediksi penjualan dapat diakses secara online melalui Streamlit:

https://salesproject.streamlit.app/

Pengguna dapat memasukkan jumlah barang, harga, bulan, dan tahun untuk mendapatkan prediksi penjualan secara real-time menggunakan model Machine Learning.

---
