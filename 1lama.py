import yfinance as yf
import matplotlib.pyplot as plt
import mpld3  # For embedding matplotlib plots in HTML
import pandas as pd
from io import StringIO
import base64

# Fetch stock data
def fetch_stock_data(symbol):
    try:
        stock_data = yf.download(symbol, period='1mo')
        stock_data.reset_index(inplace=True)
        return stock_data
    except Exception as e:
        print(f"Error fetching stock data for {symbol}: {e}")
        return None

# Descriptive statistics
def descriptive_statistics(data):
    stats = data[['Open', 'High', 'Low', 'Close', 'Volume']].describe()
    return stats

# Calculate daily returns
def calculate_daily_returns(data):
    data['Daily Return'] = data['Close'].pct_change() * 100
    return data

# Calculate moving averages
def calculate_moving_averages(data):
    data['3-Day MA'] = data['Close'].rolling(window=3).mean()
    data['7-Day MA'] = data['Close'].rolling(window=7).mean()
    return data

# Plotting function, returns HTML string of plot
def plot_price_trends_html(data, symbol):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data['Date'], data['Close'], marker='o', label='Close Price')
    ax.set_title(f'{symbol} Closing Price Trend Over the Last Month')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    plt.xticks(rotation=45)
    plt.grid()
    
    # Convert the plot to HTML using mpld3
    html_str = mpld3.fig_to_html(fig)
    plt.close(fig)  # Close the figure after converting to HTML
    return html_str

# Generate report and HTML table
def generate_report(symbol):
    stock_data = fetch_stock_data(symbol)
    if stock_data is None:
        return f"<p>Error fetching stock data for {symbol}</p>"

    # Perform calculations
    stats = descriptive_statistics(stock_data)
    stock_data = calculate_daily_returns(stock_data)
    stock_data = calculate_moving_averages(stock_data)

    # Generate HTML plot
    plot_html = plot_price_trends_html(stock_data, symbol)
    
    # Convert descriptive statistics to HTML
    stats_html = stats.to_html()

    # Combine everything into a single HTML structure
    report_html = f"""
    <h2>Performance Report for {symbol}</h2>
    <h3>Descriptive Statistics</h3>
    {stats_html}
    <h3>Closing Price Trend</h3>
    {plot_html}
    <br><hr>
    """
    return report_html

# Generate an HTML report for multiple stocks and save to file
def generate_full_report(symbols):
    full_html = "<html><head><title>Stock Report</title></head><body>"
    for symbol in symbols:
        full_html += generate_report(symbol)
    full_html += "</body></html>"

    # Save to an HTML file
    with open("stock_report.html", "w") as f:
        f.write(full_html)
    print("Report generated and saved as 'stock_report.html'.")

# List of stocks to analyze
symbols = ["TCS.BO", "HDFC.BO", "RELIANCE.BO", "ADANIPORTS.BO"]

# Generate report
generate_full_report(symbols)
        