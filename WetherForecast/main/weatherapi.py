import requests
import os
from datetime import datetime

def current_City(location):
    user_api= os.environ["CurrentWeather"]

    complete_api_link= "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
    print(complete_api_link)

    api_link= requests.get(complete_api_link)
    api_data= api_link.json()
    print(api_data)
    if api_data['cod'] == '400':
        print("Please enter a city name")
        return api_data
    if api_data['cod'] == "404":
        print ("Invalid City: {}, Please check you City name".format(location))
        return api_data
    else:
        temp_city= ((api_data['main']['temp'])-273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data[ 'wind' ]['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        print ("---------------------------------------------------------")
        print ("Weather Stats for - {}   ||   {} ".format(location.upper(), date_time))
        print ("----------------------------------------------------------------")
        print ("Current temperature is: {0:.2f} deg C".format(temp_city))
        print ("Current weather desc: ",weather_desc)
        print ("Current Humidity : ",hmdt,"%")
        print ("Current windspeed : ",wind_spd,"kmph")
    return api_data
  