import requests
import json

url = 'http://localhost:5000/webhook'
headers = {'Content-Type': 'application/json'}
data = {
    "Name": "Kolade",
    "Level": "500",
    "Dept": "Computer Science"
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
