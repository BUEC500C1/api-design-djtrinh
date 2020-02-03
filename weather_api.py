import pandas as pd
import json
from urllib.request import urlopen


class weather_api():

    def __init__(self):
        self.airports = pd.read_csv("airports.csv")

    def find_airport_read(self, code):
        data = self.airports[self.airports['iata_code'].str.contains(code.upper(), na=False)]

        if(data.empty):
            return -1
        else:
            return data.iloc[0, 4], data.iloc[0, 5]

    def get_weather(self, code):
        if (code.isalpha() is False):
            print("Please enter a valid airport code\n")
            return -1
        elif (len(code) != 3):
            print("Please enter a valid airport code\n")
            return -1

        loc = self.find_airport_read(code)

        if(loc == -1):
            print("Please enter a valid airport code\n")
            return -1
        else:
            response = urlopen('https://api.weather.gov/points/'
                               + str(loc[0])+','+str(loc[1]))
            data = json.load(response)
            url = data['properties']['forecastHourly']
            response = urlopen(url)
            data = json.load(response)
            return data
