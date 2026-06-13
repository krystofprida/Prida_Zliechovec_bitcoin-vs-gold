import pandas as pd


def get_daily_returns(df):
    """Calculates daily percentage returns for given assets."""
    # pct_change computes the percentage change between days
    return df.pct_change().dropna()


def make_custom_index(returns_df, weights):
    """Creates a combined index based on user asset weights."""
    # weights is a dictionary like {'BTC-USD': 40, 'GC=F': 60}
    total_index_return = 0

    for ticker, percentage in weights.items():
        # Convert weight from percentage (e.g. 40) to decimal (0.4)
        weight_decimal = percentage / 100
        # Add weighted return of the asset to the total index
        total_index_return += returns_df[ticker] * weight_decimal

    return total_index_return


def get_cumulative_returns(returns_series):
    """Calculates cumulative growth of a 1 USD investment."""
    return (1 + returns_series).cumprod()
