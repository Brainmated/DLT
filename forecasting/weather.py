import datetime as dt
import requests

base_url = "http://api.weatherapi.com/v1/forecast.json?key=aa45f6330f334a29afd163712232010&q=London&days=1&aqi=no&alerts=no"

endpoint = "/forecast.json"
params = {
    "key": api_key,
    "q": "146.8333333, 43.86666667",
    "days": 1
}

response = requests.get(base_url + endpoint, params=params)

data = response.json

if "forecast" in data.keys():
    forecast = data["forecast"]
    print(forecast)
else:
    print("Error retrieving weather forecast: ",data["error"]["message"])
