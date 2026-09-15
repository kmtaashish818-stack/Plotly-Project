# India Map Data Visualization

An interactive Streamlit dashboard for exploring district-level data across India on a dynamic map, built with Python, Pandas, and Plotly Express.

## Features

- View data for all of India or filter down to a specific state
- Choose a **Primary Parameter** to control marker size
- Choose a **Secondary Parameter** to control marker color
- Explore district-level information directly on an interactive map
- Hover over markers to see district names

## Tech Stack

- Python
- Pandas
- NumPy
- Streamlit
- Plotly Express

## Dataset

The project uses `india.csv`, which contains district-level data combined with geographic coordinates so it can be plotted on a map.

Key columns include:

- `State`
- `District`
- `Latitude`
- `Longitude`
- `District code`
- `Population`
- `Households_with_Internet`
- `Housholds_with_Electric_Lighting`
- `sex_ratio`
- `literacy_rate`

## How It Works

The dashboard provides three main controls in the sidebar:

1. **Select a State** — choose "overall India" to see all districts, or pick a specific state to filter the map.
2. **Select Primary Parameter** — controls the size of the map markers.
3. **Select Secondary Parameter** — controls the color of the map markers.

After choosing your parameters, click **Plot** to render the map.

### Example

Selecting:
- Primary Parameter → `Population`
- Secondary Parameter → `literacy_rate`

will size each district marker by population and color it by literacy rate.

## Map Details

The map is built with Plotly's `scatter_mapbox`, using the OpenStreetMap style:

| Map property | Data column |
|---|---|
| Latitude | District latitude |
| Longitude | District longitude |
| Size | Selected primary parameter |
| Color | Selected secondary parameter |
| Hover name | District name |

## Project Structure

```
india-map-project/
│
├── project_plotly.py
├── india.csv
├── README.md
└── .gitignore
```

## Installation

Clone the repository and install the required libraries:

```bash
git clone https://github.com/kmtaashish818-stack/Plotly-Project.git
cd Plotly-Project
pip install streamlit numpy pandas plotly
```

## Usage

Run the Streamlit application:

```bash
python -m streamlit run project_plotly.py
```

If your Python file is in another folder, provide its path:

```bash
python -m streamlit run "path/to/project_plotly.py"
```

## Learning Purpose

This project was built to practice:

- Pandas data handling and DataFrame filtering
- Working with geographic coordinates
- Plotly Express and interactive maps
- Streamlit widgets and app layout
- Building a complete interactive data visualization application

## Future Improvements

- Add more visualization types
- Add summary statistics for the selected state
- Add supporting charts alongside the map
- Improve map styling
- Add data cleaning/preprocessing steps
- Deploy the Streamlit app online

## License

No license specified yet — consider adding one (e.g., MIT) if you plan to share or accept contributions.