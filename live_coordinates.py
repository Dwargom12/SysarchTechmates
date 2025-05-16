import requests
import time

def get_iss_position():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()

    position = data['iss_position']
    latitude = position['latitude']
    longitude = position['longitude']
    return latitude, longitude

print("Fetching live ISS coordinates every 5 seconds...\n")
while True:
    lat, lon = get_iss_position()
    print(f"Latitude: {lat}, Longitude: {lon}")
    time.sleep(5)
