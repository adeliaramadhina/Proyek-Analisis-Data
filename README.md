# Bike Sharing SSS Dashboard 🚴✨

Melakukan analisis data pada data Bike Sharing untuk menjawab pertanyaan bisnis berikut:
- Bagaimana tren jumlah sepeda yang disewa dalam 2 tahun terakhir?
- Apa perbedaan rata-rata jumlah sepeda yang disewa setiap harinya antara penyewa kasual dan penyewa terdaftar?
- Bagaimana cuaca mempengaruhi rata-rata jumlah sepeda yang disewa?
- Apa hubungan antara jumlah sepeda yang disewa dengan suhu, kelembapan, dan kecepatan angin?

Berbagai tahap analisis dilakukan, mulai dari data wrangling, exploratory data analysis, data visualization, hingga membuat dashboard Streamlit.

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

### Run Dashboard
```
streamlit run dashboard.py
```
