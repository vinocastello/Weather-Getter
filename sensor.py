import requests, json
import random

LOCATION = (14.648900271585852, 121.06881775671476)

def KelvinToCelsius(temp):
    return round(temp - 273.15,2)
14.648900271585852, 121.06881775671476
def get_weather(loc):
    my_api_key = "05ee991c43ccaeba6a9221e4c2b2b5da"
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={loc}&appid={my_api_key}&units=metric"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LOCATION[0]}&lon={LOCATION[1]}&appid={my_api_key}"
    res = requests.get(url)
    data = res.json()
    # print(f"data = {data}")
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = KelvinToCelsius(data['main']['temp'])
    max_temp = KelvinToCelsius(data['main']['temp_max'])
    min_temp = KelvinToCelsius(data['main']['temp_min'])
    loc_name = data['name']
    # print(f"data = {data}")
    print(f"Location: {loc_name}\nTemperature: {temp} °C\nTemp range: {min_temp} - {max_temp}°C\nWind: {wind}\nPressure: {pressure} Pa\nHumidity: {humidity}%\nDescription: {description}")
    print("Random temperature")
    for i in range(5):
        print(f"temp {i+1}: {round(random.uniform(min_temp,max_temp),2)}")
    # return f"Temperature: {temp} °C\nWind: {wind}\nPressure: {pressure} Pa\nHumidity: {humidity}%\nDescription: {description}"

# print(get_weather(LOCATION))
get_weather(LOCATION)