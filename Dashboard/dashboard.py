import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import ssl 
sns.set(style='dark')

ssl._create_default_https_context = ssl._create_unverified_context 
                                                                                   
#Judul Dashboard
st.title('Dashboard Performa Penyewaan Sepeda')

 # Menambahkan logo perusahaan
st.set_option('deprecation.showPyplotGlobalUse', False)
st.image("https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/image1_hH9B4gs.jpg")


#Baca Dataset
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/NurAnisahFadhilah/Bike-Sharing/main/Data/day.csv',delimiter=',')
    return data

def load_data1():
    data1 = pd.read_csv('https://raw.githubusercontent.com/NurAnisahFadhilah/Bike-Sharing/main/Data/hour.csv')
    return data1

st.subheader('Rata - Rata Penyewaan Berdasarkan Cuaca')

jumlah_pinjam = load_data().groupby('weathersit')['cnt'].mean()

# Disable the warning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Your plotting code
plt.bar(jumlah_pinjam.index, jumlah_pinjam.values, color='blue')
plt.title('Rata - Rata Penyewaan Berdasarkan Cuaca')
plt.xlabel('Cuaca')
plt.ylabel('Mean Penyewaan')

# Pass the figure to st.pyplot()
fig, ax = plt.subplots()
ax.bar(jumlah_pinjam.index, jumlah_pinjam.values, color='blue')
ax.set_title('Rata - Rata Penyewaan Berdasarkan Cuaca')
ax.set_xlabel('Cuaca')
ax.set_ylabel('Mean Penyewaan')
st.pyplot(fig)
st.markdown('''*Conclusion Pertanyaan 1 (Apakah terdapat pola peningkatan dalam jumlah peminjaman sepeda terkait dengan kondisi cuaca tertentu? Jika iya, cuaca seperti apa yang cenderung meningkatkan aktivitas peminjaman sepeda?)*

1: Cerah, Berawan

2: Mendung, Berembun

3: Hujan, Kabut

4: Salju, Angin Kencang

Angka 1-3 merepresentasikan cuaca, di mana telah dijelaskan keterangan dari angka-angka tersebut.
Dapat disimpulkan bahwa pada cuaca (1) di mana cuaca bersih dan berawan angka penyewaan sepeda meningkat lalu diikuti oleh cuaca (2) dan (3). Sedangkan di cuaca (4) tidak terdapat record peminjaman sepeda sama sekali.''')

st.subheader('Rata - Rata Penyewaan Berdasarkan Waktu')
jumlah_pinjam = load_data1().groupby('hr')['cnt'].mean()

# Your plotting code
fig, ax = plt.subplots()
ax.bar(jumlah_pinjam.index, jumlah_pinjam.values, color='yellow')
ax.set_title('Rata - Rata Penyewaan Berdasarkan Jam')
ax.set_xlabel('Waktu')
ax.set_ylabel('Mean Penyewaan')

# Display the plot using st.pyplot()
st.pyplot(fig)

st.markdown('''*Conclusion Pertanyaan 2 (Di waktu-waktu tertentu pada setiap harinya, kapan jumlah peminjaman sepeda cenderung mencapai puncaknya? Apakah terdapat pola tertentu dalam jam-jam tersebut?)*

Berdasarkan barplot tersebut, dapat dilihat bahwa angka peminjaman paling tinggi berada di antara pukul 17-18. Hal ini mungkin terjadi dikarenakan waktu tersebut merupakan waktu selesai aktivitas di daerah tersebut. Diikuti pada pukul 8 di mana kemungkinan merupakan waktu mulai beraktivitas.''')