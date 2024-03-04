import streamlit as st
import pandas as pd
from Analisa import tampilkan_analisa

df = pd.read_csv('https://raw.githubusercontent.com/ddapun/bike-sharing-dataset/main/day.csv')

def main():
    st.header("Bike Sharing Analysis")
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Cycling_%28mountain_biking%29_pictogram.svg/450px-Cycling_%28mountain_biking%29_pictogram.svg.png", caption="Source : Wikipedia")
    pilihan = st.sidebar.selectbox(
        'Hasil Analisis yang Tersedia:', 
                                           ['Relasi Penjualan dengan Hari Kerja dan Hari Libur', 
                                            'Relasi antara Cuaca, Musim, Bulan terhadap Penjualan', 
                                            'Tren Penjualan Bike Sharing'
                                            ]
                                            )
    tampilkan_analisa(pilihan)


if __name__ == '__main__':
    main()

