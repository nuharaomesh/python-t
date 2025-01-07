import requests
import json

def fetch_weather(latitude, longitude, current):
    
    url = 'https://api.open-meteo.com/v1/forecast'

    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current': current
    }

    resp = requests.get(url, params=params)

    if resp.status_code == 200:
        
        print("Fetch Success")
        weather_info = resp.json()
        return weather_info
    else:
        print('Error happened!')
        return None
        
def parse_weather_data(weather_data):
    
    if weather_data:
        temperature = weather_data['current']['temperature_2m']
        wind_speed = weather_data['current']['wind_speed_10m']
        
        print("Current temperature:", temperature)
        print("Current Wind speed:", wind_speed)
        
        return temperature, wind_speed

weather_data = fetch_weather(6.71130, 79.90993, 'temperature_2m,wind_speed_10m')
parse_weather_data(weather_data)

# with open('/home/omesh/vs code/intro-to-python2/exercises/weather_data.json', 'w+') as file:
#     data = weather_data
#     json_data = json.dumps(data, indent=0)
#     file.write(json_data)