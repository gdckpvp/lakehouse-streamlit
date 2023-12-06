import streamlit as st
import os

st.set_page_config(page_title="Data Statistics", page_icon=":bar_chart:", layout="wide")

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


def SelectMonth():
    #select month
    #return: month
    month = st.sidebar.selectbox("Select month", ["Full","1","2","3","4","5","6","7","8","9","10","11","12"])
    return month

def SelectYear():
    #select year
    #return: year
    year = st.sidebar.selectbox("Select year", ["Full","2021","2022","2023"])
    return year

def main():
    st.title("Sales By Date")
    st.sidebar.title("Select options")
    st.markdown("### Click button on the image to view the full image")
    # print select month and year in sidebar
    month = SelectMonth()
    year = SelectYear()
    st.sidebar.text("Month: " + month)
    st.sidebar.text("Year: " + year)
    # print image
    if Path(month,year) is not None:
        st.image(Path(month,year))
    if Path(month,year) is None:
        st.warning("We dont have data in this time!!!", icon="⚠️")

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass