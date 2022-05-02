from app.sdk import MetaWeather
from pprint import pprint


pprint(MetaWeather().get_next_six_days_weather(15015370))