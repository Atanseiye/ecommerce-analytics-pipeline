import requests
import json


def fetch_load_data(api_url, output_file):
    """
    - To fetch data from a API and save if in the given directory
    
    Parameters:
    api_url(str): the api usr to get the data from
    output_file(str): the filepath to save the loaded file

    """
    try:
        response = requests.get(api_url)
        response.raise_for_status() # to raise signal if there is any error
        data = response.json()

        with open(output_file, 'w') as file:
            json.dumps(data, file, indent=4)

        return {'respose': f"Data successfully fetched and saved to {output_file}"}

    except Exception as error:
        return {'respose': "Error fetching data"}


   