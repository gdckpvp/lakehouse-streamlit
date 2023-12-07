import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="Home", page_icon=":bar_chart:", layout="wide")

def Path(m,y):
    #colect image from foder Image and sub folder have path: D:\ShareFolder\test.t\Image\2021\TotalPay_by_Day_in_Month_1_in_2021.png
    #m: month
    #y: year
    #return: list image path
    path = None
    if m == "Full" or y == "Full":
        path = "Image/0/Total_by_Day_in_Month_0_in_0.png"
        return path
    else:
        path = "Image/" + str(y) +"/Total_by_Day_in_Month_" + str(m) + "_in_" + y + ".png"
        if os.path.isfile(path):
            return path
        else:
            path = None
            return path

def check_data(df):
    if df.empty:
        st.markdown("### Data is empty")
    else:
        m = df.tail(1)['Month'].values[0]
        y = df.tail(1)['Year'].values[0]
        #convert type of m and y to string
        m = str(m)
        y = str(y)
        Path(m,y)
        return Path(m,y)
    
 

def main():
   st.title('Sales Information')
   st.markdown('Choose the tab to view the information')
   df = pd.read_csv('data/df_totalByDay_pd.csv')
   
   st.markdown('# Doanh thu 10 ngày cuối cùng kể từ lần cuối dữ liệu được cập nhật')
   st.dataframe(df.tail(10),hide_index=True,use_container_width=True)
   if check_data(df) is not None:
       st.image(check_data(df))

         
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass