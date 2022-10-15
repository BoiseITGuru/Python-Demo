import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time

notificationObject = ToastNotifier()


def getWeather(link):
    info = requests.get(link)
    return info.text


data = getWeather('https://forecast.weather.gov/MapClick.php?CityName=Boulder&state=CO&site=BOU&lat=40.0269&lon=-105.251#.YPCAZOhKg2w')
parsed = BeautifulSoup(data, 'html.parser')

currentTemp = parsed.find_all(class_="myforecast-current-lrg")
Temp = (str(currentTemp))
Temp = Temp[35:39]

result = "The current temperature is: " + Temp + "in Boulder Colorado"
notificationObject.show_toast("Weather Update", result, duration=15)
time.sleep(60*60*40)

