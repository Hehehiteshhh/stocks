import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib  # Import joblib for saving the model

# Step 1: Load the dataset
data = pd.read_csv("C:\\Users\\mahes\\OneDrive\\Desktop\\hack1 - Copy\\stock_market_india.csv")

# Step 2: Feature Engineering
data['Prev_Open'] = data['Open'].shift(1)
data['Prev_Close'] = data['Close'].shift(1)
data['Prev_High'] = data['High'].shift(1)
data['Prev_Low'] = data['Low'].shift(1)
data['Prev_Volume'] = data['Volume'].shift(1)

# Drop rows with NaN values
data = data.dropna()

# Step 3: Train the model for each company
companies = data['Company'].unique()

for company in companies:
    company_data = data[data['Company'] == company]

    # Define features and target variable
    X = company_data[['Prev_Open', 'Prev_Close', 'Prev_High', 'Prev_Low', 'Prev_Volume']]
    y = company_data['Open']

    # Step 4: Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 5: Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Step 6: Save the model
    joblib.dump(model, f'{company}_linear_regression_model.pkl')  # Save the model with company name

    # Step 7: Make predictions
    y_pred = model.predict(X_test)

    # Step 8: Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    print(f'RMSE for {company}: {rmse}')

# Optional: You can now load each model later using:
# loaded_model = joblib.load(f'{company}_linear_regression_model.pkl')
