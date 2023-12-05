import streamlit as st
import pandas as pd

def filter_data(data, search_term):
    # Filter data based on search term by any column (case insensitive) and return the filtered data
    return data[data.astype(str).apply(lambda x: x.str.contains(search_term, case=False).any(), axis=1)]

st.title('Sales Information')
#read 1000 rows from csv

my_dataframe = pd.read_csv("data/ndata.csv", sep="|", encoding="ISO-8859-9", nrows=10000)

# Sidebar search bar
search_term = st.sidebar.text_input(label='Search by Name', value='')

# Filtered DataFrame based on search
filtered_data = filter_data(my_dataframe, search_term)

# Display the filtered DataFrame
st.dataframe(filtered_data)