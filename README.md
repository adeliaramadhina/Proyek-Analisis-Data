# Bike Sharing SSS Dashboard 🚴✨

Analisis data dilakukan menggunakan data Bike Sharing untuk menjawab pertanyaan bisnis berikut:
- Bagaimana tren jumlah sepeda yang disewa dalam 2 tahun terakhir?
- Apa perbedaan rata-rata jumlah sepeda yang disewa setiap harinya antara penyewa kasual dan penyewa terdaftar?
- Bagaimana cuaca mempengaruhi rata-rata jumlah sepeda yang disewa?
- Apa hubungan antara jumlah sepeda yang disewa dengan suhu, kelembapan, dan kecepatan angin?

### Setup Environment Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

Run Dashboard
```
streamlit run dashboard.py
```
