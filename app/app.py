import streamlit as st
import pickle
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import os

# PAGE CONFIG

st.set_page_config(
    page_title="Sales Prediction Dashboard",
    layout="wide"
)

# LOAD MODEL

import os

@st.cache_resource
def load_model():
    base_path = os.path.dirname(__file__)
    model_path = os.path.join(base_path, "model_sales.pkl")

    with open(model_path, "rb") as file:
        model = pickle.load(file)

    return model

model = load_model()

# HEADER

st.title("Sales Prediction Dashboard")
st.markdown("Prediksi total penjualan berdasarkan input pengguna")
st.markdown("---")

# SIDEBAR INPUT

st.sidebar.header("Masukkan informasi penjualan")

quantity = st.sidebar.slider(
    "Jumlah barang yang dibeli",
    1, 100,
    10,
    help="Contoh: pelanggan membeli 10 barang"
)

price = st.sidebar.slider(
    "Harga per barang",
    10, 500,
    100,
    help="Contoh: harga 1 barang adalah 100"
)

# Menfgunakan mapping bulan
month_dict = {
    "Januari": 1,
    "Februari": 2,
    "Maret": 3,
    "April": 4,
    "Mei": 5,
    "Juni": 6,
    "Juli": 7,
    "Agustus": 8,
    "September": 9,
    "Oktober": 10,
    "November": 11,
    "Desember": 12
}

month_name = st.sidebar.selectbox(
    "Bulan transaksi",
    list(month_dict.keys())
)

month = month_dict[month_name]

year = st.sidebar.selectbox(
    "Tahun transaksi",
    [2003, 2004, 2005]
)

# MAIN CONTENT

col1, col2 = st.columns(2)

with col1:
    st.subheader("Ringkasan Input")

    st.write(f"Jumlah barang: {quantity}")
    st.write(f"Harga per barang: ${price}")
    st.write(f"Bulan: {month_name}")
    st.write(f"Tahun: {year}")

# PREDICT BUTTON

if st.sidebar.button("Predict Sales"):

    with st.spinner("Predicting..."):
        time.sleep(1)

        data = pd.DataFrame({
            'QUANTITYORDERED': [quantity],
            'PRICEEACH': [price],
            'MONTH_ID': [month],
            'YEAR_ID': [year]
        })

        prediction = model.predict(data)[0]

    with col2:

        st.subheader("Hasil Prediksi")

        st.metric(
            label="Prediksi Total Penjualan",
            value=f"${prediction:,.2f}"
        )

        if prediction > 5000:
            st.success("Penjualan diperkirakan tinggi")

        elif prediction > 2000:
            st.info("Penjualan diperkirakan sedang")

        else:
            st.warning("Penjualan diperkirakan rendah")

# CHART SECTION

st.markdown("---")
st.subheader("Simulasi Penjualan vs Jumlah Barang")

quantities = np.arange(1, 100)

sim_data = pd.DataFrame({
    'QUANTITYORDERED': quantities,
    'PRICEEACH': [price]*99,
    'MONTH_ID': [month]*99,
    'YEAR_ID': [year]*99
})

sim_pred = model.predict(sim_data)

fig, ax = plt.subplots()

ax.plot(quantities, sim_pred)

ax.set_xlabel("Jumlah Barang")
ax.set_ylabel("Prediksi Penjualan")
ax.set_title("Hubungan Jumlah Barang vs Penjualan")

st.pyplot(fig)

# FOOTER

st.markdown("---")

st.markdown(
"""
Dibuat dengan:

- Python  
- Scikit-learn  
- Streamlit  

Portfolio Data Science Project - Rika Rostika Afipah
"""
)
