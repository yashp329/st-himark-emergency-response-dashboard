import streamlit as st
import pandas as pd
import altair as alt
import page1
import page2
import page3

#page configuration
st.set_page_config(
    page_title="St.Himark Updates",
    page_icon="🏛",
    layout="wide")

#loading the data
df= pd.read_csv("/Users/shriyakumbhoje/Desktop/IV project/clean_Himark_data.csv")

st.markdown('''
    <style>
        .rounded-box {
            background-color: #f0f0f0; /* Background color */
            padding: 7px; /* Padding around the content */
            border-radius: 10px; /* Rounded corners */
            box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Optional: Shadow */
            width: fit-content; /* Adjust width to fit content */
            margin: auto; /* Center the box horizontally */
        }
    </style>

    <div class="rounded-box">
        <h1 style="font-size:3em; font-family: Arial, sans-serif; margin: 0;">🏛 St.Himark City Report</h1>
    </div>
''', unsafe_allow_html=True)


def main():
    # Adding radio buttons for selecting options
    selected_option = st.sidebar.radio("Select an option", ("Areas of Concern", "Neighbourhood Reliability", "Uncertainty Over Time"))

    # Based on the selected option, calling the corresponding display function
    if selected_option == "Areas of Concern":
        page1.display_option1()
    elif selected_option == "Neighbourhood Reliability":
        page2.display_option2()
    elif selected_option == "Uncertainty Over Time":
        page3.display_option3()

if __name__ == "__main__":
    main()























