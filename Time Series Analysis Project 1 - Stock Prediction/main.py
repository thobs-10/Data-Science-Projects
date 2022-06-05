# import libraries
import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

# create a start date
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# start creating web app
st.title("Stock Prediction App")

# create different choices of stocks
# apple stock, google stocks, microsoft stocks, game stop stocks
stocks = ("AAPL", "GOOG", "MSFT", "GME")

selected_stocks = st.selectbox("Select dataset for prediction", stocks)

# add a slider to select number of years for prediction
num_years = st.slider("Year of prediction:", 1, 5)
period = num_years * 365

# cache the downloaded data to avoid re-downloading it again and again
# load the stock data
@st.cache
def load_stock_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

# create a pane for the data in streamlit
data_load_state = st.text("Load data...")
stock_data = load_stock_data(selected_stocks)
data_load_state.text("Loading data...done!")

# plot and analyze the data
st.subheader('Raw data')
st.write(stock_data.tail())

# function for ploting
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'], name='stock_close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# forecasting
df_train = stock_data[['Date', 'Close']]
# rename the columns
df_train = df_train.rename(columns = {"Date": "ds", "Close": "y"})

# create a facebook prophet model
model = Prophet()
model.fit(df_train)
# forecast
future = model.make_future_dataframe(periods=period)
prediction_forecast = model.predict(future)

# plot and analyze the data
st.subheader('Forecast data')
st.write(prediction_forecast.tail())

st.write("Forecast Data")
fig_1 = plot_plotly(model, prediction_forecast)
st.plotly_chart(fig_1)

st.write("Forecast components")
fig_2 = model.plot_components(prediction_forecast)
st.write(fig_2)
