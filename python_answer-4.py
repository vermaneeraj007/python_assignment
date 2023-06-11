


            #Python Answer------4

import pandas as pd
import requests

def download_data(url):
    response = requests.get(url)  
    return response.json()  

def process_data(data):
    processed_data = []
    for meteorite in data:
        processed_data.append({
            'name': meteorite.get('name', ''),
            'id': meteorite.get('id', ''),
            'nametype': meteorite.get('nametype', ''),
            'recclass': meteorite.get('recclass', ''),
            'mass': meteorite.get('mass (g)', ''),
            'year': meteorite.get('year', ''),
            'reclat': meteorite.get('reclat', ''),
            'reclong': meteorite.get('reclong', ''),
            'coordinates': [meteorite.get('reclong', ''), meteorite.get('reclat', '')]
        })

    # Create a DataFrame from the processed data
    df = pd.DataFrame(processed_data)

    return df

def convert_to_csv(df, output_file):
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    data_url = 'https://data.nasa.gov/resource/y77d-th95.json'

    # Provide the desired output file path
    output_file_path = 'output.csv'

    # Download the data
    downloaded_data = download_data(data_url)

    # Process the data
    processed_data = process_data(downloaded_data)

    # Convert and save the processed data to a CSV file
    convert_to_csv(processed_data, output_file_path)
