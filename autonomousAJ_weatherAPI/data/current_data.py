# autonomousAJ_weatherAPI/autonomousAJ_weatherAPI/data/current_data.py
# Endpoint: current
# URL: {'proper_name': 'Current', 'url': nan}
import pandas as pd
from autonomousAJ_weatherAPI.api.current import Current
from autonomousAJ_weatherAPI.config import global_config

class Current_Data:
    def __init__(self):
        self.current = Current()

    def get_and_process_data(self):
        data = self.current.get_current()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
