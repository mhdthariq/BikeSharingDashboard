import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set page config first
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply consistent styling to plots
def set_plot_style(fig, ax):
    fig.patch.set_facecolor('#1E1E1E')
    ax.set_facecolor('#283747')
    for text in ax.get_xticklabels() + ax.get_yticklabels():
        text.set_color('white')
    ax.title.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.grid(True, linestyle='--', alpha=0.3, color='gray')
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('gray')
        spine.set_linewidth(0.5)
    fig.tight_layout()

# Plot functions
def plot_daily_trend(df):
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df['dteday'], df['cnt'], marker='o', linestyle='-',
            color='#3498DB', linewidth=2, markersize=5)
    ax.set_title("Daily Bike Rentals", fontsize=14, fontweight='bold')
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Number of Rentals", fontsize=12)
    set_plot_style(fig, ax)
    return fig

def plot_season_weather_impact(df):
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Plot 1: Mean rentals by season
    mean_per_season = df.groupby('season_label', as_index=False)['cnt'].mean()
    max_value = mean_per_season['cnt'].max()
    mean_per_season['highlight'] = mean_per_season['cnt'] == max_value
    palette = {True: 'crimson', False: 'lightgray'}

    sns.barplot(data=mean_per_season, x='season_label', y='cnt', hue='highlight',
                palette=palette, dodge=False, ax=ax1, legend=False)
    ax1.set_title('Rata-rata Peminjaman Sepeda per Musim')
    ax1.set_xlabel('Musim')
    ax1.set_ylabel('Rata-rata Jumlah Peminjaman')

    # Plot 2: Mean rentals by weather
    mean_per_weather = df.groupby('weather_label', as_index=False)['cnt'].mean()
    max_value = mean_per_weather['cnt'].max()
    mean_per_weather['highlight'] = mean_per_weather['cnt'] == max_value
    palette = {True: 'darkorange', False: 'lightgray'}

    sns.barplot(data=mean_per_weather, x='weather_label', y='cnt', hue='highlight',
                palette=palette, dodge=False, ax=ax2, legend=False)
    ax2.set_title('Rata-rata Peminjaman Sepeda per Kondisi Cuaca')
    ax2.set_xlabel('Cuaca')
    ax2.set_ylabel('Rata-rata Jumlah Peminjaman')

    set_plot_style(fig, ax1)
    set_plot_style(fig, ax2)
    fig.tight_layout()
    return fig

def plot_user_patterns(df):
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['weekday_name'] = pd.Categorical(df['weekday_name'], categories=weekday_order, ordered=True)

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, x='weekday_name', y='casual', label='Casual', ax=ax, marker='o')
    sns.lineplot(data=df, x='weekday_name', y='registered', label='Registered', ax=ax, marker='o')
    ax.set_title('Pola Peminjaman: Casual vs Registered per Hari')
    ax.set_xlabel('Hari dalam Minggu')
    ax.set_ylabel('Jumlah Peminjaman')

    legend = ax.legend()
    for text in legend.get_texts():
        text.set_color('white')

    set_plot_style(fig, ax)
    return fig

def plot_monthly_trend(df):
    # Ensure month is ordered correctly
    bulan_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df['month'] = pd.Categorical(df['month'], categories=bulan_order, ordered=True)

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df, x='month', y='cnt', estimator='mean', hue='month', palette='Blues', ax=ax, legend=False)
    ax.set_title('Rata-rata Peminjaman Sepeda per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Rata-rata Jumlah Peminjaman')
    plt.xticks(rotation=45)
    # ax.legend_.remove()  # Remove the legend as it's redundant

    set_plot_style(fig, ax)
    return fig

def plot_hourly_patterns(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, x='hr', y='cnt', errorbar=None, ax=ax, color='#2ECC71')
    ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Jam')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Jumlah Peminjaman')
    ax.set_xticks(range(0, 24))

    set_plot_style(fig, ax)
    return fig

def plot_workday_comparison(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=df, x='workingday', y='cnt', hue='workingday', palette='Set2', legend=False, ax=ax)
    ax.set_title('Distribusi Peminjaman: Hari Kerja vs Akhir Pekan/Libur')
    ax.set_xlabel('Working Day (0 = Libur, 1 = Kerja)')
    ax.set_ylabel('Jumlah Peminjaman')

    set_plot_style(fig, ax)
    return fig

# Main function
def main():
    # Set plotting style
    plt.style.use("dark_background")
    sns.set_style("darkgrid")

    # Load data
    day_df = pd.read_csv("main-data/day_data.csv")
    hour_df = pd.read_csv("main-data/hour_data.csv")

    # Convert date columns to datetime
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    hour_df['datetime'] = pd.to_datetime(hour_df['datetime'])

    # Add month column for day_df if not present
    if 'month' not in day_df.columns:
        day_df['month'] = day_df['dteday'].dt.month_name()

    # Ensure categories are ordered correctly
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_df['weekday_name'] = pd.Categorical(day_df['weekday_name'], categories=weekday_order, ordered=True)

    # Sidebar with filters
    st.sidebar.image("assets/logo.png", width=150)
    st.sidebar.title("Filters")

    # Date range filter
    min_date = day_df['dteday'].min().date()
    max_date = day_df['dteday'].max().date()
    start_date, end_date = st.sidebar.date_input(
        "Select Date Range",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    # Season filter
    seasons = st.sidebar.multiselect(
        "Select Seasons",
        options=day_df['season_label'].unique().tolist(),
        default=day_df['season_label'].unique().tolist()
    )

    # Weather filter
    weather_conditions = st.sidebar.multiselect(
        "Select Weather Conditions",
        options=day_df['weather_label'].unique().tolist(),
        default=day_df['weather_label'].unique().tolist()
    )

    # About section
    st.sidebar.divider()
    st.sidebar.subheader("About")
    st.sidebar.text("Created by: Muhammad Thariq")
    st.sidebar.text("Data: Bike Sharing Dataset")

    # Filter data
    filtered_day_df = day_df[
        (day_df['dteday'].dt.date >= start_date) &
        (day_df['dteday'].dt.date <= end_date) &
        (day_df['season_label'].isin(seasons)) &
        (day_df['weather_label'].isin(weather_conditions))
    ]

    filtered_hour_df = hour_df[
        (hour_df['dteday'].dt.date >= start_date) &
        (hour_df['dteday'].dt.date <= end_date)
    ]

    # Main content
    st.title("🚲 Bike Sharing Dashboard")
    st.info("Analysis of bike sharing patterns based on seasonality, user types, and time factors.")

    # Overview metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        total_rentals = filtered_day_df['cnt'].sum()
        st.metric("Total Rentals", f"{total_rentals:,}")
    with col2:
        avg_daily_rentals = filtered_day_df['cnt'].mean()
        st.metric("Average Daily Rentals", f"{avg_daily_rentals:.0f}")
    with col3:
        max_daily_rentals = filtered_day_df['cnt'].max()
        st.metric("Max Daily Rentals", f"{max_daily_rentals:,}")

    # Daily trend chart - Keep this as it already exists
    st.subheader("Daily Rental Trends")
    fig_daily = plot_daily_trend(filtered_day_df)
    st.pyplot(fig_daily)

    # Question 1: Impact of season and weather
    st.subheader("Pengaruh Musim dan Cuaca terhadap Jumlah Peminjaman")
    fig_season_weather = plot_season_weather_impact(filtered_day_df)
    st.pyplot(fig_season_weather)

    # Question 2: User patterns by day of week
    st.subheader("Perilaku Peminjaman Pengguna Berdasarkan Hari")
    fig_users = plot_user_patterns(filtered_day_df)
    st.pyplot(fig_users)

    # Question 3: Monthly trends
    st.subheader("Tren Peminjaman Sepeda per Bulan")
    fig_monthly = plot_monthly_trend(filtered_day_df)
    st.pyplot(fig_monthly)

    # Question 4: Hourly patterns
    st.subheader("Distribusi Penyewaan Sepeda Setiap Jam")
    fig_hourly = plot_hourly_patterns(filtered_hour_df)
    st.pyplot(fig_hourly)

    # Question 5: Workday vs Weekend comparison
    st.subheader("Perbandingan Hari Kerja dengan Akhir Pekan")
    fig_workday = plot_workday_comparison(filtered_day_df)
    st.pyplot(fig_workday)

    # Key insights
    st.subheader("Key Insights")
    with st.expander("📌 Usage Patterns", expanded=True):
        st.write("- Peak hours occur around 8 AM and 5-6 PM, aligning with commuting hours.")
        st.write("- Registered users dominate weekday rentals, suggesting commuter usage.")
        st.write("- Casual users are more active on weekends, indicating recreational use.")
        st.write("- Fall season shows the highest rental activity, followed by Summer.")
        st.write("- Clear weather conditions significantly increase rental numbers compared to rainy conditions.")

    # Footer
    st.divider()
    st.caption("Bike Sharing Dashboard | Created with Streamlit")

if __name__ == "__main__":
    main()
