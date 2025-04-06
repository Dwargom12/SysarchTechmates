# Team: Tech Mate
# Team Members: 
# Derick Aton
# Ed Francis C. Librando 
# Honeyzenth Flores 
# James David A Guba
import requests
import folium

def get_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    lat = float(data['iss_position']['latitude'])
    lon = float(data['iss_position']['longitude'])
    return lat, lon

def create_iss_map(lat, lon):
    # Create a world map centered around the ISS
    m = folium.Map(location=[lat, lon], zoom_start=2)
    folium.Marker([lat, lon], tooltip="🛰️ ISS is here!").add_to(m)
    m.save("iss_map.html")
    print("Map saved as iss_map.html")

if __name__ == "__main__":
    print("Fetching ISS location...")
    lat, lon = get_iss_location()
    print(f"Current ISS location: Latitude {lat:.2f}, Longitude {lon:.2f}")
    create_iss_map(lat, lon)
