# Bitcoin vs Physical Gold: A Comparative Analysis & Custom Index

This project is an interactive data analytics web application built with Python and Streamlit. It allows users to explore the historical performance, volatility, and correlation of Bitcoin (`BTC-USD`), Physical Gold (`GC=F`), and US Stocks (`SPY`) from 2016 to 2026.

## Authors
- Kryštof Přída
- Daniel Zliechovec

## Project Structure
- `app.py`: The main Streamlit web application interface and visualizations.
- `data_loader.py`: Handles downloading data from yfinance with integrated error handling (EAFP principle) and logging.
- `analytics.py`: Contains mathematical functions for daily returns and custom portfolio index calculation.
- `test_analytics.py`: Unit tests verifying the mathematical calculations using `pytest`.
- `requirements.txt`: List of dependencies required to run the project.
- `.gitignore`: Specifies files and folders for Git to ignore (e.g., local logs, `.venv`).

## How to Run the Project From Scratch

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/krystofprida/Prida_Zliechovec_bitcoin-vs-gold.git

2. Open Git Bash in the project root folder.
3. Install all necessary dependencies using pip: pip install -r requirements.txt
4. python -m streamlit run app.py

## Coherent Narrative & Key Analytical Findings

1. The "Digital Gold" Myth
Our analysis shows that while Bitcoin is often labeled as "digital gold", its price movements behave like a completely different asset class compared to physical gold. Bitcoin exhibits massive volatility and explosive cumulative returns, whereas gold acts as a slow, stable, and traditional safe haven.

2. Correlation Analysis
Through the Correlation Heatmap, we can observe that the daily returns of Bitcoin and Gold have a correlation very close to 0. This proves they are independent in daily movements, making them excellent assets for portfolio diversification.

3. Dynamic Custom Index
Following the project extension guidelines, we incorporated US Stocks (SPY) so users can build a custom blended index. For example, a portfolio of 40% BTC, 40% Gold, and 20% SPY smooths out Bitcoin's extreme volatility spikes while still heavily outperforming a pure gold investment over the 2016–2026 period. The interactive Streamlit environment allows users to test these different asset allocation strategies dynamically.