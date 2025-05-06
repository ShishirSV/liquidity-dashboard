import streamlit as st
import pandas as pd
from visualise import plot_time_series
from model import score_cash_allocation

def load_data():
    return {
        "Nifty": pd.read_csv("data/nifty.csv"),
        "India VIX": pd.read_csv("data/vix.csv")
    }

st.title("Liquidity Dashboard")
data = load_data()

option = st.selectbox("Select dataset", data.keys())
df = data[option]
st.write(df.tail())

plot_column = st.selectbox("Select column to plot", df.columns[1:])
plot_time_series(df, "Date", plot_column)

risk = st.radio("Risk Tolerance", ["Low", "Medium", "High"])
allocation = score_cash_allocation(df, risk)
st.metric("💰 Recommended Cash Allocation", f"{allocation}%")
