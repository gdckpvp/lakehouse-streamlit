import streamlit as st
import os

def main():
    # tab view
    st.title("Data Statistics")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Category", "Brand", "City", "SalesScope", "Frequency"])
    # tab1: Category
    with tab1:
        st.markdown("## Category")
        st.markdown("### Click button on the image to view the full image")
        st.image("Image/Stastic/scatterplot_CategoryStatistic.png")
    # tab2: Brand
    with tab2:
        st.markdown("## Brand")
        st.markdown("### Click button on the image to view the full image")
        st.image("Image/Stastic/barplot_Brand.png")
    # tab3: City
    with tab3:
        st.markdown("## City")
        st.markdown("### Click button on the image to view the full image")
        st.image("Image/Stastic/barplot_City.png")
    # tab4: SalesScope
    with tab4:
        st.markdown("## SalesScope")
        st.markdown("### Click button on the image to view the full image")
        st.image("Image/Stastic/scatterplot_SellScope.png")
    # tab5: Frequency
    with tab5:
        st.markdown("## Frequency")
        st.markdown("### Click button on the image to view the full image")
        st.image("Image/Stastic/pieplot_Frequency.png")

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass