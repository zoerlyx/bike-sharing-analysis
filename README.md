# Bike Sharing Data Analysis Dashboard

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis dataset Bike Sharing guna memahami:

* Pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda
* Pola penyewaan sepeda berdasarkan waktu

---

## Setup Environment

### 1. Clone Repository

```
git clone https://github.com/fardhoz25/bike-sharing-analysis.git
cd project-bike
```

### 2. Membuat Virtual Environment

```
python -m venv venv
```

### 3. Aktivasi Virtual Environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

## Install Dependencies

Install library yang dibutuhkan menggunakan file requirements.txt:

```
pip install -r requirements.txt
```

---

## Menjalankan Dashboard Secara Lokal

Gunakan perintah berikut:

Pastikan berada di folder yang sesuai (misalnya folder dashboard) sebelum menjalankan perintah:

```
cd dashboard
python -m streamlit run dashboard.py
```

Dashboard akan berjalan di browser pada:

```
http://localhost:8502
```
Pastikan port yang digunakan sesuai dengan hasil yang muncul saat menjalankan Streamlit.

---

## Fitur Dashboard

* Visualisasi pengaruh cuaca terhadap penyewaan sepeda
* Visualisasi pola penyewaan per jam
* Filter interaktif:

  * Tanggal
  * Musim
  * Kondisi cuaca
  * Ringkasan metrik penyewaan

---

## Deployment (Streamlit Cloud)

Dashboard ini dapat dijalankan secara online melalui Streamlit Cloud dengan langkah berikut:

1. Upload project ke GitHub
2. Buka https://streamlit.io/cloud
3. Klik "New App"
4. Pilih repository
5. Tentukan file utama: `dashboard.py`
6. Klik Deploy

---

## Dataset

Dataset yang digunakan merupakan Bike Sharing Dataset yang telah melalui proses data cleaning sebelum digunakan dalam dashboard.

---

## Author

Nama: [Fardho Zurrahman]

## Demo Dashboard
https://dashboard-bike-project-zhxest8ngipb9ga3ndopht.streamlit.app/


