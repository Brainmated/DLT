import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.api import SimpleExpSmoothing
from sklearn.metrics import mean_absolute_error

data = pd.read_csv("data/greenhouse.csv", header=7)

country = input("Type the country of the EU from which you want to generate a report: \n")

country_names = data.iloc[:, 0].unique()

# Validate user input
while country not in country_names:
    print("Invalid country name. Please try again.")
    country = input("Type the country of the EU from which you want to generate a report: \n")

country_data = data[data.iloc[:, 0] == country]
print("Found", country)
years = data.columns[1:]
sma_years = data.columns[13:]
print("Years: ", years)
emissions = country_data.iloc[:, 1:].values
emissions = emissions.astype(float)
emissions = np.concatenate(emissions)

# Fill missing values with forward fill
emissions = pd.Series(emissions).fillna(method='ffill').values

#
arima_model = ARIMA(emissions[:-1], order=(1, 1, 1))
arima_model_fit = arima_model.fit()

# Simple Moving Average (SMA)
sma_predictions = pd.Series(emissions).rolling(window=10).mean() #last 10 years

# Exponential Smoothing (ES)
es_model = SimpleExpSmoothing(emissions)
es_predictions = es_model.fit(smoothing_level=0.6).forecast(steps=5)

future_years = ["2022", "2023", "2024", "2025", "2026"]
predictions = []

for year in future_years:
    next_year_prediction = arima_model_fit.forecast(steps=1)[0]
    predictions.append(next_year_prediction)
    emissions = np.append(emissions, next_year_prediction)
    arima_model = ARIMA(emissions, order=(1, 1, 1))
    arima_model_fit = arima_model.fit()

for year, prediction in zip(future_years, predictions):
    print(f"Prediction for {year}: {prediction}")

# Split data into training and test sets
train_years = years[:-5]  # Use all years except the last 5 as training data
test_years = years[-5:]  # Use the last 5 years as test data
train_emissions = emissions[:len(train_years)]
test_emissions = emissions[len(train_years):]

# Make predictions on test data
test_predictions = arima_model_fit.forecast(steps=len(test_years))[0]

all_years = np.concatenate((years, future_years))
all_emissions = np.concatenate((emissions[:len(years)], predictions))


# Train ARIMA model on training data
arima_model = ARIMA(train_emissions[:-1], order=(1, 1, 1))
arima_model_fit = arima_model.fit()

# Make predictions on test data
test_predictions = []
for _ in range(len(test_years)):
    next_year_prediction = arima_model_fit.forecast(steps=1)[0]
    test_predictions.append(next_year_prediction)
    train_emissions = np.append(train_emissions, next_year_prediction)
    arima_model = ARIMA(train_emissions, order=(1, 1, 1))
    arima_model_fit = arima_model.fit()

# Calculate MAE
mae = mean_absolute_error(emissions[len(years):], test_predictions)
print("Mean Absolute Error (MAE):", mae)

plt.figure(figsize=(15, 6))
plt.plot(years, emissions[:len(years)], label="Emissions")
plt.plot(future_years, predictions, label="Future Emissions", color="red")  
plt.plot(future_years, es_predictions, label="ES Predictions", color="green")
plt.plot(sma_years, sma_predictions[:len(sma_years)], label="SMA Predictions", color="yellow")
plt.xlabel("Years")
plt.ylabel("Emissions")
plt.title(f"Emissions for {country}\n MAE: {mae}")
plt.xticks(rotation=45)
plt.legend()

plt.savefig("results/graphs/{}_{}.png".format(country, "emissions"))

