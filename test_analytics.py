import pandas as pd
from analytics import get_daily_returns, make_custom_index


def test_daily_returns():
    """Test if percentage change calculation works correctly."""
    # Create fake price data: 100 USD -> 105 USD (which is a 5% increase)
    fake_data = pd.DataFrame({"BTC-USD": [100.0, 105.0]})
    returns = get_daily_returns(fake_data)

    # Check if the result is 0.05 (5%)
    assert round(returns["BTC-USD"].iloc[0], 2) == 0.05


def test_custom_index():
    """Test if the portfolio weight math is correct."""
    # Fake daily returns: Bitcoin +10%, Gold +2%
    fake_returns = pd.DataFrame({"BTC-USD": [0.10], "GC=F": [0.02]})
    fake_weights = {"BTC-USD": 50, "GC=F": 50}  # 50/50 portfolio

    result = make_custom_index(fake_returns, fake_weights)

    # Expected math: (0.10 * 0.5) + (0.02 * 0.5) = 0.05 + 0.01 = 0.06
    assert round(result.iloc[0], 2) == 0.06