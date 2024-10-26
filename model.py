import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib  # Import joblib for saving the model
import pickle

# Step 1: Load the dataset
data = pd.read_csv("C:\\Users\\mahes\\OneDrive\\Desktop\\hack1 - Copy\\stock_market_india.csv")

# Step 2: Feature Engineering
data['Prev_Open'] = data['Open'].shift(1)
data['Prev_Close'] = data['Close'].shift(1)
data['Prev_High'] = data['High'].shift(1)
data['Prev_Low'] = data['Low'].shift(1)
data['Prev_Volume'] = data['Volume'].shift(1)

data = data.dropna()

# Step 3: Define features and target variable
X = data[['Prev_Open', 'Prev_Close', 'Prev_High', 'Prev_Low', 'Prev_Volume']]
y = data['Open']

# Step 4: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Save the model
joblib.dump(model, 'Tata Consultancy Services (TCS)_linear_regression_model.pkl')  # Save the model

# Step 7: Make predictions
y_pred = model.predict(X_test)

# Step 8: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f'RMSE: {rmse}')

# Step 9: Predict the Open price for tomorrow based on the last available row
last_row = data.iloc[-1][['Open', 'Close', 'High', 'Low', 'Volume']].values
input_data = np.array([[last_row[0], last_row[1], last_row[2], last_row[3], last_row[4]]])
predicted_open = model.predict(input_data)
print(f'Predicted Open price for tomorrow: {predicted_open[0]}')





# Optional: Loading the model later
loaded_model = joblib.load('linear_regression_model.pkl')  # Load the model
predicted_open_loaded = loaded_model.predict(input_data)  # Use loaded model for prediction
print(f'Predicted Open price for tomorrow using loaded model: {predicted_open_loaded[0]}')
