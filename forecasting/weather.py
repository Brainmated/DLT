import datetime as dt
import requests


base_url = "http://api.weatherapi.com/v1"

endpoint = "/current.json"
params = {
    "key": api_key,
    "q": "Paris",
    "days": 1
}

response = requests.get(base_url + endpoint, params=params)

data = response.json

if "forecast" in data.keys():
    forecast = data["forecast"]
    print(forecast)
else:
    print("Error retrieving weather forecast: ",data["error"]["message"])
