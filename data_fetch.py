import yfinance as yf
import pandas as pd
import os

def fetch_nifty_data():
    df = yf.download("^NSEI", period="3y")
    df.reset_index(inplace=True)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/nifty.csv", index=False)

def fetch_vix_data():
    vix = yf.download("^INDIAVIX", period="3y")
    vix.reset_index(inplace=True)
    # vix = vix[["Date", "Close"]].rename(columns={"Close": "India VIX"})
    vix.to_csv("data/vix.csv", index=False)

if __name__ == "__main__":
    fetch_nifty_data()
    fetch_vix_data()
