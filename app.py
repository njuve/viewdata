import streamlit as st
import src.pages.about
import src.pages.data
import src.pages.eda

st.set_option('deprecation.showfileUploaderEncoding', False)

PAGES = {
    'DATA': src.pages.data,
    'EDA': src.pages.eda,
    'ABOUT': src.pages.about,
}

st.sidebar.title("Navigation")
selection = st.sidebar.selectbox('PAGE', list(PAGES.keys()))
page = PAGES[selection].write()