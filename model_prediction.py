import streamlit as st
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from tensorflow.keras.models import load_model  # type: ignore
import matplotlib.pyplot as plt
def show_model_prediction_page(data):
  """
  Displays the model prediction page and utilizes the provided data.

  Args:
      df: A pandas DataFrame containing the processed stock data.
  """
  st.subheader('Model Prediction')
  st.write("This page utilizes a pre-trained model to predict future stock prices.")
  symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL")
  df = yf.download(symbol, start="2020-01-01", end="2024-07-04")
  df = df.reset_index()
  df = df.drop(['Date','Adj Close'],axis = 1)
  # Data preparation
  data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
  data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])
  # Preprocessing steps (ensure consistency with data_exploration.py)
  scaler = MinMaxScaler(feature_range=(0, 1))
  scaler.fit(data_training)
  data_training_array = scaler.transform(data_training)
  x_train = []
  y_train = []
  for i in range(100, data_training_array.shape[0]):
      x_train.append(data_training_array[i-100:i])
      y_train.append(data_training_array[i, 0])
  x_train, y_train = np.array(x_train), np.array(y_train)
  # Load the model
  model = load_model(r"C:\Users\sanap\OneDrive\Documents\Stock_Trend_Prediction\keras_model.h5")
  # Testing and Prediction
  past_100_days = data_testing.tail(100)
  final_df = past_100_days._append(data_testing, ignore_index=True)
  input_data = scaler.transform(final_df)
  x_test = []
  y_test = []
  for i in range(100, input_data.shape[0]):
      x_test.append(input_data[i-100:i])
      y_test.append(input_data[i, 0])
  x_test, y_test = np.array(x_test), np.array(y_test)
  y_predicted = model.predict(x_test)
  # Inverse scaling for visualization
  scale_factor = 1 / scaler.data_min_
  y_predicted = y_predicted * scale_factor
  y_test = y_test * scale_factor
  # Visualization
  st.subheader('Original Vs. Predicted Price')
  fig2 = plt.figure(figsize=(10, 6))
  plt.plot(y_test, 'g', label='Original Price')
  plt.plot(y_predicted, 'r', label='Predicted Price')
  plt.xlabel('Time')
  plt.ylabel('Price')
  plt.legend()
  st.pyplot(fig2)
  st.write("Disclaimer : This is for educational purposes only. Do not use for real-world trading.")
if __name__ == "__main__":
  st.write("This model_prediction.py is not intended to be run directly.  "
           "Please use main.py to launch the multi-page application.")