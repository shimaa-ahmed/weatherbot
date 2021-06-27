# import required modules
import sys
import requests
import json

def main(dict):
    city=dict["location"]
    q=dict["weather"]
    response=requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=538fe22efbc50929ed599d1d8f3ed6e0")
    x = response.json()
    if x["cod"] != "404":
    	# store the value of "main"
    	# key in variable y
    	y = x["main"]
    	current_temperature = y["temp"]
    	current_pressure = y["pressure"]
    	current_humidity = y["humidity"]
    	z = x["weather"]
    	weather_description = z[0]["description"]
    	# print following values
    	print(" Temperature (in kelvin unit) = " +str(current_temperature) +"\n atmospheric pressure (in hPa unit) = " +str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidity) +"\n description = " +str(weather_description))
    	result ={"pressure":current_pressure,"humidity":current_humidity,"temperature":current_temperature,"condition":weather_description,"output":" Temperature (in kelvin unit) = " +str(current_temperature) +"\n Atmospheric Pressure (in hPa unit) = " +str(current_pressure) +"\n Humidity (in percentage) = " +str(current_humidity) +"\n Condition = " +str(weather_description)}
    	
    	   #result = {"temperature":current_temperature,"weather": weather_description,"pressure":current_pressure,"humidity":current_humidity}

    else:
        print(" City Not Found ")
    return result
