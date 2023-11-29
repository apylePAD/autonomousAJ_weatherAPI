# autonomousAJ_weatherAPI/autonomousAJ_weatherAPI/api/base.py
from autonomousAJ_weatherAPI.auth import weather_client
import requests

class Weather_API_Base:
    def get_weather_client(self):
        return weather_client.get_weather_client()

    def get_api_url(self):
        return weather_client.get_api_url()

    def handle_api_calls(self, api_function, *args, **kwargs):
        try:
            response = api_function(*args, **kwargs)
            response.raise_for_status()
            return response

        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"OOps: Something Else {err}")
        except Exception as e:
            print(f"Error: {e}")

        return None
