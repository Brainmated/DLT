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

if "current" in response.keys():
    current = response["current"]
    temp = current["temp_c"]
    print("Current temperature in Paris:", temp)
else:
    print("Error retrieving weather forecast:", response["error"]["message"])
