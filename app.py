# from flask import Flask, render_template, request
# import yfinance as yf

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/recommend', methods=['POST'])
# def recommend():
#     # Capture user inputs from the form
#     risk_tolerance = request.form.get('risk_tolerance')
#     investment_duration = request.form.get('investment_duration')
    
#     # Set up recommended assets based on inputs
#     recommended_assets = []
    
#     if risk_tolerance == 'low':
#         if investment_duration == 'long-term':
#             recommended_assets = ["TCS.BO", "HDFC.BO"]
#         elif investment_duration == 'short-term':
#             recommended_assets = ["NTPC.BO", "ICICIBANK.BO"]
#     elif risk_tolerance == 'medium':
#         if investment_duration == 'long-term':
#             recommended_assets = ["RELIANCE.BO", "INFY.BO"]
#         elif investment_duration == 'short-term':
#             recommended_assets = ["HINDUNILVR.BO", "AXISBANK.BO"]
#     elif risk_tolerance == 'high':
#         if investment_duration == 'long-term':
#             recommended_assets = ["ADANIPORTS.BO", "BHARTIARTL.BO"]
#         elif investment_duration == 'short-term':
#             recommended_assets = ["MINDTREE.BO", "GAIL.BO"]

#     selected_assets = []

#     # Fetch data for each recommended asset
#     for symbol in recommended_assets:
#         stock = yf.Ticker(symbol)
#         stock_info = stock.history(period="1d")
        
#         if not stock_info.empty:
#             latest_data = stock_info.iloc[-1]
#             price = round(latest_data['Close'], 2)
#             previous_close = latest_data['Close'] if 'Close' in latest_data else price
#             change = round(((price - previous_close) / previous_close) * 100, 2) if previous_close else None
#             selected_assets.append({
#                 'symbol': symbol,
#                 'price': price,
#                 'change': change
#             })
#         else:
#             selected_assets.append({
#                 'symbol': symbol,
#                 'price': None,
#                 'change': None
#             })

#     return render_template('recommendations.html', selected_assets=selected_assets)

# if __name__ == "__main__":
#     app.run(debug=True)from flask import Flask, render_template, request
import yfinance as yf
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Capture user inputs from the form
    risk_tolerance = request.form.get('risk_tolerance')
    investment_duration = request.form.get('investment_duration')
    
    # Set up recommended assets based on inputs
    recommended_assets = []
        
    if risk_tolerance == 'low':
        if investment_duration == 'long-term':
            recommended_assets = [
                "TCS.BO", "HDFC.BO", "ITC.BO", "ASIANPAINT.BO", "HDFCBANK.BO",
                "LT.BO", "BRITANNIA.BO", "BAJAJFINSV.BO", "NESTLEIND.BO", "DRREDDY.BO",
                "HCLTECH.BO", "MARICO.BO", "GODREJCP.BO", "ULTRACEMCO.BO", "DMART.BO",
                "BAJFINANCE.BO", "PIDILITIND.BO", "HAVELLS.BO", "MRF.BO", "TITAN.BO"
            ]
        elif investment_duration == 'short-term':
            recommended_assets = [
                "NTPC.BO", "ICICIBANK.BO", "COALINDIA.BO", "ONGC.BO", "POWERGRID.BO",
                "NMDC.BO", "GRASIM.BO", "LICHSGFIN.BO", "NHPC.BO", "BPCL.BO",
                "GODREJPROP.BO", "SHREECEM.BO", "HINDPETRO.BO", "RECLTD.BO", "IOC.BO",
                "DABUR.BO", "BERGEPAINT.BO", "SUNTV.BO", "MCDOWELL-N.BO", "PETRONET.BO"
            ]

    elif risk_tolerance == 'medium':
        if investment_duration == 'long-term':
            recommended_assets = [
                "RELIANCE.BO", "INFY.BO", "WIPRO.BO", "SUNPHARMA.BO", "BAJAJ-AUTO.BO",
                "HINDUNILVR.BO", "TATASTEEL.BO", "MARUTI.BO", "M&M.BO", "SIEMENS.BO",
                "CIPLA.BO", "BATAINDIA.BO", "MOTHERSUMI.BO", "EICHERMOT.BO", "ONGC.BO",
                "COLPAL.BO", "AMBUJACEM.BO", "PFIZER.BO", "HINDZINC.BO", "TATAPOWER.BO"
            ]
        elif investment_duration == 'short-term':
            recommended_assets = [
                "AXISBANK.BO", "SBIN.BO", "JSWSTEEL.BO", "INDUSINDBK.BO", "ACC.BO",
                "HDFCAMC.BO", "EXIDEIND.BO", "LUPIN.BO", "APOLLOHOSP.BO", "TVSMOTOR.BO",
                "GAIL.BO", "BHARATFORG.BO", "UBL.BO", "ADANIGREEN.BO", "BOSCHLTD.BO",
                "FEDERALBNK.BO", "TATACHEM.BO", "MANAPPURAM.BO", "CUMMINSIND.BO", "BEL.BO"
            ]

    elif risk_tolerance == 'high':
        if investment_duration == 'long-term':
            recommended_assets = [
                "ADANIPORTS.BO", "BHARTIARTL.BO", "TATAMOTORS.BO", "VEDL.BO", "DLF.BO",
                "BANDHANBNK.BO", "IDEA.BO", "RBLBANK.BO", "IBULHSGFIN.BO", "TATACOMM.BO",
                "JINDALSTEL.BO", "FORTIS.BO", "IRCTC.BO", "MFSL.BO", "BHEL.BO",
                "ASHOKLEY.BO", "SAIL.BO", "INDIGO.BO", "AMARAJABAT.BO", "JSWENERGY.BO"
            ]
        elif investment_duration == 'short-term':
            recommended_assets = [
                "MINDTREE.BO", "GAIL.BO", "IDFC.BO", "BHEL.BO", "ESCORTS.BO",
                "NATIONALUM.BO", "ADANIPOWER.BO", "TATASPONGE.BO", "ZEEL.BO", "DELTACORP.BO",
                "JPPOWER.BO", "JPASSOCIAT.BO", "SOUTHBANK.BO", "YESBANK.BO", "ABFRL.BO",
                "INDOCO.BO", "IRB.BO", "SUZLON.BO", "HFCL.BO", "SUNTECK.BO"
            ]

    selected_assets = []

    # Fetch data for each recommended asset
    for symbol in recommended_assets:
        stock = yf.Ticker(symbol)
        stock_info = stock.history(period="5d")  # Fetch the last 2 days for comparison

        # Check if stock_info is not empty and has at least 2 entries
        if stock_info.empty or len(stock_info) < 2:
            selected_assets.append({
                'symbol': symbol,
                'price': None,
                'change': None,
                'message': 'Data not available for this stock'
            })
            continue

        latest_data = stock_info.iloc[-1]
        previous_data = stock_info.iloc[-2]
        price = round(latest_data['Close'], 2)
        previous_close = round(previous_data['Close'], 2)
        change = round(((price - previous_close) / previous_close) * 100, 2) if previous_close else None
        
        selected_assets.append({
            'symbol': symbol,
            'price': price,
            'change': change,
            'message': None
        })

    return render_template('recommendations.html', selected_assets=selected_assets)

if __name__ == "__main__":
    app.run(debug=True)
