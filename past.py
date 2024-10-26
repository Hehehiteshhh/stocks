import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import requests  # Import requests for API calls

def fetch_stock_data(symbol):
    # Get the past month's data (1 month = approximately 30 days)
    stock_data = yf.download(symbol, period='1mo')
    stock_data.reset_index(inplace=True)
    return stock_data

def descriptive_statistics(data):
    stats = data[['Open', 'High', 'Low', 'Close', 'Volume']].describe()
    return stats

def calculate_daily_returns(data):
    data['Daily Return'] = data['Close'].pct_change() * 100  # Percentage change
    return data

def calculate_moving_averages(data):
    data['3-Day MA'] = data['Close'].rolling(window=3).mean()
    data['7-Day MA'] = data['Close'].rolling(window=7).mean()
    return data

def calculate_volatility(data):
    return data['Daily Return'].std()  # Standard deviation of daily returns

def plot_price_trends(data, symbol):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'], marker='o', label='Close Price')
    plt.title(f'{symbol} Closing Price Trend Over the Last Month')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.show()

def plot_daily_returns(data):
    plt.figure(figsize=(10, 5))
    plt.bar(data['Date'], data['Daily Return'], color='skyblue')
    plt.title('Daily Returns Over the Last Month')
    plt.xlabel('Date')
    plt.ylabel('Daily Return (%)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

def generate_report(symbol):
    # Fetch stock data
    stock_data = fetch_stock_data(symbol)

    # Perform analyses
    stats = descriptive_statistics(stock_data)
    returns_data = calculate_daily_returns(stock_data)
    ma_data = calculate_moving_averages(returns_data)
    volatility = calculate_volatility(returns_data)

    # Print the report
    print(f"\n--- Performance Report for {symbol} ---\n")
    print("Descriptive Statistics:")
    print(stats)
    
    print("\nVolatility (standard deviation of daily returns): {:.2f}%".format(volatility))

    # Plot trends and returns
    plot_price_trends(stock_data, symbol)
    plot_daily_returns(returns_data)

    # Prepare the paragraph for the Gemini API
    paragraph = (
        f"""Based on the analysis of the stock data for {symbol} over the past month, here are the key insights:\n
        Descriptive Statistics:\n{stats.to_string()}\n
        The volatility, represented by the standard deviation of daily returns, is {volatility:.2f}%. 
        Investors should consider this volatility when making decisions for the upcoming month. 
        It may be prudent to monitor market conditions and adjust strategies accordingly. 
        For the next month, a careful review of market trends and possible economic indicators will help in making informed investment decisions."""
    )

    # Generate a structured report using the Gemini API
    report = generate_report_gemini(paragraph)
    return report

def generate_report_gemini(paragraph):
    """Generate a structured paragraph using the Gemini API."""
    
    url = 'https://generativelanguage.googleapis.com/'  # Replace with your actual endpoint
    headers = {
        'Content-Type': 'application/json',
        'API-Key': 'AIzaSyBrs06KLgPusgvxpHM3V5J4VVYWaZ9qsXY',  # Replace with your Gemini API key
    }

    payload = {
        'text': paragraph,
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("Generated Report:")
        print(response.json())  # Print the structured response
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Example usage
stock_symbol = input("Enter the stock symbol: ")
generate_report(stock_symbol)
