# autonomousAJ_weatherAPI/autonomousAJ_weatherAPI/data/marine_data.py
# Endpoint: marine
# URL: {'proper_name': 'Marine', 'url': nan}
import pandas as pd
from autonomousAJ_weatherAPI.api.marine import Marine
from autonomousAJ_weatherAPI.config import global_config

class Marine_Data:
    def __init__(self):
        self.marine = Marine()

    def get_and_process_data(self):
        data = self.marine.get_marine()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
