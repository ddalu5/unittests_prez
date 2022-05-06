from unittest import mock
from unittest import TestCase

from app.sdk import MetaWeather
from app.sdk import Team, Human
from app.exceptions import ResultNotFoundError
from app.exceptions import MetaWeatherAPIUnreachableError


def mocked_requests_get(*args, **kwargs):
    """
    Used to mock requests.get Response
    :param args:
    :param kwargs:
    :return:
    """

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if kwargs["url"] == "https://www.metaweather.com/api/location/15015370/":
        return MockResponse({"detail": "Not found"}, 404)
    elif kwargs["url"] == "http://www.metaweather.com/api/not_url/0/":
        raise Exception("URL unreachable")
    elif kwargs["url"] == "https://www.metaweather.com/api/location/99/":
        return MockResponse(
                {
                    "consolidated_weather": [
                        {
                            "id": 5464516864245760,
                            "weather_state_name": "Light Rain",
                            "weather_state_abbr": "lr",
                            "wind_direction_compass": "NE",
                            "created": "2022-05-03T06:59:01.586418Z",
                            "applicable_date": "2022-05-03",
                            "min_temp": 8.955,
                            "max_temp": 16.259999999999998,
                            "the_temp": 13.995000000000001,
                            "wind_speed": 3.8144267555767652,
                            "wind_direction": 40.78154971274732,
                            "air_pressure": 1021.5,
                            "humidity": 76,
                            "visibility": 7.495290006362842,
                            "predictability": 75,
                        },
                        {
                            "id": 5021636781670400,
                            "weather_state_name": "Light Rain",
                            "weather_state_abbr": "lr",
                            "wind_direction_compass": "W",
                            "created": "2022-05-03T06:59:01.971355Z",
                            "applicable_date": "2022-05-04",
                            "min_temp": 9.49,
                            "max_temp": 17.57,
                            "the_temp": 17.02,
                            "wind_speed": 5.825482604745619,
                            "wind_direction": 263.0279907236704,
                            "air_pressure": 1018.5,
                            "humidity": 67,
                            "visibility": 9.568184303666587,
                            "predictability": 75,
                        },
                        {
                            "id": 6227192863260672,
                            "weather_state_name": "Heavy Cloud",
                            "weather_state_abbr": "hc",
                            "wind_direction_compass": "W",
                            "created": "2022-05-03T06:59:01.948218Z",
                            "applicable_date": "2022-05-05",
                            "min_temp": 8.434999999999999,
                            "max_temp": 19.775,
                            "the_temp": 19.57,
                            "wind_speed": 4.749838222736551,
                            "wind_direction": 281.155143579782,
                            "air_pressure": 1023.5,
                            "humidity": 56,
                            "visibility": 14.265129145788594,
                            "predictability": 71,
                        },
                        {
                            "id": 6744614351405056,
                            "weather_state_name": "Light Rain",
                            "weather_state_abbr": "lr",
                            "wind_direction_compass": "WNW",
                            "created": "2022-05-03T06:59:01.980403Z",
                            "applicable_date": "2022-05-06",
                            "min_temp": 10.555,
                            "max_temp": 19.185,
                            "the_temp": 18.395,
                            "wind_speed": 6.2345527280972455,
                            "wind_direction": 287.38233632142305,
                            "air_pressure": 1024.5,
                            "humidity": 69,
                            "visibility": 12.558533166308756,
                            "predictability": 75,
                        },
                        {
                            "id": 4541891786833920,
                            "weather_state_name": "Showers",
                            "weather_state_abbr": "s",
                            "wind_direction_compass": "NE",
                            "created": "2022-05-03T06:59:01.891863Z",
                            "applicable_date": "2022-05-07",
                            "min_temp": 8.865,
                            "max_temp": 16.564999999999998,
                            "the_temp": 15.585,
                            "wind_speed": 5.80370938900289,
                            "wind_direction": 41.77573823700348,
                            "air_pressure": 1029.5,
                            "humidity": 58,
                            "visibility": 12.851820369044777,
                            "predictability": 73,
                        },
                        {
                            "id": 5112684350537728,
                            "weather_state_name": "Light Cloud",
                            "weather_state_abbr": "lc",
                            "wind_direction_compass": "E",
                            "created": "2022-05-03T06:59:05.069424Z",
                            "applicable_date": "2022-05-08",
                            "min_temp": 5.965,
                            "max_temp": 16.435000000000002,
                            "the_temp": 15.19,
                            "wind_speed": 3.964681857949574,
                            "wind_direction": 89.5,
                            "air_pressure": 1031.0,
                            "humidity": 50,
                            "visibility": 9.999726596675416,
                            "predictability": 70,
                        },
                    ],
                    "time": "2022-05-03T09:22:52.446273+01:00",
                    "sun_rise": "2022-05-03T05:28:53.178071+01:00",
                    "sun_set": "2022-05-03T20:26:58.312348+01:00",
                    "timezone_name": "LMT",
                    "parent": {
                        "title": "England",
                        "location_type": "Region / State / Province",
                        "woeid": 24554868,
                        "latt_long": "52.883560,-1.974060",
                    },
                    "sources": [
                        {
                            "title": "BBC",
                            "slug": "bbc",
                            "url": "http://www.bbc.co.uk/weather/",
                            "crawl_rate": 360,
                        },
                        {
                            "title": "Forecast.io",
                            "slug": "forecast-io",
                            "url": "http://forecast.io/",
                            "crawl_rate": 480,
                        },
                        {
                            "title": "HAMweather",
                            "slug": "hamweather",
                            "url": "http://www.hamweather.com/",
                            "crawl_rate": 360,
                        },
                        {
                            "title": "Met Office",
                            "slug": "met-office",
                            "url": "http://www.metoffice.gov.uk/",
                            "crawl_rate": 180,
                        },
                        {
                            "title": "OpenWeatherMap",
                            "slug": "openweathermap",
                            "url": "http://openweathermap.org/",
                            "crawl_rate": 360,
                        },
                        {
                            "title": "Weather Underground",
                            "slug": "wunderground",
                            "url": "https://www.wunderground.com/?apiref=fc30dc3cd224e19b",
                            "crawl_rate": 720,
                        },
                        {
                            "title": "World Weather Online",
                            "slug": "world-weather-online",
                            "url": "http://www.worldweatheronline.com/",
                            "crawl_rate": 360,
                        },
                    ],
                    "title": "London",
                    "location_type": "City",
                    "woeid": 44418,
                    "latt_long": "51.506321,-0.12714",
                    "timezone": "Europe/London",
                }
            ,
            200,
        )


class TestSdk(TestCase):
    def setUp(self):
        self.mw = MetaWeather()

    @mock.patch("app.sdk.requests.get", side_effect=mocked_requests_get)
    def test_get_raises_exception(self, mock_get):
        with self.assertRaises(ResultNotFoundError):
            self.mw._MetaWeather__get("https://www.metaweather.com/api/location/15015370/")

    @mock.patch("app.sdk.requests.get", side_effect=mocked_requests_get)
    def test_get_raises_ok(self, mock_get):
        result = self.mw._MetaWeather__get(
            "https://www.metaweather.com/api/location/99/"
        )
        self.assertIs(type(result), dict)


def mock_get_info(*args, **kwargs):
    return "This is #####"


class TestTeam(TestCase):

    @mock.patch("app.sdk.Human.get_info", side_effect=mock_get_info)
    def test_something(self, mock_get):
        m1 = Human(name="Claudine", age=24)
        t1 = Team()
        t1.add_member(m1)
        print(t1.members[0].get_info())
        exit(1)
