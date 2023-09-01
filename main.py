import config
import requests
from datetime import datetime

############ NUTRITIONIX SET-UP ############
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": config.APP_ID,
    "x-app-key": config.API_KEY
}

nutritionix_params = {
    "query": input("What exercise did you do? "),
    "gender": config.GENDER,
    "weight_kg": config.WEIGHT_KG,
    "height_cm": config.HEIGHT_CM,
    "age": config.AGE
}

response = requests.post(nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_headers)
exercise_data = response.json()["exercises"][0]
print(exercise_data)

############ SHEETY SET-UP ############
sheety_endpoint = f"https://api.sheety.co/{config.SHEETY_END}"

today = datetime.now().strftime("%m/%d/%Y")
time = datetime.now().strftime("%X")

sheety_headers = {
    "Authorization": config.SHEETY_AUTH
}
sheety_data = {
        "sheet1": {
            "date": today,
            "time": time,
            "exercise": exercise_data["name"].title(),
            "duration(minutes)": exercise_data["duration_min"],
            "calories": exercise_data["nf_calories"]
        }
    }

response2 = requests.post("https://api.sheety.co/4f2493c9b66f38854fb55d19168fb579/workoutTracking/sheet1", json=sheety_data, headers=sheety_headers)

