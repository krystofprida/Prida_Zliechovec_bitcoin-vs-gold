import logging
import pandas as pd
import streamlit as st
import yfinance as yf

# Simple logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("project.log"), logging.StreamHandler()],
)


@st.cache_data 
def download_asset_data(tickers, start_date, end_date):
    """Downloads Close prices from yfinance using EAFP principle."""
    logging.info(
        f"Starting data download for {tickers} from {start_date} to {end_date}"
    )

    try:
        # Fetch data from yfinance
        df = yf.download(tickers, start=start_date, end=end_date)

        # EAFP principle:  
        try:
            df_close = df["Close"]
        except KeyError:
            df_close = df

        df_clean = df_close.dropna()
        logging.info(f"Data successfully downloaded. Rows: {len(df_clean)}")
        return df_clean

    except Exception as e:
        # If something breaks (e.g. no internet), log the error and return empty df
        logging.error(f"Error during download: {e}")
        return pd.DataFrame()