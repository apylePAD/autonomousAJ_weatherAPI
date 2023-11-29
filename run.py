# autonomousAJ_weatherAPI/run.py
import inquirer
from autonomousAJ_weatherAPI.data.current_data import Current_Data
from autonomousAJ_weatherAPI.data.forecast_data import Forecast_Data
from autonomousAJ_weatherAPI.data.historical_data import Historical_Data
from autonomousAJ_weatherAPI.data.marine_data import Marine_Data

def main_menu():
    questions = [
        inquirer.List("choice",
                      message="What type of data would you like to interact with?",
                      choices=["Current", "Forecast", "Historical", "Marine", "Exit"]),
    ]
    return inquirer.prompt(questions)["choice"]

def get_current_input():
    current_processor = Current_Data()
    current_processor.get_and_process_data()

def get_forecast_input():
    forecast_processor = Forecast_Data()
    forecast_processor.get_and_process_data()

def get_historical_input():
    historical_processor = Historical_Data()
    historical_processor.get_and_process_data()

def get_marine_input():
    marine_processor = Marine_Data()
    marine_processor.get_and_process_data()

def run():
    while True:
        choice = main_menu()
        if choice == "Current":
            get_current_input()
        elif choice == "Forecast":
            get_forecast_input()
        elif choice == "Historical":
            get_historical_input()
        elif choice == "Marine":
            get_marine_input()
        elif choice == "Exit":
            break

if __name__ == "__main__":
    run()