import streamlit as st
import pandas as pd
from Analisa import tampilkan_analisa

df = pd.read_csv('https://raw.githubusercontent.com/ddapun/bike-sharing-dataset/main/day.csv')

def main():
    st.sidebar.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    analysis_choice = st.sidebar.selectbox(
        'Hasil Analisis yang Tersedia:', 
                                           ['Relasi Penjualan dengan Hari Kerja dan Hari Libur', 
                                            'Relasi antara Cuaca, Musim, Bulan terhadap Penjualan', 
                                            'Tren Penjualan Bike Sharing'
                                            ]
                                            )
    tampilkan_analisa(analysis_choice)


if __name__ == '__main__':
    main()

