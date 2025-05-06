import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def plot_time_series(df, date_col, metric_col):
    fig, ax = plt.subplots()
    ax.plot(pd.to_datetime(df[date_col]), df[metric_col])
    ax.set_title(f'{metric_col} over Time')
    ax.set_xlabel("Date")
    ax.set_ylabel(metric_col)
    st.pyplot(fig)
