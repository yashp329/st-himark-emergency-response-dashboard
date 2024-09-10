import numpy as np

import altair as alt
import streamlit as st
import pandas as pd

#loading the dataset
df= pd.read_csv("/Users/shriyakumbhoje/Desktop/IV project/clean_Himark_data.csv")
def display_option2():
        st.markdown('<center><h2 style="font-family: Arial, sans-serif">Reliability of Neighbourhood Report</h2></center>', unsafe_allow_html=True)
        options = ['sewer_and_water', 'power', 'medical', 'buildings', 'roads_and_bridges']
        colors = ['#FFFFE0','#e1f5b5','#949e7e','#91a16d','#6f804b','#566633','#404f1f','#2d4003','#1e5926','#052e0a']
  # Defining colors for each location


        # Sidebar
        with st.sidebar:
                selected_column= st.selectbox('Select an Option', options=sorted(options))

        col = st.columns((2,3.5, 2.5), gap='small')

        with col[0]:
                with st.expander('About', expanded=True):
                        st.write('''
                        <div style="border: 2px solid black; border-radius: 10px; padding: 10px;">
                            <p style="font-size: 16px;">
                                <span style="color:#F0E68C; font-weight: bold; font-size: 16px;">Most Active Time Period:</span> NIGHT
                            </p>
                            <p style="font-size: 16px;">
                                <span style="color:#F0E68C; font-weight: bold; font-size: 16px;">Least Active Time Period:</span> EVENING
                            </p>
                            <p style="font-size: 16px;">
                            <span style="color:#F0E68C; font-weight: bold; font-size: 16px;">Most Reliable Locations for Damage Assessment:</span>
                            <span style="font-size: 14px; color: orange;">BUILDINGS:</span><span style="font-weight: bold;">CHAPPARAL</span><span style="font-size: 14px;">, </span><span style="font-weight: bold;">OAK WILLOW</span>
                            </p>
                            <p style="font-size: 16px;">
                            <span style="font-size: 14px; color: orange;">MEDICAL:</span><span style="font-weight: bold;">OLD TOWN,TERRAPIN SPRINGS </span><span style="font-size: 14px;">
                            </p>
                            <p style="font-size: 16px;">
                            <span style="font-size: 14px; color: orange;">POWER:</span><span style="font-weight: bold;">PEPPER MILL ,EAST PARTON </span><span style="font-size: 14px;">
                            </p>
                            <p style="font-size: 16px;">
                            <span style="font-size: 14px; color: orange;">ROADS & BRIDGES:</span><span style="font-weight: bold;">EASTON,OAK WILLOW</span><span style="font-size: 14px;">
                            </p>
                            <p style="font-size: 16px;">
                            <span style="font-size: 14px; color: orange;">SEWER AND WATER:</span><span style="font-weight: bold;">EAST PARTON, PEPPER MILL, TERRAPIN SPRINGS</span><span style="font-size: 14px;">
                            </p>


                        </div>
                    ''', unsafe_allow_html=True)

        with col[1]:
                #chart1
                st.markdown('<center><h5> Avg Damage by Time period</h5></center>', unsafe_allow_html=True)
                custom_color_sch = alt.Scale(
                        domain=['Morning', 'Afternoon', 'Evening', 'Night'],
                        range=['#43755b','#FFFFE0','#dffabb','#3d613c']
                )

                grouped_bar_chart = alt.Chart(df).mark_bar().encode(
                        x=alt.X('Period_of_day:N', title='Time Period'),
                        y=alt.Y('mean(' + selected_column + '):Q', title='Mean Value'),
                        color=alt.Color('Period_of_day:N', scale=custom_color_sch, legend = None)
                ).properties(
                        width=390,
                        height=350
                ).configure_axis(
                        labelFontSize=14,
                        titleFontSize=16
                ).configure_mark(
                        cornerRadius=3
                )

                # Displaying the chart
                st.altair_chart(grouped_bar_chart)

                #chart2

                st.markdown('<center><h5> Location Vs Hours </h5></center>', unsafe_allow_html=True)
                color_scheme = alt.Scale(domain=[0, 10],
                                                range=['#FFFFE0','#f5efbf','#e3d986','#ded273','#d1c358','#d4c346','#d1bd2c','#cfb606','#c4cc5a','#c7d145','#8a912c','#788016','#4c5205',
                                                       '#32782a','#24661d','#17630f','#094a02','#3f7547','#044a0f']
                                                )
                heatmap = alt.Chart(df).mark_rect().encode(
                        x=alt.X('hours:O', title='Hours'),
                        y=alt.Y('location:N', title='Location'),
                        color=alt.Color(selected_column + ':Q', title='Value',
                                        scale=color_scheme),
                        tooltip=[selected_column, 'location:N', 'hours:O']
                ).properties(
                        width=390,
                        height=350
                ).configure_view(
                        strokeWidth=0
                ).configure_axis(
                        labelFontSize=14,
                        titleFontSize=16
                )

                # Displaying the heatmap
                st.altair_chart(heatmap)

        with col[2]:

                #chart3
                st.markdown('<center><h5> Distribution of</h5></center>', unsafe_allow_html=True)

                histogram = alt.Chart(df).mark_bar().encode(
                        x=alt.X(selected_column, bin=True),
                        y='count()',
                        tooltip=[selected_column]
                ).properties(

                        width=350,
                        height=350
                ).configure_mark(
                        fill='#FFFFE0',
                        cornerRadius=3
                )
                # Displaying the chart
                st.altair_chart(histogram)

                #chart4
                col=['#FFFFE0','#f5efbf','#e3d986','#ded273','#d1c358','#d4c346','#d1bd2c','#cfb606','#c4cc5a','#c7d145','#8a912c','#788016','#4c5205',
                                                       '#32782a','#24661d','#17630f','#094a02','#3f7547','#044a0f']
                st.markdown('<center><h5> Variablity Across Location </h5></center>', unsafe_allow_html=True)
                box_plot = alt.Chart(df).mark_boxplot().encode(
                        x=alt.X('location:N', axis=alt.Axis(title='Location')),
                        y=alt.Y(selected_column + ':Q'),
                        color=alt.Color('location:N', scale=alt.Scale(range=col), legend=None)
                ).properties(

                        width=350,
                        height=350
                ).configure_mark(
                        cornerRadius=3
                )

                # Displaying the chart
                st.altair_chart(box_plot)


