import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Load data from CSV
data = pd.read_csv("data/greenhouse.csv", header=8)

# Extract unique country names
countries = data.iloc[:, 0].unique()

# Create a DataFrame to store the predictions
predictions_df = pd.DataFrame({'Country': countries})

# Iterate over countries and make predictions
for country in countries:
    # Filter data for the current country
    country_data = data[data['Country'] == country]
  
    # Extract years and emissions for the current country
    years = country_data['Year']
    emissions = country_data['Emissions']
  
    # Train the model and make predictions for future years
    model = ARIMA(emissions, order=(1, 0, 0), seasonal_order=(1, 1, 1, 12))
    model_fit = model.fit()
    future_years = list(range(2022, 2027))
    predictions = model_fit.predict(start=len(emissions), end=len(emissions) + len(future_years) - 1)
  
    # Store the predictions in the DataFrame
    predictions_df.loc[predictions_df['Country'] == country, '2022'] = predictions[0]
    predictions_df.loc[predictions_df['Country'] == country, '2023'] = predictions[1]
    predictions_df.loc[predictions_df['Country'] == country, '2024'] = predictions[2]
    predictions_df.loc[predictions_df['Country'] == country, '2025'] = predictions[3]
    predictions_df.loc[predictions_df['Country'] == country, '2026'] = predictions[4]

# Save the predictions to a CSV file
predictions_df.to_csv("results/predictions.csv", index=False)