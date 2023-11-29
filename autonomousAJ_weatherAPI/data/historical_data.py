# autonomousAJ_weatherAPI/autonomousAJ_weatherAPI/data/historical_data.py
# Endpoint: historical
# URL: {'proper_name': 'Historical', 'url': nan}
import pandas as pd
from autonomousAJ_weatherAPI.api.historical import Historical
from autonomousAJ_weatherAPI.config import global_config

class Historical_Data:
    def __init__(self):
        self.historical = Historical()

    def get_and_process_data(self):
        data = self.historical.get_historical()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
