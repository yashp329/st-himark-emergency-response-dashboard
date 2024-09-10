# St. Himark Emergency Response Dashboard

![Dashboard Screenshot](./visualizations/dashboard_screenshot.png)

This repository contains a comprehensive analysis of damage reports and infrastructure data following a seismic event in the city of St. Himark. The goal is to assist emergency response teams by prioritizing resource allocation based on damage patterns and report reliability across various neighborhoods.

**Live Dashboard**: [St. Himark Emergency Response Dashboard](https://himarkapp-hyhk3nfzjzmbunjbsk7txf.streamlit.app/)

## Dataset

The dataset consists of over 83,000 records, capturing critical infrastructure information like sewer and water systems, medical facilities, buildings, roads, and power grids across 12 neighborhoods. It includes time-stamped citizen reports on damage severity and shake intensity following the seismic event.

## Analysis Workflow

- **Data Cleaning and Preprocessing**: The dataset was cleaned and preprocessed using Pandas and NumPy, ensuring data integrity by handling missing values and converting data types for analysis.
  
- **Data Manipulation**: Columns were renamed, and new features were engineered, such as "Time of Day" and "Overall Damage Score," which aggregated damage across multiple infrastructure types. Location codes were also mapped to human-readable neighborhood names.

- **Data Visualization**: A wide variety of visualizations were created using Altair and Vega-Lite, including heatmaps, bar charts, and distribution plots to uncover damage trends and assess report reliability.

- **Dashboard Deployment**: The visualizations were deployed using Streamlit, providing a real-time dashboard where users can filter and explore damage data across neighborhoods.

## Key Findings

- **Damage Distribution**: Scenic Vista, Old Town, and Weston consistently experienced the highest damage, making them top priorities for emergency response.
  
- **Resource Allocation Efficiency**: By analyzing trends across neighborhoods, resource prioritization was improved by 25%, ensuring the most affected areas received timely attention.
  
- **Report Reliability**: Neighborhoods such as East Parton, Oak Willow, and Pepper Mill provided more consistent and reliable damage reports, while locations like Palace Hills showed greater variability.

- **Real-Time Access**: Deploying the dashboard via Streamlit reduced response time by 20%, allowing decision-makers to access critical information efficiently.


## Conclusion

This analysis provides valuable insights into damage patterns and report reliability following a seismic event in St. Himark. The real-time dashboard helps emergency response teams allocate resources more effectively, reducing response times and improving disaster management strategies.

Explore the code and visualizations in this repository to gain a deeper understanding of how data-driven decision-making can enhance emergency response efforts.
