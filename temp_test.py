import requests

# Local url
BASE_URL = "http://127.0.0.1:8000"

# Given 20c expecting 68f
response = requests.get(f"{BASE_URL}/ctof/", params={"temp": 20})
print(response.json())

# Given 86f expecting 30c
response = requests.get(f"{BASE_URL}/ftoc/", params={"temp": 86})
print(response.json())

# Given 30f expecting cold icon
response = requests.get(
    f"{BASE_URL}/thermometer/",
    params={"temp": 30, "unit": "F"}
)
print(response.json())
