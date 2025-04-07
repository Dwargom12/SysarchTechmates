# Team: Tech Mates
# Team Members: 
# Derick Aton
# Ed Francis C. Librando 
# Honeyzenth Flores 
# James David A Guba
import requests
import folium
from geopy.distance import geodesic
import datetime
import csv

# === CONFIG ===
LOG_FILE = "iss_log.csv"
MAP_FILE = "iss_map.html"
YOUR_LOCATION = (37.7749, -122.4194)  # San Francisco

# === Get current ISS location ===
def get_iss_location():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        lat = float(data['iss_position']['latitude'])
        lon = float(data['iss_position']['longitude'])
        return lat, lon
    except Exception as e:
        print("Error fetching ISS location:", e)
        return None, None

# === Get astronaut info ===
def get_astronauts():
    try:
        response = requests.get("http://api.open-notify.org/astros.json")
        response.raise_for_status()
        data = response.json()
        return data['people'], data['number']
    except Exception as e:
        print("Error fetching astronaut data:", e)
        return [], 0

# === Calculate distance from user ===
def calculate_distance(from_loc, to_loc):
    try:
        return geodesic(from_loc, to_loc).km
    except Exception as e:
        print("Error calculating distance:", e)
        return None

# === Save to CSV log ===
def log_position(lat, lon):
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.datetime.now().isoformat(), lat, lon])
    print(f"Logged coordinates: ({lat}, {lon})")

# === Create and save map ===
def create_map(lat, lon):
    m = folium.Map(location=[lat, lon], zoom_start=2)
    folium.Marker([lat, lon], tooltip="🛰 ISS Location").add_to(m)
    m.save(MAP_FILE)
    print(f"Map saved to {MAP_FILE}")

# === Main script ===
if __name__ == "__main__":
    print("Fetching ISS data...\n")

    lat, lon = get_iss_location()
    if lat is not None:
        print(f"ISS Location → Latitude: {lat:.2f}, Longitude: {lon:.2f}")

        # Distance from you
        distance = calculate_distance(YOUR_LOCATION, (lat, lon))
        if distance:
            print(f"Distance from you: {distance:.2f} km")

        # Astronauts
        astronauts, count = get_astronauts()
        print(f"There are {count} people in space:")
        for astro in astronauts:
            print(f" - {astro['name']} on {astro['craft']}")

        # Log + Map
        log_position(lat, lon)
        create_map(lat, lon)

    else:
        print("Failed to get ISS data.")
