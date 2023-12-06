import streamlit as st
st.set_page_config(page_title="Home", page_icon=":bar_chart:", layout="wide")

def main():
   st.title('Sales Information')
   st.markdown('Choose the tab to view the information')
         
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass