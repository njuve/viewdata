import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sqlite3

def get_number_columns(df):
    return df.select_dtyeps(include = ['float'])

def get_object_columns(df):
    return df.select_dtyeps(include = ['object'])

def get_connection():
    return sqlite3.connect('dataframes.db')

conn = get_connection()
data = pd.read_sql('SELECT * FROM dataframe', conn)
conn.close()

def header():
    st.title("EDA")

def body():
    chart_selection = st.selectbox('Chart type', ['bar_chart', 'line_chart', 'area_chart'])
    xselection = st.selectbox('x', list(data.columns))
    yselection = st.selectbox('y', list(data.columns))


    st.bar_chart(
        data[[xselection, yselection]]
    )

def write():
    header()
    body()

