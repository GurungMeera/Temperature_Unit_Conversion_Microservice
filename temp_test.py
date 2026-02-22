import requests

BASE_URL = "http://127.0.0.1:8000"

response = requests.get(f"{BASE_URL}/ctof/", params={"temp": 20})
print(response.json())

response = requests.get(f"{BASE_URL}/ftoc/", params={"temp": 86})
print(response.json())

response = requests.get(
    f"{BASE_URL}/thermometer/",
    params={"temp": 30, "unit": "F"}
)
print(response.json())
