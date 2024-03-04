import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/ddapun/bike-sharing-dataset/main/day.csv')


def tampilkan_analisa(pilihan):
    if pilihan == 'Relasi Penjualan dengan Hari Kerja dan Hari Libur':
        display_day_analysis(df)
    elif pilihan == 'Relasi antara Cuaca, Musim, Bulan terhadap Penjualan':
        display_season_relation(df)
    elif pilihan == 'Tren Penjualan Bike Sharing':
        display_trend(df)

def display_season_relation(df):
    st.header('Relasi antara Cuaca, Musim, Bulan terhadap Penjualan')
    
    st.subheader('Musim')
    st.write("Relasi Penjualan Bike Sharing dengan Musim")
    st.write("Kategori Musim : 1 = Spring, 2 = Summer, 3 = Fall, 4 = Winter")
    st.bar_chart(x='season', y='cnt', data=df)

    st.subheader('Cuaca')
    st.write("Relasi Penjualan Bike Sharing dengan Kondisi Cuaca")
    st.write("Kategori Cuaca : 1 = Cerah, 2 = Berawan, 3 = Hujan")
    st.bar_chart(x='weathersit', y='cnt', data=df)

    st.subheader('Bulan')
    st.write("Relasi Penjualan Bike Sharing dengan Kondisi Cuaca")
    st.bar_chart(x='mnth', y='cnt', data=df)

    st.write('''
             Jumlah penjualan bike sharing cenderung meningkat pada musim panas dan musim gugur, dan menurun pada musim dingin dan musim semi. Dapat dilihat juga penjualan paling banyak terjadi apabila cuacanya cerah, dan penjualan paling sedikit apabila cuacanya hujan. Dan penjualan banyak terjadi pada bulan 6 sampai bulan 9. Maka dapat disimpulkan bahwa cuaca, musim, dan bulan berpengaruh dalam penjualan, seperti pada cuaca cerah yang sering terjadi pada musim panas, dan cuaca hujan yang sering terjadi pada musim dingin.
             ''')


def display_day_analysis(df):
    st.header('Penjualan pada Hari Libur dan Hari Kerja')

    sales_by_day_type = df.groupby(['holiday', 'workingday'])['cnt'].sum().reset_index()

    # Mengganti nilai 0 dan 1 pada kolom holiday dan workingday dengan label yang lebih deskriptif
    sales_by_day_type['holiday'] = sales_by_day_type['holiday'].map({0: 'Non-Holiday', 1: 'Holiday'})
    sales_by_day_type['workingday'] = sales_by_day_type['workingday'].map({0: 'Weekend or Holiday', 1: 'Weekday'})

    # Set up Streamlit app

    # Create plot
    plt.figure(figsize=(10, 6))
    sns.barplot(data=sales_by_day_type, x='holiday', y='cnt', hue='workingday', color='steelblue', errorbar=None)
    plt.title('Penjualan pada Hari Libur dan Hari Kerja')
    plt.xlabel('Hari')
    plt.ylabel('Penjualan')
    plt.legend(title='Status Minggu')

    # Display plot using Streamlit
    st.pyplot(plt)

    st.write('''
             Berdasarkan hasil penelitian, orang-orang cenderung bersepeda di hari kerja yang bukan merupakan tanggal merah/libur, dan apabila dibandingkan dengan hari kerja, orang-orang tidak terlalu sering bersepeda di hari libur atau diluar jam kerja.
             ''')

def display_trend(df):
    st.header('Tren Penjualan Bike Sharing')

    st.write("")

    st.line_chart(x='dteday', y='cnt', data=df)

    st.write('''
             Dapat dilihat bahwa penjualan seiring berjalannya waktu meningkat, dan memuncak atau menurun pada bulan tertenu, seperti meningkat pada bulan 6 sampai bulan 9 dan menunjukkan penurunan pada bulan setelahnya.
             ''')
    