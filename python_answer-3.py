
        #Python Answer ------ 3

import pandas as pd
import requests

def download_data(url):
    response = requests.get(url)  
    return response.json() 

def process_data(data):
    # Extract the relevant attributes from the data
    processed_data = []
    for pokemon in data['pokemon']:
        processed_data.append({
            'id': pokemon['id'],
            'num': pokemon['num'],
            'name': pokemon['name'],
            'img': pokemon['img'],
            'type': ', '.join(pokemon['type']),
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'candy': pokemon.get('candy', ''),
            'candy_count': pokemon.get('candy_count', ''),
            'egg': pokemon.get('egg', ''),
            'spawn_chance': pokemon.get('spawn_chance', ''),
            'avg_spawns': pokemon.get('avg_spawns', ''),
            'spawn_time': pokemon.get('spawn_time', ''),
            'multipliers': ', '.join(str(multiplier) for multiplier in pokemon.get('multipliers', [])),
            'weakness': ', '.join(pokemon.get('weaknesses', [])),
            'next_evolution': ', '.join(evolution['name'] for evolution in pokemon.get('next_evolution', [])),
            'prev_evolution': ', '.join(evolution['name'] for evolution in pokemon.get('prev_evolution', []))
        })

    # Create a DataFrame from the processed data
    df = pd.DataFrame(processed_data)

    return df

def convert_to_excel(df, output_file):
    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)

if __name__ == '__main__':
    # Provide the link to download the data
    data_url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'

    # Provide the desired output file path
    output_file_path = 'output.xlsx'

    # Download the data
    downloaded_data = download_data(data_url)

    # Process the data
    processed_data = process_data(downloaded_data)

    # Convert and save the processed data to Excel
    convert_to_excel(processed_data, output_file_path)

