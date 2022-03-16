import requests
import os
from datetime import datetime
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)
def current_City(location):
    user_api= os.environ["CurrentWeather"]

    complete_api_link= "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
    logging.debug(complete_api_link)

    api_link= requests.get(complete_api_link)
    api_data= api_link.json()
    if api_data['cod'] == '400':
        logging.debug("Please enter a city name")
        return api_data
    if api_data['cod'] == "404":
        logging.debug ("Invalid City: {}, Please check you City name".format(location))
        return api_data
    else:
        temp_city= ((api_data['main']['temp'])-273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data[ 'wind' ]['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        logging.debug ("---------------------------------------------------------")
        logging.debug ("Weather Stats for - {}   ||   {} ".format(location.upper(), date_time))
        logging.debug ("----------------------------------------------------------------")
        logging.debug ("Current temperature is: {0:.2f} deg C".format(temp_city))
        logging.debug ("Current weather desc: {} ".format(weather_desc))
        logging.debug ("Current Humidity : {}%".format(hmdt))
        logging.debug ("Current windspeed : {}kmph".format(wind_spd))
    return api_data
  