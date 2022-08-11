import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

from module.get_finance import get_finance_df


def draw_cahrt(ticker, period_year):
    df_chart = get_finance_df(ticker, period_year)
    # 線グラフ描画
    fig = px.line(
        df_chart,
        markers=True,
    )
    return fig


if __name__ == "__main__":
    st.title("test")

    # sidebarに描画
    st.sidebar.write("test")
    period_year = st.sidebar.slider(
        'Select a range of year',
        1, 20)
    st.sidebar.write('Values:', period_year)
    ticker = st.sidebar.text_input("ticker", value="BZ=F")

    # 市況データ取得
    fig = draw_cahrt(ticker, period_year)
    st.plotly_chart(fig, use_container_width=True)
