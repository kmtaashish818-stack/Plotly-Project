India Map Data Visualization

An interactive Streamlit dashboard for exploring district-level data across India on an interactive map.

The application allows users to:

View data for overall India or select a specific state

Choose a Primary Parameter to control marker size

Choose a Secondary Parameter to control marker color

Explore district-level information directly on the map

Hover over districts to see district names

Tech Stack

Python

Pandas

NumPy

Streamlit

Plotly Express

Dataset

The project uses india.csv, which contains district-level data along with geographic coordinates.

Important columns include:

State

District

Latitude

Longitude

District code

Population

Households_with_Internet

Housholds_with_Electric_Lighting

sex_ratio

literacy_rate

The dataset combines district information with latitude/longitude values so it can be displayed on an interactive map.

How It Works

The dashboard provides three main controls in the sidebar:

Select a State

overall India shows all available districts.

A specific state filters the map to that state.

Select Primary Parameter

The selected parameter controls the size of the map markers.

Select Secondary Parameter

The selected parameter controls the color of the map markers.

After selecting the parameters, click the Plot button to display the map.

Project Structure

india-map-project/
│
├── project_plotly.py
├── india.csv
├── README.md
└── .gitignore

Installation

Clone the repository and install the required libraries:

pip install streamlit numpy pandas plotly

Run the Project

Run the Streamlit application with:

python -m streamlit run project_plotly.py

If your Python file is inside another folder, provide its path:

python -m streamlit run "path/to/project_plotly.py"

Map

The project uses Plotly's scatter_mapbox with the OpenStreetMap map style.

The map uses:

Latitude → district latitude

Longitude → district longitude

Size → selected primary parameter

Color → selected secondary parameter

Hover name → district name

Example

For example, you can select:

Primary Parameter → Population

Secondary Parameter → literacy_rate

The map will then use population to determine marker size and literacy rate to determine marker color.

Learning Purpose

This project was created to practice:

Pandas data handling

Filtering DataFrames

Working with geographic coordinates

Plotly Express

Interactive maps

Streamlit widgets

Building an interactive data visualization application

Future Improvements

Possible improvements include:

Add more visualization types

Add summary statistics for the selected state

Add charts along with the map

Improve map styling

Add data cleaning/preprocessing steps

Deploy the Streamlit application online