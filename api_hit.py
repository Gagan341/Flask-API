import requests
BASE = "http://127.0.0.1:5000/"

response = requests.patch(BASE + "game/2", {})
print(response.json())
input()
response = requests.get(BASE + "game/1",{})
print(response.json())




