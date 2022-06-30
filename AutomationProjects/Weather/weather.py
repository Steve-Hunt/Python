import sys
import json
import requests

API_KEY = "1ea03a5ebab2c06b1f2f1acdb4118ee1"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
SAVED_DATA = "weather.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) < 2:
    print("Location required.  e.g. 'Bracknell' or 'Cambridge, UK'" )
    city = input("Enter the location(City/Town) for the weather info: ")
else:
    city = sys.argv[1]
    if len(sys.argv) > 2:
        city +=  ", " 
        city += sys.argv[2]

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    
    save_data(SAVED_DATA, data)
        
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    country = data['sys']['country']
    print("|----------")
    print("| Data For:", city)
    print ("| Country:", country)
    print("| Weather:", weather)
    print("| Temperature:", temperature, "celcius")
    print("|----------")
else:
    print("An error occured!")