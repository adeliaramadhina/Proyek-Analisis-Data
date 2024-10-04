import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

def create_daily_rental_df(df):
    daily_rental_df = df.resample(rule='D', on='dteday').agg({
        "cnt": "sum"
    })
    daily_rental_df = daily_rental_df.reset_index()
    daily_rental_df.rename(columns={
        "cnt": "total_rental"
    }, inplace=True)
    return daily_rental_df

def create_casual_weekday_df(df):
    casual_weekday_df = df.groupby("weekday").casual.mean().sort_values(ascending=False).reset_index()
    return casual_weekday_df

def create_registered_weekday_df(df):
    registered_weekday_df = df.groupby("weekday").registered.mean().sort_values(ascending=False).reset_index()
    return registered_weekday_df

def create_workingday_rental_df(df):
    workingday_rental_df = df.groupby(by="workingday").agg({
        "casual": "mean",
        "registered": "mean"
    }).reset_index()
    return workingday_rental_df

def create_cuaca_df(df):
    cuaca_df = df.groupby(by="weathersit").agg({
        "cnt": "mean",
    }).reset_index()
    
    cuaca_df.rename(columns={
        "weathersit": "Weather",
        "cnt": "Count Mean",
    }, inplace=True)

    return cuaca_df

def create_correlation_df(df):
    feature_cols = ["temp", "hum", "windspeed"]
    corr_series = df[feature_cols].corrwith(df["cnt"])
    correlation_df = corr_series.reset_index()
    correlation_df.columns = ['Feature', 'Correlation']
    return correlation_df

# Load cleaned data
main_data = pd.read_csv("https://raw.githubusercontent.com/adeliaramadhina/Proyek-Analisis-Data/refs/heads/main/dashboard/main_data.csv")

datetime_columns = ["dteday"]
main_data.sort_values(by="dteday", inplace=True)
main_data.reset_index(inplace=True)

for column in datetime_columns:
    main_data[column] = pd.to_datetime(main_data[column])

# Filter data
min_date = main_data["dteday"].min()
max_date = main_data["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/adeliaramadhina/Proyek-Analisis-Data/blob/main/dashboard/games_10574001.png?raw=true")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_data = main_data[(main_data["dteday"] >= str(start_date)) & 
                (main_data["dteday"] <= str(end_date))]

# Menyiapkan berbagai dataframe
daily_rental_df = create_daily_rental_df(main_data)
casual_weekday_df = create_casual_weekday_df(main_data)
registered_weekday_df = create_registered_weekday_df(main_data)
workingday_rental_df = create_workingday_rental_df(main_data)
cuaca_df = create_cuaca_df(main_data)
correlation_df = create_correlation_df(main_data)


# Jumlah Sepeda yang Disewa
st.header('Bike Rental SSS :sparkles::sparkles::sparkles:')
st.subheader('Daily Orders')

total_rental = daily_rental_df.total_rental.sum()
st.metric("Total Rental Bikes", value=total_rental)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    daily_rental_df["dteday"],
    daily_rental_df["total_rental"],
    marker='o', 
    linewidth=2,
    color="#6A9C89"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)


# Rata-rata jumlah sepeda yang disewa setiap harinya
st.subheader("Average Total Rental Bikes Each Day")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

colors = ["#6A9C89", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="casual", y="weekday", data=casual_weekday_df, palette=colors, ax=ax[0], order=casual_weekday_df['weekday'])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Casual Users", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(x="registered", y="weekday", data=registered_weekday_df, palette=colors, ax=ax[1], order=registered_weekday_df['weekday'])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Registered Users", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)


# Rata-rata jumlah sepeda yang disewa pada hari kerja dan bukan hari kerja
st.subheader("Average Total Rental Bikes on Working Day")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

ax[0].pie(x=workingday_rental_df["casual"], labels=workingday_rental_df["workingday"], autopct='%1.1f%%', colors=["#6A9C89", "#D1BB9E"], textprops={'fontsize': 35})
ax[0].set_title("Casual Users", loc="center", fontsize=50)

ax[1].pie(x=workingday_rental_df["registered"], labels=workingday_rental_df["workingday"], autopct='%1.1f%%', colors=["#6A9C89", "#D1BB9E"], textprops={'fontsize': 35})
ax[1].set_title("Registered Users", loc="center", fontsize=50)

st.pyplot(fig)


# Rata-rata jumlah sepeda yang disewa berdasarkan cuaca
st.subheader("Average Total Rental Bike based on Weather")

fig, ax = plt.subplots(figsize=(20, 10))

sns.barplot(
    y="Count Mean", 
    x="Weather",
    data=cuaca_df.sort_values(by="Count Mean", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_title(None)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)


# Korelasi antara Total Rental Bikes dengan Temperature, Humidity, and Wind Speed
st.subheader("Correlation on Total Rental Bikes")

tab1, tab2, tab3 = st.tabs(["Temperature", "Humidity", "Windspeed"])
 
with tab1:
    st.header("Total Rental Bikes vs Temperature")
    st.metric("Correlation Value", value=round(correlation_df[correlation_df['Feature'] == 'temp']['Correlation'].values[0], 3))
    fig_temp, ax_temp = plt.subplots(figsize=(8, 5))
    sns.regplot(x=main_data["temp"], y=main_data["cnt"], color="#6A9C89", line_kws={"color": "#424242"}, ax=ax_temp)
    st.pyplot(fig_temp)
 
with tab2:
    st.header("Total Rental Bikes vs Humidity")
    st.metric("Correlation Value", value=round(correlation_df[correlation_df['Feature'] == 'hum']['Correlation'].values[0], 3))
    fig_hum, ax_hum = plt.subplots(figsize=(8, 5))
    sns.regplot(x=main_data["hum"], y=main_data["cnt"], color="#6A9C89", line_kws={"color": "#424242"}, ax=ax_hum)
    st.pyplot(fig_hum)
 
with tab3:
    st.header("Total Rental Bikes vs Windspeed")
    st.metric("Correlation Value", value=round(correlation_df[correlation_df['Feature'] == 'windspeed']['Correlation'].values[0], 3))
    fig_wind, ax_wind = plt.subplots(figsize=(8, 5))
    sns.regplot(x=main_data["windspeed"], y=main_data["cnt"], color="#6A9C89", line_kws={"color": "#424242"}, ax=ax_wind)
    st.pyplot(fig_wind)


st.caption('SSS')
