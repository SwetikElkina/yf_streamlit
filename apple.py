import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#Название приложения
st.title('Котировки компании Apple (AAPL)')

#Шаг 1: Выбор дат для загрузки данных о котировках
st.sidebar.header("Настройки")
startdate = st.sidebar.date_input("Выберите начальную дату:", value=pd.to_datetime('2020-01-01'))
enddate = st.sidebar.date_input("Выберите конечную дату:", value=pd.to_datetime('2023-12-31'))

# Загрузка данных
if startdate < enddate:
    ticker = 'AAPL'
    data = yf.download(ticker, start=startdate, end=enddate)

    # Шаг 2: Отображение данных
    st.write("### Данные о котировках Apple:")
    st.dataframe(data)

    # Шаг 3: Построение графика котировок
    st.write("### График котировок Apple:")
    plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], label='Закрытие', color='blue')
    plt.title('Котировки Apple (AAPL)')
    plt.xlabel('Дата')
    plt.ylabel('Цена (USD)')
    plt.legend()
    st.pyplot(plt)

    # Шаг 4: Скачивание данных
    csv = data.to_csv().encode('utf-8')
    st.download_button("Скачать данные о котировках (CSV)", csv, "applestockdata.csv", "text/csv")
else:
    st.error("Ошибка: Конечная дата должна быть больше начальной даты.")