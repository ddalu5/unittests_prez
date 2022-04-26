import requests

from .exceptions import ResultNotFoundError
from .exceptions import MetaWeatherAPIUnreachableError

BASE_URL = "https://www.metaweather.com/"


class MetaWeather:
    def __get(self, url: str, params: dict = {}):
        try:
            response = requests.get(url=url, params=params)
            if response.status_code == 404:
                raise
        except Exception as e:
            raise MetaWeatherAPIUnreachableError(str(e))

    def __search(self, criteria: dict):
        return self.__get(url=f"{BASE_URL}api/location/search/?", params=criteria)

    def search_by_name(self, name: str):
        return self.__search({"query": name})

    def search_by_location(self, latt: float, long: float):
        return self.__search({"lattlong": f"{latt},{long}"})

    def get_weather(self, woid: int):
        return self.__get(url=f"{BASE_URL}api/location/{woid}/")
