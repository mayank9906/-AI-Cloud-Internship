import requests

# Pune Coordinates
latitude = 18.5204
longitude = 73.8567

url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

try:
    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        current = data["current"]

        print("===== Current Weather =====")
        print("Latitude :", latitude)
        print("Longitude:", longitude)
        print("Temperature :", current["temperature_2m"], "°C")
        print("Humidity    :", current["relative_humidity_2m"], "%")
        print("Wind Speed  :", current["wind_speed_10m"], "km/h")

    else:
        print("Failed to fetch weather data.")
        print("Status Code:", response.status_code)

except Exception as e:
    print("Error:", e)