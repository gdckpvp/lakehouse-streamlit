import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="Data Statistics", page_icon=":bar_chart:", layout="wide")

def main():
    # tab view
    st.title("Data Statistics")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Brand", "City", "Category", "Frequency", "Corelation"])
    with tab1:
        st.markdown("## Brand")
        st.markdown("Click button on the image to view the full image")
        st.image("Image/Stastic/barplot_Brand.png")
        st.dataframe(pd.read_csv("data/df_Brand.csv"), hide_index=True, use_container_width=True)
    with tab2:
        st.markdown("## City")
        st.markdown("Click button on the image to view the full image")
        st.image("Image/Stastic/barplot_City.png")
        st.dataframe(pd.read_csv("data/df_totalByCity.csv"), hide_index=True, use_container_width=True)
    with tab3:
        st.markdown("## Category")
        st.markdown("Click button on the image to view the full image")
        st.image("Image/Stastic/scatterplot_CategoryStatistic.png")
        st.dataframe(pd.read_csv("data/df_Category1.csv"), hide_index=True, use_container_width=True)
    with tab4:
        st.markdown("## Frequency")
        st.markdown("Click button on the image to view the full image")
        st.image("Image/Stastic/pieplot_Frequency.png")
    with tab5:
        st.markdown("## Corelation")
        st.markdown("Click button on the image to view the full image")
        st.markdown("### Sales by category")
        st.image("Image/Stastic/scatterplot_SellScope.png")
        st.markdown("### Corelation in Item")
        st.image("Image/Stastic/heatmap.png")
        st.dataframe(pd.read_csv("data/TopItem.csv"), hide_index=True, use_container_width=True)



if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass