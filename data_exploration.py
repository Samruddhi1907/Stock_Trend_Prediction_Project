import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import json
import time
def download_stock_data(symbol, start, end, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            df = yf.download(symbol, start=start, end=end)
            if df.empty:
                print(f"No data found for {symbol}. Retrying in 5 seconds...")
                retries += 1
                time.sleep(5)
                continue  # Continue to the next iteration
            return df
        except json.JSONDecodeError:
            print(f"Error downloading {symbol}. Retrying in 5 seconds...")
            retries += 1
            time.sleep(5)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    print(f"Failed to download {symbol} after {max_retries} retries.")
    return None

def show_data_exploration_page():
    """
    Displays the data exploration page.
    """
    # User input for stock symbol
    symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL")
    if symbol:
        try:
            df = download_stock_data(symbol, start="2020-01-01", end="2024-07-04")
            if df is not None:
                try:
                    df = df.reset_index()
                    df = df.drop(['Date'], axis=1)
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader('Data Summary')
                        st.write(df.describe())
                    with col2:
                        st.subheader("Understanding Moving Averages (WIP)")
                        with st.expander("Click to learn more"):
                            st.markdown("""
                            Moving Averages (MAs) are a technical analysis indicator used to smooth out price fluctuations
                            and identify trends.

                            - **100-day MA:** Represents the average closing price over the past 100 days.
                            - **200-day MA:** Represents the average closing price over the past 200 days.

                            A **Golden Cross** occurs when the 100-day MA crosses above the 200-day MA,
                            potentially indicating a trend reversal towards an uptrend.

                            A **Death Cross** occurs when the 100-day MA crosses below the 200-day MA,
                            potentially indicating a trend reversal towards a downtrend.

                            **Note:** This is a simplified explanation, and other factors should be considered for investment decisions.
                            """)
                    # Visualization 1: Closing price Vs. 100 & 200-day moving averages
                    st.subheader('Closing Price Vs. 100 & 200-day Moving Averages')
                    ma100 = df.Close.rolling(100).mean()
                    ma200 = df.Close.rolling(200).mean()
                    fig1 = plt.figure(figsize=(10, 6))
                    plt.plot(df.Close, label='Closing Price')
                    plt.plot(ma100, 'r', label='100-day MA')
                    plt.plot(ma200, 'g', label='200-day MA')
                    plt.legend()
                    plt.xlabel('Time')
                    plt.ylabel('Closing Price')
                    st.pyplot(fig1)
                    st.write("Note : If 100-day MA crosses 200-day MA then there is an Uptrend otherwise there is a Downtrend.")
                    processed_data = df
                    return processed_data
                except Exception as e:
                    st.error(f"Error processing data: {e}")
                    return None  # Return None on processing error
            else:
                st.error(f"Could not download {symbol} data.")
                return None  # Return None on download error
        except Exception as e:
            st.error(f"Error downloading or processing data: {e}")
            return None
    else:
        return pd.DataFrame()

if __name__ == "__main__":
    show_data_exploration_page()
