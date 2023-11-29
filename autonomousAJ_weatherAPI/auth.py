# autonomousAJ_weatherAPI/autonomousAJ_weatherAPI/auth.py
import os
from dotenv import load_dotenv

load_dotenv()

class Get_Weather_Client:
    def __init__(self):
        self.api_key = os.getenv("WEATHER_API_KEY")

    def get_weather_client(self):
        api_key = self.api_key

        return clientapi_key

weather_client = Get_Weather_Client()