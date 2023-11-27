import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Gantilah 'nama_file.csv' dengan nama file CSV Anda
cp_air = 'changping_air.csv'

# Membaca data dari file CSV
df = pd.read_csv(cp_air)

# Judul Dashboard
st.title("Dashboard Analisis Data Udara")

# Sidebar untuk memilih jenis visualisasi
jenis_visualisasi = st.sidebar.selectbox("Pilih Jenis Visualisasi", ["Scatter Plot 3D", "Korelasi PM2.5 dan PM10"])

# Pilihan Visualisasi: Scatter Plot 3D
if jenis_visualisasi == "Scatter Plot 3D":
    st.header("Scatter Plot 3D Suhu vs CO vs O3")

    # Korelasi Suhu-CO dan Suhu-O3
    korelasi_suhu_co = df['TEMP'].corr(df['CO'])
    korelasi_suhu_o3 = df['TEMP'].corr(df['O3'])

    # Visualisasi Scatter Plot 3D
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(df['TEMP'], df['CO'], df['O3'], c=df['TEMP'], cmap='viridis', marker='o')

    # Tambahkan colorbar untuk keterangan warna suhu
    cbar = plt.colorbar(scatter)
    cbar.set_label('Suhu (°C)')

    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Konsentrasi CO')
    ax.set_zlabel('Konsentrasi O3')
    ax.set_title(f'Scatter Plot 3D Suhu vs CO vs O3\nKorelasi Suhu-CO: {korelasi_suhu_co:.2f}, Korelasi Suhu-O3: {korelasi_suhu_o3:.2f}')
    st.pyplot(fig)

# Pilihan Visualisasi: Korelasi PM2.5 dan PM10
elif jenis_visualisasi == "Korelasi PM2.5 dan PM10":
    st.header("Analisis Korelasi PM2.5 dan PM10")

    # Korelasi PM2.5 dan PM10
    korelasi_pm25_pm10 = df['PM2.5'].corr(df['PM10'])

    # Tampilkan Nilai Korelasi dan Scatter Plot
    st.write(f"Nilai Korelasi PM2.5 dan PM10: {korelasi_pm25_pm10:.2f}")

    # Visualisasi Scatter Plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='PM2.5', y='PM10', data=df)
    plt.title(f'Scatter Plot PM2.5 vs PM10\nKorelasi: {korelasi_pm25_pm10:.2f}')
    plt.xlabel('Konsentrasi PM2.5')
    plt.ylabel('Konsentrasi PM10')
    st.pyplot()

# Menampilkan informasi tambahan
st.sidebar.markdown("### Informasi Proyek")
st.sidebar.write("Nama: Jeconiah Firman Alvaro Siahaan")
st.sidebar.write("Email: jeconiah777@gmail.com")
st.sidebar.write("Id Dicoding: jeconiahfas")
