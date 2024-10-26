import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import requests
import os  # For environment variables
import dataframe_image as dfi
import google.generativeai as genai

GEMINI_API_KEY='AIzaSyBrs06KLgPusgvxpHM3V5J4VVYWaZ9qsXY'
def fetch_stock_data(symbol):
    try:
        stock_data = yf.download(symbol, period='1mo')
        stock_data.reset_index(inplace=True)
        return stock_data
    except Exception as e:
        print(f"Error fetching stock data for {symbol}: {e}")
        return None

def descriptive_statistics(data):
    stats = data[['Open', 'High', 'Low', 'Close', 'Volume']].describe()
    return stats

def calculate_daily_returns(data):
    data['Daily Return'] = data['Close'].pct_change() * 100
    return data

def calculate_moving_averages(data):
    data['3-Day MA'] = data['Close'].rolling(window=3).mean()
    data['7-Day MA'] = data['Close'].rolling(window=7).mean()
    return data

def calculate_volatility(data):
    return data['Daily Return'].std()

def plot_price_trends(data, symbol):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'], marker='o', label='Close Price')
    plt.title(f'{symbol} Closing Price Trend Over the Last Month')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.tight_layout()  # Adjust layout
    plt.show()

def plot_daily_returns(data):
    plt.figure(figsize=(10, 5))
    plt.bar(data['Date'], data['Daily Return'], color='skyblue')
    plt.title('Daily Returns Over the Last Month')
    plt.xlabel('Date')
    plt.ylabel('Daily Return (%)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()

def generate_report(symbol):
    stock_data = fetch_stock_data(symbol)
    if stock_data is None:
        return  # Exit if data fetching failed

    stats = descriptive_statistics(stock_data)
    returns_data = calculate_daily_returns(stock_data)
    ma_data = calculate_moving_averages(returns_data)
    volatility = calculate_volatility(returns_data)
    dfi.export(stats, 'dataframe.png')
    

    print(f"\n--- Performance Report for {symbol} ---\n")
    print("Descriptive Statistics:")
    print(stats)
    
    print(f"\nVolatility (standard deviation of daily returns): {volatility:.2f}%")
    plot_price_trends(stock_data, symbol)
    plot_daily_returns(returns_data)


# Example usage
stock_symbol = input("Enter the stock symbol: ")
generate_report(stock_symbol)