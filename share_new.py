import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


DATA_URL = ("C:/Users/Divya/gainers.csv")
DATA_UR= ("C:/Users/Divya/losers.csv")
df=pd.read_csv(DATA_URL)
df1=pd.read_csv(DATA_UR)

st.title("Share Price analysis for May 2019 to May 2020:")
st.sidebar.title("Share Price analysis for May 2019 to May 2020:")
st.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")
st.sidebar.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")


st.sidebar.title("Gainers")
select = st.sidebar.selectbox('Share', ['Adani Green Energy', 'GMM Pfaudler', 'AGC Networks', 'Alkyl Amines Chem', 'IOL Chem & Pharma'], key='1')


if not st.sidebar.checkbox("Hide", True, key='1'):
    st.title("Gainers")
    if select == 'Adani Green Energy':
        for i in ['AdaLow', 'AdaHigh', 'AdaClose', 'AdaOpen']:
            df[i] = df[i].astype('float64')
        avg_20 = df.AdaClose.rolling(window=20, min_periods=1).mean()
        avg_50 = df.AdaClose.rolling(window=50, min_periods=1).mean()
        avg_200 = df.AdaClose.rolling(window=200, min_periods=1).mean()
        set1 = { 'x': df.AdaDate, 'open': df.AdaOpen, 'close': df.AdaClose, 'high': df.AdaHigh, 'low': df.AdaLow, 'type': 'candlestick',}
        set2 = { 'x': df.AdaDate, 'y': avg_20, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'blue' },'name': 'MA 20 periods'}
        set3 = { 'x': df.AdaDate, 'y': avg_50, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'yellow' },'name': 'MA 50 periods'}
        set4 = { 'x': df.AdaDate, 'y': avg_200, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 200 periods'}
        data = [set1, set2, set3, set4]
        fig = go.Figure(data=data)
        st.plotly_chart(fig)
    elif select=='AGC Networks':
        for i in ['AgcLow', 'AgcHigh', 'AgcClose', 'AgcOpen']:
            df[i] = df[i].astype('float64')
        avg_20 = df.AgcClose.rolling(window=20, min_periods=1).mean()
        avg_50 = df.AgcClose.rolling(window=50, min_periods=1).mean()
        avg_200 = df.AgcClose.rolling(window=200, min_periods=1).mean()
        set1 = { 'x': df.AgcDate, 'open': df.AgcOpen, 'close': df.AgcClose, 'high': df.AgcHigh, 'low': df.AgcLow, 'type': 'candlestick',}
        set2 = { 'x': df.AgcDate, 'y': avg_20, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'blue' },'name': 'MA 20 periods'}
        set3 = { 'x': df.AgcDate, 'y': avg_50, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'yellow' },'name': 'MA 50 periods'}
        set4 = { 'x': df.AgcDate, 'y': avg_200, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 200 periods'}
        data = [set1, set2, set3, set4]
        fig = go.Figure(data=data)
        st.plotly_chart(fig)
    elif select == 'GMM Pfaudler':
        for i in ['GmmLow', 'GmmHigh', 'GmmClose', 'GmmOpen']:
            df[i] = df[i].astype('float64')
        avg_20 = df.GmmClose.rolling(window=20, min_periods=1).mean()
        avg_50 = df.GmmClose.rolling(window=50, min_periods=1).mean()
        avg_200 = df.GmmClose.rolling(window=200, min_periods=1).mean()
        set1 = { 'x': df.GmmDate, 'open': df.GmmOpen, 'close': df.GmmClose, 'high': df.GmmHigh, 'low': df.GmmLow, 'type': 'candlestick',}
        set2 = { 'x': df.GmmDate, 'y': avg_20, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'blue' },'name': 'MA 20 periods'}
        set3 = { 'x': df.GmmDate, 'y': avg_50, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'yellow' },'name': 'MA 50 periods'}
        set4 = { 'x': df.GmmDate, 'y': avg_200, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 200 periods'}
        data = [set1, set2, set3, set4]
        fig = go.Figure(data=data)
        st.plotly_chart(fig)
    elif select=='Alkyl Amines Chem':
        fig = go.Figure(data=[go.Candlestick(x=df['AlkDate'], open=df[' AlkOpen '], high=df[' AlkHigh '], low=df[' AlkLow '], close=df[' AlkClose '])])
        st.plotly_chart(fig)
    else:
        fig = go.Figure(data=[go.Candlestick(x=df['IolDate'], open=df[' IolOpen '], high=df[' IolHigh '], low=df[' IolLow '], close=df[' IolClose '])])
        st.plotly_chart(fig)



st.sidebar.title("Losers")
select = st.sidebar.selectbox('Share', ['Indiabulls Housing', 'YES Bank', 'Indusind Bank', 'GAIL India', 'HDFC Bank'], key='2')
if not st.sidebar.checkbox("Hide", True, key='2'):
    st.title("Losers")
    if select == 'Indiabulls Housing':
        fig = go.Figure(data=[go.Candlestick(x=df1['IBDate'], open=df1[' IBOpen '], high=df1[' IBHigh '], low=df1[' IBLow '], close=df1[' IBClose '])])
        st.plotly_chart(fig)
    elif select=='YES Bank':
        fig = go.Figure(data=[go.Candlestick(x=df1['YEDate'], open=df1[' YEOpen '], high=df1[' YEHigh '], low=df1[' YELow '], close=df1[' YEClose '])])
        st.plotly_chart(fig)
    elif select == 'Indusind Bank':
        fig = go.Figure(data=[go.Candlestick(x=df1['INDate'], open=df1['INOpen'], high=df1['INHigh'], low=df1['INLow'], close=df1['INClose'])])
        st.plotly_chart(fig)
    elif select=='GAIL India':
        fig = go.Figure(data=[go.Candlestick(x=df1['GADate'], open=df1[' GAOpen '], high=df1[' GAHigh '], low=df1[' GALow '], close=df1[' GAClose '])])
        st.plotly_chart(fig)
    else:
        fig = go.Figure(data=[go.Candlestick(x=df1['HDDate'], open=df1[' HDOpen '], high=df1[' HDHigh '], low=df1[' HDLow '], close=df1[' HDClose '])])
        st.plotly_chart(fig)
