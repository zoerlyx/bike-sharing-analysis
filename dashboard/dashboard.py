import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CONFIG
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# LOAD DATA (HASIL CLEANING)
day_df = pd.read_csv('main_data.csv')
hour_df = pd.read_csv('hour_data.csv')

day_df['dteday'] = pd.to_datetime(day_df['dteday'])

st.title("Bike Sharing Dashboard")
st.markdown("""
Dashboard ini menampilkan analisis:
- Pengaruh kondisi cuaca terhadap penyewaan sepeda  
- Pola penyewaan sepeda berdasarkan waktu  

Gunakan filter di sidebar untuk mengeksplorasi data.
""")

# SIDEBAR FILTER
st.sidebar.header("Filter Data")

# Filter tanggal
start_date = st.sidebar.date_input("Start Date", day_df['dteday'].min())
end_date = st.sidebar.date_input("End Date", day_df['dteday'].max())

# Filter season (dengan opsi All)
season_options = ["All Season"] + sorted(day_df['season'].unique().tolist())
season_filter = st.sidebar.selectbox("Pilih Musim", season_options)

# Filter weather (dengan opsi All)
weather_options = ["All Weather"] + sorted(day_df['weathersit'].unique().tolist())
weather_filter = st.sidebar.selectbox("Pilih Cuaca", weather_options)

# FILTER DATA
filtered_day = day_df[
    (day_df['dteday'] >= pd.to_datetime(start_date)) &
    (day_df['dteday'] <= pd.to_datetime(end_date))
]

if season_filter != "All Season":
    filtered_day = filtered_day[filtered_day['season'] == season_filter]

if weather_filter != "All Weather":
    filtered_day = filtered_day[filtered_day['weathersit'] == weather_filter]

# METRIC
st.subheader("Ringkasan Data")

col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", int(filtered_day['total_rentals'].sum()))
col2.metric("Rata-rata Harian", int(filtered_day['total_rentals'].mean()))
col3.metric("Jumlah Hari", filtered_day.shape[0])

# VISUALISASI 1 (diperkecil)
st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")

fig1, ax1 = plt.subplots(figsize=(6,4))
sns.barplot(data=filtered_day, x='weathersit', y='total_rentals', ax=ax1)
ax1.set_title("Rata-rata Penyewaan Berdasarkan Cuaca")
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig1)

st.markdown("""
Insight:  
Penyewaan sepeda cenderung lebih tinggi pada kondisi cuaca cerah dan menurun pada kondisi cuaca yang kurang mendukung. Hal ini menunjukkan bahwa faktor cuaca berpengaruh terhadap tingkat penggunaan sepeda.
""")

# VISUALISASI 2 (agregasi + ukuran kecil)
st.subheader("Pola Penyewaan Sepeda per Jam")

hour_avg = hour_df.groupby(['hr','workingday'])['total_rentals'].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(7,4))
sns.lineplot(data=hour_avg, x='hr', y='total_rentals', hue='workingday', ax=ax2)
ax2.set_title("Pola Penyewaan per Jam")
ax2.set_xlabel("Jam")
ax2.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig2)

st.markdown("""
Insight:  
Penyewaan sepeda meningkat pada pagi dan sore hari, terutama pada hari kerja. Hal ini menunjukkan pola penggunaan untuk aktivitas mobilitas harian.
""")