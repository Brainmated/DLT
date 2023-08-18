import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error

data = pd.read_csv("data/test.csv", header=7)
print("CSV read")

country_names = data.iloc[:, 0].unique()
country = input("Type the country of the EU from which you want to generate a report: \n")

# Validate user input
while country not in country_names:
    print("Invalid country name. Please try again.")
    country = input("Type the country of the EU from which you want to generate a report: \n")

country_data = data[data.iloc[:, 0] == country]
print("Found", country)

# Assuming that the years begin from the second column and are every other column
years = data.columns[1::2]
print(years)

# Assuming that the year values are located right below the years row
consumption = country_data.iloc[:, 1::2].values
print(consumption)
consumption = consumption.astype(float)  # Converting the consumption values to float type
consumption = np.concatenate(consumption)
print("Found corresponding rows and columns")

# Splitting the data into training and testing sets
# Training data
train_size = int(len(consumption) * 0.8)  # The training set is 80% of the data
print("Training set size:", train_size)
train_years = years[:train_size]
print("Training set years:", len(train_years))
train_consumption = consumption[:train_size]
print("Consumption model trained")

# Testing data
test_years = ["2022", "2023", "2024", "2025", "2026"]  # Years for which you want to make predictions
print("Data tested")

# Fitting the ARIMA model
arima_model = sm.tsa.ARIMA(train_consumption, order=(1, 1, 1))
arima_model_fit = arima_model.fit()
print("ARIMA Model Trained")

''' Fitting the SARIMA model
sarima_model = SARIMAX(train_consumption, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
sarima_model_fit = sarima_model.fit()
print("SARIMA Model Trained")
'''

# Energy consumption estimation for upcoming years using ARIMA
arima_forecast = arima_model_fit.get_forecast(steps=len(test_years))
arima_predictions = arima_forecast.predicted_mean
print("Predicted Energy Consumption: ", arima_predictions)

''' Energy consumption estimation for upcoming years using SARIMA
sarima_forecast = sarima_model_fit.get_forecast(steps=len(test_years))
sarima_predictions = sarima_forecast.predicted_mean
'''

# Validation and Evaluation for ARIMA
arima_rmse = np.sqrt(mean_squared_error(consumption[train_size:], arima_predictions))
arima_mae = np.mean(np.abs(consumption[train_size:], arima_predictions))
arima_mape = np.mean(np.abs((consumption[train_size:], arima_predictions)))
# Validation and Evaluation for SARIMA
#sarima_rmse = np.sqrt(mean_squared_error(consumption[train_size:], sarima_predictions))

# Plot the actual and the predicted consumption
plt.figure(figsize=(10, 6))
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.plot(years, consumption, label="Actual")  # Plot all years
plt.plot(test_years, arima_predictions, label="ARIMA Predicted")  # Plot ARIMA predictions for test_years
#plt.plot(test_years, sarima_predictions, label="SARIMA Predicted")  # Plot SARIMA predictions for test_years
plt.xlabel("Year")
plt.ylabel("Energy Consumption in Tons of Oil")
plt.title("Energy Consumption Prediction for {} using ARIMA".format(country))
plt.legend()
plt.savefig("data/results/graphs/{}_{}.png".format(country, "prediction"))
print("ARIMA Root Mean Squared Error:", arima_rmse)
print("ARIMA Mean Absolute Error: ", arima_mae)
print("ARIMA Mean Absolute percentage Error: ", "{:.2f}".format(arima_mape),"%")
#print("SARIMA Root Mean Squared Error:", sarima_rmse)
