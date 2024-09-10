import numpy as np
import altair as alt
import streamlit as st
import pandas as pd

#loading the dataset
df= pd.read_csv("/Users/shriyakumbhoje/Desktop/IV project/clean_Himark_data.csv")


def display_option3():
    st.markdown('<center><h2 style="font-family: Arial, sans-serif">Uncertainty Over Time</h2></center>',unsafe_allow_html=True)
    options = ['sewer_and_water', 'power', 'medical', 'buildings', 'roads_and_bridges']
    location_dropdown = alt.binding_select(options=list(df['location'].unique()))
    location_selection = alt.selection_point(fields=['location'], bind=location_dropdown, name='Select_Location')

    # Sidebar
    with st.sidebar:
        loc_dropdown = st.sidebar.selectbox('Select a Location', options=sorted(df['location'].unique()))
        selected_option = st.selectbox('Select an Option', options=sorted(options))


    col = st.columns((2.0, 3.5, 2.5), gap='medium')
    with col[0]:
        with st.expander('About', expanded=True):
            st.write('''
                          <div style="border: 2px solid black; border-radius: 10px; padding: 10px;">
                              <p style="font-size: 16px;">
                                <span style="color:#F0E68C; font-weight: bold; font-size: 16px;">Peak Earthquake Hours:</span> 11am-12pm, 12am-1am
                              </p>
                              <p style="font-size: 16px;">
                                <span style="color:#F0E68C; font-weight: bold; font-size: 16px;">Optimal Assessment Days:</span> April 8th , April 9th
                            </p>
                            <p style="font-size: 16px;">
                                <span style="color:#F0E68C; font-weight: bold; font-size: 16px;">Most Active Time Period:</span> NIGHT
                            </p>
                            <p style="font-size: 16px;">
                                <span style="color:#F0E68C; font-weight: bold; font-size: 16px;">Least Active Time Period:</span> EVENING
                            </p>
                            <p style="font-size: 16px;">
                                <span style="color:#F0E68C; font-weight: bold; font-size: 16px;">Least Uncertainty over Days:</span> MEDICAL
                            </p>
                            <p style="font-size: 16px;">
                                <span style="color:#F0E68C; font-weight: bold; font-size: 16px;">Most Uncertainty over Days:</span> POWER
                            </p>
                          </div>
                      ''', unsafe_allow_html=True)

    with col[1]:
        #chart1
        st.markdown('<center><h5> Uncertainty over time </h5></center>', unsafe_allow_html=True)
        default_column = selected_option
        # Creating the boxplot
        boxplot = alt.Chart(df).mark_boxplot().encode(
            x=alt.X('day:O', title='Time'),
            y=alt.Y(selected_option + ':Q', title=selected_option),
        ).properties(
            width=390,
            height=320
        ).configure_view(
            strokeWidth=0
        ).configure_axis(
            labelFontSize=14,
            titleFontSize=16
        ).configure_mark(
            fill='#FFFFE0',
            cornerRadius=3
        )

        # Displaying the boxplot
        st.altair_chart(boxplot)

        #chart2
        # Filtering the data based on selected location
        filtered_df = df[df['location'] == loc_dropdown]

        # Defining color scheme
        color_scheme = alt.Scale(domain=[0, 10],
                                 range=['#FFFFE0','#d9f299','#99c965','#b2d162','#6d9c3b','#73b572','#59ab64','#27822a','#1c872c','#376b36','#558769'])

        # Creating the heatmap
        heatmap = alt.Chart(filtered_df).mark_rect().encode(
            x=alt.X('hours:O', title='Hours'),
            y=alt.Y('day:O', title='Day'),
            color=alt.Color(selected_option + ':Q', title='Value', scale=color_scheme),
            tooltip=[selected_option, 'hours:O']
        ).properties(
            width=390,
            height=300
        ).configure_view(
            strokeWidth=0
        ).configure_axis(
            labelFontSize=14,
            titleFontSize=16
        )

        # Displaying the heatmap
        st.markdown('<center><h5> Hours Vs Days </h5></center>', unsafe_allow_html=True)
        st.altair_chart(heatmap)

    with col[2]:
        #chart3
        st.markdown('<center><h5> Mean Damage by Hours</h5></center>', unsafe_allow_html=True)
        filtered_df = df[df['location'] == loc_dropdown]
        default_column = selected_option
        # Creating the grouped bar chart
        line_chart = alt.Chart(filtered_df).mark_line().encode(
            x=alt.X('hours:O', title='Hours'),
            y=alt.Y('mean(' + default_column + '):Q', title='Mean Value'),
        ).properties(
            width=340,
            height=320
        ).configure_axis(
            labelFontSize=14,
            titleFontSize=16
        )
        # Displaying the chart
        st.altair_chart(line_chart)

        #chart4
        custom_color = alt.Scale(
            domain=['Morning', 'Afternoon', 'Evening', 'Night'],
            range=['#43755b','#FFFFE0','#dffabb','#3d613c']
        )

        st.markdown('<center><h5> Uncertainty Over Time Period </h5></center>', unsafe_allow_html=True)

        # Filtering data based on location
        filtered_df = df[df['location'] == loc_dropdown]

        # Creating the horizontal box plot
        box_plot = alt.Chart(filtered_df).mark_bar().encode(
            y=alt.Y('Period_of_day:N', title='Period of the Day'),
            x=alt.X('mean(' + default_column + '):Q', title='Mean Value'),
            color=alt.Color('Period_of_day:N', scale=custom_color, legend= None)
        ).properties(
            width=340,
            height=290
        ).configure_axis(
            labelFontSize=14,
            titleFontSize=16
        ).configure_mark(
            cornerRadius=3
        )

        # Displaying the chart
        st.altair_chart(box_plot)










