from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import joblib

app = Flask(__name__)

# Load the pre-trained model
loaded_model = joblib.load('model\linear_regression_model.pkl')

# Ensure these features match exactly what was used to train the model
expected_features = ["Prev_Open", "Prev_Close", "Prev_High", "Prev_Low", "Prev_Volume"]

def get_latest_stock_info(symbol):
    stock = yf.Ticker(symbol)
    # Get historical data for the last 5 days
    info = stock.history(period="5d")
    
    if len(info) < 2:
        return None  # Not enough data for prediction
    
    # Prepare the input data for prediction
    latest_info = {
        "Prev_Open": info["Open"].iloc[-2],  # Previous day's open
        "Prev_Close": info["Close"].iloc[-2], # Previous day's close
        "Prev_High": info["High"].iloc[-2],   # Previous day's high
        "Prev_Low": info["Low"].iloc[-2],     # Previous day's low
        "Prev_Volume": info["Volume"].iloc[-2] # Previous day's volume
    }
    return latest_info

def predict_open_price(symbol):
    latest_info = get_latest_stock_info(symbol)
    
    if latest_info is not None:
        # Prepare the input data for prediction
        input_data = pd.DataFrame([latest_info])
        
        # Ensure the model input is in the expected format
        if not input_data.empty and all(feature in input_data.columns for feature in expected_features):
            # Reorder columns to match expected features
            input_data = input_data[expected_features]
            predicted_open = loaded_model.predict(input_data)
            return predicted_open[0]
        else:
            return "No data available for prediction."
    else:
        return "No data found for the symbol."

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        prediction = predict_open_price(stock_symbol)
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
