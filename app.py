# To run this app write in git bash:
# 1. Install all required packages: pip install -r requirements.txt
# 2. Launch the interactive web app: python -m streamlit run app.py
import pandas as pd
import plotly.express as px
import streamlit as st
from analytics import get_cumulative_returns, get_daily_returns, make_custom_index
from data_loader import download_asset_data

st.set_page_config(page_title="Asset Analytics Dashboard", layout="wide")
st.title("Bitcoin vs Physical Gold & Custom Stock Index")
st.write(
    "This app analyzes financial assets from 2016 to 2026. You can create your own custom index below."
)

# Sidebar for user inputs
st.sidebar.header("User Settings")

# Date inputs
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2016-04-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2026-03-31"))

# Asset weights sliders (PŮVODNÍ FUNKČNÍ VERZE)
st.sidebar.subheader("Set Index Weights (Must equal 100%)")
btc_w = st.sidebar.slider("Bitcoin (BTC-USD) weight %", 0, 100, 40)
gold_w = st.sidebar.slider("Gold (GC=F) weight %", 0, 100, 40)
spy_w = st.sidebar.slider("US Stocks (SPY) weight %", 0, 100, 20)

total_weight = btc_w + gold_w + spy_w
st.sidebar.write(f"**Total portfolio weight:** {total_weight}%")

# Main application logic
if total_weight != 100:
    st.sidebar.error("Error: The total weight must be exactly 100%!")
else:
    tickers = ["BTC-USD", "GC=F", "SPY"]
    weights = {"BTC-USD": btc_w, "GC=F": gold_w, "SPY": spy_w}

    # Download data
    prices_df = download_asset_data(tickers, str(start_date), str(end_date))

    if not prices_df.empty:
        returns_df = get_daily_returns(prices_df)
        custom_returns = make_custom_index(returns_df, weights)

        # Calculate cumulative performance
        cumulative_df = pd.DataFrame()
        cumulative_df["Our Custom Index"] = get_cumulative_returns(
            custom_returns
        )
        cumulative_df["Bitcoin Only"] = get_cumulative_returns(
            returns_df["BTC-USD"]
        )
        cumulative_df["Gold Only"] = get_cumulative_returns(returns_df["GC=F"])

        # VISUAL OUTPUT 1: Line Chart
        st.subheader("1. Cumulative Performance (Growth of 1 USD)")
        fig_line = px.line(
            cumulative_df,
            labels={"value": "Wealth Multiplier", "index": "Date"},
        )   
        fig_line.update_yaxes(type="log", tickformat=".0f")
        st.plotly_chart(fig_line, use_container_width=True)

        col1, col2 = st.columns(2)

        with col1:
            # VISUAL OUTPUT 2: Heatmap
            st.subheader("2. Correlation Heatmap")
            heatmap_data = returns_df.copy()
            heatmap_data["Custom Index"] = custom_returns
            matrix = heatmap_data.corr()

            fig_heat = px.imshow(
                matrix, text_auto=True, color_continuous_scale="RdBu_r"
            )
            st.plotly_chart(fig_heat, use_container_width=True)

        with col2:
            # VISUAL OUTPUT 3: Rolling Correlation
            st.subheader("3. Rolling Correlation (Bitcoin vs Gold)")
            window = st.slider("Select Rolling Window (Days)", 30, 180, 90)

            rolling_corr = (
                returns_df["BTC-USD"]
                .rolling(window)
                .corr(returns_df["GC=F"])
                .dropna()
            )
            fig_rolling = px.line(
                rolling_corr, labels={"value": "Correlation", "index": "Date"}
            )
            st.plotly_chart(fig_rolling, use_container_width=True)
    else:
        st.error("No data found. Please check your internet connection.")