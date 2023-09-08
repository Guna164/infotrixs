import requests
import json
import time
# Make a request to the weather API for the current weather data for a given city.
API_KEY="49d519d91d174024a21112322230809"
def get_weather_data(city):
    url = "https://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=yes".format(API_KEY,city)
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        raise Exception("API request failed")
# Print the weather information to the console.
def print_weather_data(data):
    print("City:{}".format(data["location"]["name"]))
    print("Temperature:{}°C".format(data["current"]["temp_c"]))
    print("Temperature:{}°F".format(data["current"]["temp_f"]))
    print("Humidity:{}%".format(data["current"]["humidity"]))
    print("Wind speed:{} m/h".format(data["current"]["wind_mph"]))
    print("Wind speed:{} km/h".format(data["current"]["wind_kph"]))
    print("Wind direction:{}".format(data["current"]["wind_dir"]))

# Create a list to store the favorite cities.
print("please enter the list of your favourite cities with spaces in between")
favourite_cities = [i for i in input().split()]
print(favourite_cities)
#data_validation
data_validation=False
while data_validation==False:
  city=input("please enter the city name: ")
  try:
    for character in city:
      if character.isalpha():
        data_validation=True
  except:
    print("only city names are accepted")
    break

#outcomes of the program
if data_validation==True:
    weather_data = get_weather_data(city)
    print_weather_data(weather_data)

# Add a city to the favourite list.

def add_city(city):
    favourite_cities.append(city)

# Remove a city from the favourite list.
def remove_city(city):
    favourite_cities.remove(city)

# Update the information for a city in the favourite list.
def update_city(city, new_data):
    for index, item in enumerate(favourite_cities):
        if item == city:
            favourite_cities[index] = new_data
            break

# Refresh the weather data every 30 seconds.
while True:
    if data_validation==True:
        weather_data = get_weather_data(city)
        time.sleep(30)


