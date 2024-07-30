import requests
import json
import random
import time

url = 'http://localhost:5000/webhook'
headers = {'Content-Type': 'application/json'}

def generate_data():
    """
    Generates a dictionary with random values for each metric.
    """
    data = {
        "Number of visitors": random.randint(1000, 5000),
        "Page views per session": random.randint(1, 50),
        "Click-through rates": round(random.uniform(0.01, 0.5), 2),  # Percentage between 1% and 50%
        "Bounce rates": round(random.uniform(0.1, 0.9), 2),  # Percentage between 10% and 90%
        "Average session duration": round(random.uniform(30, 3600), 2)  # Seconds between 30 seconds and 1 hour
    }
    return data

def send_data(data):
    """
    Sends data to the specified URL.
    """
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(f"Status Code: {response.status_code}")
        print("Response JSON:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main(num_records):
    """
    Generates and sends data records.
    """
    for _ in range(num_records):
        data = generate_data()
        send_data(data)
        time.sleep(0.1)  # Throttle requests to avoid overwhelming the server

if __name__ == "__main__":
    num_records = 1000000  # Number of records to send
    main(num_records)

