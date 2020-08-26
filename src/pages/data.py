import streamlit as st
import pandas as pd
import numpy as np
import sqlite3

@st.cache
def load_data(csv):
    data = pd.read_csv(csv, nrows=500)
    conn = sqlite3.connect('dataframes.db')
    data.to_sql('dataframe', conn, if_exists='replace')
    conn.close()
    return data

def data_info(df):
    count_null = df.isnull().sum()
    info = pd.concat(
        [
            df.dtypes,
            count_null,
            count_null/df.shape[0],
        ],
        axis=1
    )
    info.columns = ['dtype', 'count_null', 'ratio_null']
    return info

def header():
    st.title("View Data")

def body():
    csv_file = st.file_uploader('Upload a csv file here!', 'csv')

    data_load_state = st.text('Loading data...')
    data = load_data('https://s3-us-west-2.amazonaws.com/'
                'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
    data_load_state.text("Done!")

    st.header('Data')
    st.dataframe(data.head())
    if st.checkbox('See raw data?'):
        st.subheader('Raw data')
        st.dataframe(data)

    st.subheader('Data information')
    st.markdown(
        """
            - `count_null` is the number of nulls in the column
            - `ratio_nulls` is a ratio of nulls in the columns.
        """
    )
    st.dataframe(data_info(data))

    st.subheader("Describe of data")
    st.write(data.describe())


def write():
    header()
    body()