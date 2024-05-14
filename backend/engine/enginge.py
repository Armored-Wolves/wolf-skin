import requests
import json
from backend.engine import engineConfig


def check_user(user_name):
    request = requests.get(f"https://api.worldoftanks.eu/wot/account/list/?application_id={engineConfig.config.app_id}&search={user_name}")
    if request.status_code == 200:
        data_json = json.loads(request.text)
        return data_json['data']
    else:
        return ('ERROR')

def get_personal_statistic(application_id, user_id):
    data = requests.get(f"https://api.worldoftanks.asia/wot/account/info/?application_id={application_id}&account_id={user_id}")
    return json.loads(data.text)

def parse_user_data(user_info: dict):
    user_id = str(user_info[0]["account_id"])
    user_name = user_info[0]["nickname"]
    return  user_name, user_id

def return_to_django(user_name, user_id):
    response = requests.post("http://127.0.0.1:8000/api/user/", json={"username": user_name, "password": user_id})

if __name__ == "__main__":
    input_name = input("\nEnter the name of your favourite tanker <3")
    test_user = check_user(input_name)
    name, id = parse_user_data(test_user)
    print(name, id)
    return_to_django(name, id)
