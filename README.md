# Bike Sharing Dashboard

A data visualization dashboard for analyzing bike sharing patterns. This interactive dashboard explores trends in bike rentals based on seasonality, user types, weather conditions, and time factors.

![Bike Sharing Dashboard](dashboard/assets/logo.png)

## Overview

This Streamlit-based dashboard analyzes Capital Bikeshare data from Washington D.C., USA for 2011-2012. It provides insights on rental patterns through interactive visualizations that help identify key factors affecting bike rental usage rates.

## Features

- **Interactive filtering**: Filter data by date range, seasons, and weather conditions
- **Dynamic visualizations**: Charts update in real-time based on selected filters
- **Key metrics**: View total rentals, average daily rentals, and maximum daily rentals
- **Trend analysis**: Examine daily trends, seasonal patterns, and hourly distribution
- **User behavior**: Compare casual vs registered user rental patterns
- **Weather impact**: Analyze how different weather conditions affect rental rates

## Data Insights

The dashboard reveals several key findings:

- **Seasonal trends**: Fall season shows highest rental rates, while winter shows lowest
- **Weather impact**: Clear weather conditions drive maximum rentals
- **User patterns**: Registered users dominate weekday rentals (commuters), while casual users are more active on weekends (recreational)
- **Peak hours**: Morning (8 AM) and evening (5-6 PM) show highest rental activity, aligning with commute hours
- **Monthly distribution**: May-October period shows significantly higher rental activity

## Installation

### Prerequisites

- Python 3.7+
- pip package manager

### Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/mhdthariq/Bike-Sharing-Dashboard.git

    cd Bike-Sharing-Dashboard
    ```

2. Create Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

The dashboard will open in your default web browser, typically at [http://localhost:8501](http://localhost:8501)

Use the sidebar filters to interact with the data:

- Select a date range
- Choose seasons to include
- Select weather conditions

## Data Description

The dataset includes the following key variables:

- `dteday`: Date of observation
- `season`: Season (1=spring, 2=summer, 3=fall, 4=winter)
- `yr`: Year (0=2011, 1=2012)
- `mnth`: Month (1–12)
- `hr`: Hour of the day (0–23) – only in hourly data
- `holiday`: Whether the day is a holiday or not
- `weekday`: Day of the week
- `workingday`: 1 if neither weekend nor holiday, 0 otherwise
- `weathersit`: Weather conditions (1=clear, 2=mist/cloudy, 3=light precipitation, 4=heavy precipitation)
- `temp`: Normalized temperature
- `atemp`: Normalized feeling temperature
- `hum`: Normalized humidity
- `windspeed`: Normalized wind speed
- `casual`: Number of casual (non-registered) users
- `registered`: Number of registered users
- `cnt`: Total number of rentals (casual + registered)

## Acknowledgments

- Original dataset: Capital Bikeshare
- Weather data: Freemeteo
- Dataset published by: Hadi Fanaee-T, Laboratory of Artificial Intelligence and Decision Support (LIAAD), University of Porto

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
