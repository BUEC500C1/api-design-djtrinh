# Weather API

### Introduction

In this API, the weather information is obtained from the National Weeather Service. The user is able to obtain a week weather forcast or a full day hourly forecast with an airport IATA code as the input. The reason why we chose the NWS instead of OpenWeather because of the lack of limitations in how many times data could be fetched. Also, hour by hour weather information is possible with the NWS information whereas OpenWeather would require paying for such a feature. Another advantage of the NWS API is that no key is required.

### How to test

There is a command line interface written to help evaluate the API module. The CLI program takes in an IATA code and provides the hourly data plotted. To run the test program, enter the following:

```python

python main.py

```

The following is a snippet of the CLI interface:


### About the API

The weekly weather is presented in a JSON format. An example of two days is as follows:

```JSON

{
  "@context": [
    "https://raw.githubusercontent.com/geojson/geojson-ld/master/contexts/geojson-base.jsonld",
    {
      "wx": "https://api.weather.gov/ontology#",
      "geo": "http://www.opengis.net/ont/geosparql#",
      "unit": "http://codes.wmo.int/common/unit/",
      "@vocab": "https://api.weather.gov/ontology#"
    }
  ],
  "type": "Feature",
  "geometry": {
    "type": "GeometryCollection",
    "geometries": [
      {
        "type": "Point",
        "coordinates": [
          -97.094408400000006,
          39.7559738
        ]
      },
      {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -97.1089731,
              39.766826299999998
            ],
            [
              -97.108526900000001,
              39.744778799999999
            ],
            [
              -97.079846700000004,
              39.745119500000001
            ],
            [
              -97.08028680000001,
              39.767167000000001
            ],
            [
              -97.1089731,
              39.766826299999998
            ]
          ]
        ]
      }
    ]
  },
  "properties": {
    "updated": "2020-02-03T17:10:10+00:00",
    "units": "us",
    "forecastGenerator": "BaselineForecastGenerator",
    "generatedAt": "2020-02-03T17:43:13+00:00",
    "updateTime": "2020-02-03T17:10:10+00:00",
    "validTimes": "2020-02-03T11:00:00+00:00/P7DT14H",
    "elevation": {
      "value": 441.96000000000004,
      "unitCode": "unit:m"
    },
    "periods": [
      {
        "number": 1,
        "name": "Today",
        "startTime": "2020-02-03T11:00:00-06:00",
        "endTime": "2020-02-03T18:00:00-06:00",
        "isDaytime": true,
        "temperature": 33,
        "temperatureUnit": "F",
        "temperatureTrend": null,
        "windSpeed": "15 to 20 mph",
        "windDirection": "N",
        "icon": "https://api.weather.gov/icons/land/day/fzra,20?size=medium",
        "shortForecast": "Slight Chance Freezing Rain",
        "detailedForecast": "A slight chance of freezing rain before 1pm. Cloudy, with a high near 33. North wind 15 to 20 mph, with gusts as high as 30 mph. Chance of precipitation is 20%."
      },
      {
        "number": 2,
        "name": "Tonight",
        "startTime": "2020-02-03T18:00:00-06:00",
        "endTime": "2020-02-04T06:00:00-06:00",
        "isDaytime": false,
        "temperature": 21,
        "temperatureUnit": "F",
        "temperatureTrend": null,
        "windSpeed": "15 mph",
        "windDirection": "N",
        "icon": "https://api.weather.gov/icons/land/night/ovc/snow,20?size=medium",
        "shortForecast": "Cloudy then Slight Chance Light Snow",
        "detailedForecast": "A slight chance of snow after 3am. Cloudy, with a low around 21. North wind around 15 mph, with gusts as high as 25 mph. Chance of precipitation is 20%."
      },
      {
        "number": 3,
        "name": "Tuesday",
        "startTime": "2020-02-04T06:00:00-06:00",
        "endTime": "2020-02-04T18:00:00-06:00",
        "isDaytime": true,
        "temperature": 26,
        "temperatureUnit": "F",
        "temperatureTrend": null,
        "windSpeed": "15 to 20 mph",
        "windDirection": "N",
        "icon": "https://api.weather.gov/icons/land/day/snow,40?size=medium",
        "shortForecast": "Chance Light Snow",
        "detailedForecast": "A chance of snow. Cloudy, with a high near 26. North wind 15 to 20 mph, with gusts as high as 30 mph. Chance of precipitation is 40%. New snow accumulation of less than one inch possible."
      },
      {
        "number": 4,
        "name": "Tuesday Night",
        "startTime": "2020-02-04T18:00:00-06:00",
        "endTime": "2020-02-05T06:00:00-06:00",
        "isDaytime": false,
        "temperature": 18,
        "temperatureUnit": "F",
        "temperatureTrend": null,
        "windSpeed": "5 to 15 mph",
        "windDirection": "N",
        "icon": "https://api.weather.gov/icons/land/night/snow,20/bkn?size=medium",
        "shortForecast": "Slight Chance Light Snow then Mostly Cloudy",
        "detailedForecast": "A slight chance of snow before midnight. Mostly cloudy, with a low around 18. North wind 5 to 15 mph. Chance of precipitation is 20%. New snow accumulation of less than half an inch possible."
      }]
   }
}

```

The hourly format with a couple hours is as follows:

```JSON

{
  "@context": [
    "https://raw.githubusercontent.com/geojson/geojson-ld/master/contexts/geojson-base.jsonld",
    {
      "wx": "https://api.weather.gov/ontology#",
      "geo": "http://www.opengis.net/ont/geosparql#",
      "unit": "http://codes.wmo.int/common/unit/",
      "@vocab": "https://api.weather.gov/ontology#"
    }
  ],
  "type": "Feature",
  "geometry": {
    "type": "GeometryCollection",
    "geometries": [
      {
        "type": "Point",
        "coordinates": [
          -97.094408400000006,
          39.7559738
        ]
      },
      {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -97.1089731,
              39.766826299999998
            ],
            [
              -97.108526900000001,
              39.744778799999999
            ],
            [
              -97.079846700000004,
              39.745119500000001
            ],
            [
              -97.08028680000001,
              39.767167000000001
            ],
            [
              -97.1089731,
              39.766826299999998
            ]
          ]
        ]
      }
    ]
  },
  "properties": {
    "updated": "2020-02-03T17:10:10+00:00",
    "units": "us",
    "forecastGenerator": "HourlyForecastGenerator",
    "generatedAt": "2020-02-03T17:58:16+00:00",
    "updateTime": "2020-02-03T17:10:10+00:00",
    "validTimes": "2020-02-03T11:00:00+00:00/P7DT14H",
    "elevation": {
      "value": 441.96000000000004,
      "unitCode": "unit:m"
    },
    "periods": [
      {
        "number": 1,
        "name": "",
        "startTime": "2020-02-03T11:00:00-06:00",
        "endTime": "2020-02-03T12:00:00-06:00",
        "isDaytime": true,
        "temperature": 32,
        "temperatureUnit": "F",
        "temperatureTrend": null,
        "windSpeed": "20 mph",
        "windDirection": "N",
        "icon": "https://api.weather.gov/icons/land/day/fzra,20?size=small",
        "shortForecast": "Slight Chance Freezing Rain",
        "detailedForecast": ""
      },
      {
        "number": 2,
        "name": "",
        "startTime": "2020-02-03T12:00:00-06:00",
        "endTime": "2020-02-03T13:00:00-06:00",
        "isDaytime": true,
        "temperature": 32,
        "temperatureUnit": "F",
        "temperatureTrend": null,
        "windSpeed": "20 mph",
        "windDirection": "N",
        "icon": "https://api.weather.gov/icons/land/day/fzra,20?size=small",
        "shortForecast": "Slight Chance Freezing Rain",
        "detailedForecast": ""
      }]
    }
  }

```

In order to run the API there is one method to obtain weather information. It takes in the IATA code as the first parameter and the weather data type as weekly (0) or hourly (1).

```python
import weather_api as api

weather = api()
weather.get_weather('LAX', 1);

```

Invalid IATAs such as characters longer than 3 letters, numbers in IATA, symbols in IATA will return a -1 to signify IATA code errors.

