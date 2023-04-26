import requests


ip_response = requests.get('https://api.ipify.org?format=json')
public_ip = ip_response.json()['ip']
location_response = requests.get(f'http://ip-api.com/json/{public_ip}')
location_data = location_response.json()
zoom_level = 10
marker_label = 'IP'
marker_color = 'red'
map_url = f'https://www.google.com/maps/search/?api=1&query={location_data["lat"]},{location_data["lon"]}&zoom={zoom_level}&markers=color:{marker_color}|label:{marker_label}|{location_data["lat"]},{location_data["lon"]}'

print(f'Your public IP address is: {public_ip}')
print(f'You are located in {location_data["city"]}, {location_data["regionName"]}, {location_data["country"]}')
print(f'Here is a map of your location: {map_url}')

