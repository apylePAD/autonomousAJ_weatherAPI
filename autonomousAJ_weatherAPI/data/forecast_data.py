# autonomousAJ_weatherAPI/autonomousAJ_weatherAPI/data/forecast_data.py
# Endpoint: forecast
# URL: {'proper_name': 'Forecast', 'url': nan}
import pandas as pd
from autonomousAJ_weatherAPI.api.forecast import Forecast
from autonomousAJ_weatherAPI.config import global_config

class Forecast_Data:
    def __init__(self):
        self.forecast = Forecast()

    def get_and_process_data(self):
        data = self.forecast.get_forecast()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
