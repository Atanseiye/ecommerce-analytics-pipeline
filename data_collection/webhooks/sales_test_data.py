import requests
import json
import random
import time

# Simulate a live data source for sales metrics
def fetch_sales_data():
    """
    Simulates fetching sales data from a live source.
    """
    data = {
        "Total sales": round(random.uniform(10000, 500000), 2),  # Revenue between $10,000 and $500,000
        "Average order value": round(random.uniform(50, 500), 2),  # Average order value between $50 and $500
        "Conversion rates": round(random.uniform(0.01, 0.2), 2),  # Conversion rates between 1% and 20%
        "Top-selling products": [f"Product_{i}" for i in range(random.randint(1, 10))],  # Random number of top-selling products
        "Sales by category": {f"Category_{i}": round(random.uniform(1000, 20000), 2) for i in range(random.randint(1, 5))}  # Random number of categories
    }
    return data

# URL of the live data endpoint
url = 'http://localhost:5000/webhook'
headers = {'Content-Type': 'application/json'}

def send_batch(batch):
    """
    Sends a batch of data to the specified URL.
    """
    try:
        response = requests.post(url, headers=headers, data=json.dumps(batch))
        print(f"Status Code: {response.status_code}")
        print("Response JSON:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main(batch_size, num_batches):
    """
    Continuously fetches, batches, and sends sales data.
    """
    for _ in range(num_batches):
        batch = []
        for _ in range(batch_size):
            data = fetch_sales_data()
            batch.append(data)
            time.sleep(0.1)  # Simulate data generation interval
        
        send_batch(batch)
        print(f"Sent batch of size {batch_size}")
        time.sleep(1)  # Adjust this based on server capacity and frequency of data generation

if __name__ == "__main__":
    batch_size = 100  # Number of records per batch
    num_batches = 10000  # Number of batches to send
    main(batch_size, num_batches)
