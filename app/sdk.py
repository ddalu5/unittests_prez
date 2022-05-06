import requests

from .exceptions import ResultNotFoundError
from .exceptions import MetaWeatherAPIUnreachableError

BASE_URL = "https://www.metaweather.com/"


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return {"name": self.name, "age": self.age}


class Team:

    def __init__(self):
        self.members = []

    def add_member(self, member: Human):
        self.members.append(member)


class MetaWeather:
    def __get(self, url: str, params: dict = {}):
        """
        Generic function to use HTTP GET method

        :param url: http URL
        :param params: optional parameter to send
        :return: a list of locations
        """
        try:
            response = requests.get(url=url, params=params)
        except Exception as e:
            raise MetaWeatherAPIUnreachableError(str(e))
        if response.status_code == 404:
            raise ResultNotFoundError(url)
        return response.json()

    def __search(self, criteria: dict):
        """
        Search locations using a criteria

        :param criteria:
        :return:
        """
        return self.__get(url=f"{BASE_URL}api/location/search/?", params=criteria)

    def search_odd_cities_names(self, name_criteria: str):
        """
        Search cities by names or part of the names

        :param name_criteria: part of the name we are searching for
        :return: a list of cities that have an odd names' length
        """
        odd_cities = []
        result = self.__search({"query": name_criteria})
        for element in result:
            if element["location_type"] == "City" and len(element["title"]) % 2 != 0:
                odd_cities.append(element)
        return odd_cities

    def get_next_six_days_weather(self, woid: int):
        """
        Get next six days weather for a location, current day included

        :param woid: location id
        :return: list of the next six days weather
        """
        six_days_weather = {}
        result = self.__get(url=f"{BASE_URL}api/location/{woid}/")[
            "consolidated_weather"
        ]
        for element in result:
            six_days_weather[element["applicable_date"]] = element
        return six_days_weather
