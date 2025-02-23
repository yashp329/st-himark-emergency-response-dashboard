import streamlit as st
import pandas as pd
import altair as alt
import page1
import page2
import page3

# Page configuration
st.set_page_config(
    page_title="St.Himark Updates",
    page_icon="🏛",
    layout="wide"
)

# Loading the data
df = pd.read_csv("C:/Users/yashp/OneDrive/Desktop/UoN Projects/Semester 2/Information Visualisation Project/clean_Himark_data.csv")

# Updated Header with Black Background
st.markdown('''
    <style>
        .rounded-box {
            background-color: #000000; /* Black background */
            padding: 7px; /* Padding around the content */
            border-radius: 10px; /* Rounded corners */
            box-shadow: 0 2px 4px rgba(255,255,255,0.1); /* Light Shadow */
            width: fit-content; /* Adjust width to fit content */
            margin: auto; /* Center the box horizontally */
        }
        .rounded-box h1 {
            color: white; /* White text color */
            font-size: 3em;
            font-family: Arial, sans-serif;
            margin: 0;
        }
    </style>

    <div class="rounded-box">
        <h1>🏛 St.Himark City Report</h1>
    </div>
''', unsafe_allow_html=True)

# Main Function
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
