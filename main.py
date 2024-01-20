import requests

api_key = "693b18f634973cb7b7365fe26e55823e"

paraments = {
    "lat": 34.07,
    "lon": 136.19,
    "appid": "693b18f634973cb7b7365fe26e55823e",
    "cnt":3
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=paraments, verify=False)
response.raise_for_status()
data = response.json()
# weather_id = data["list"][0]["weather"][0]["id"]
will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain = True
if will_rain:
    print("Bring an urmnrella.")