import streamlit as st
st.set_page_config(page_title="Home", page_icon="📊", layout="wide")


def main():
   st.title('Sales Information')
   st.markdown('Chose the tab to view the information')
   # nút chọn xem toàn bộ data
   
      
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass