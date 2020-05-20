# Gets stock data from financialmodelingprep and plot candle stick chart using plotly

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests
import json
quote = 'MSFT'
days = 300
def candlestick(quote,days):
  r = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/MSFT?timeseries=100')
  r = r.json()
 
  stockdata = r['historical']
  stockdata_df = pd.DataFrame(stockdata)
 
  fig = go.Figure(data=[go.Candlestick(x=stockdata_df['date'],
  open=stockdata_df['open'],
  high=stockdata_df['high'],
  low=stockdata_df['low'],
  close=stockdata_df['close'])])
  fig.update_layout(
    title= {
     'text': quote,
     'y':0.9,
     'x':0.5,
     'xanchor': 'center',
     'yanchor': 'top'},
   font=dict(
    family="Courier New, monospace",
    size=20,
    color="#7f7f7f"
 ))
  fig.show()
 
 
candlestick(quote,days)