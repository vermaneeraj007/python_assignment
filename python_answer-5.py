


            #Python Answer -------- 5




import requests
import json
import re

def download_data(url):
    response = requests.get(url)  
    return response.json()  

def process_data(data):
    show_data = {
        'id': data.get('id', ''),
        'url': data.get('url', ''),
        'name': data.get('name', ''),
        'season': data['season'],
        'number': data['number'],
        'type': data.get('type', ''),
        'airdate': data.get('airdate', ''),
        'airtime': data.get('airtime', ''),
        'runtime': data.get('runtime', ''),
        'average_rating': data.get('averageRating', ''),
        'summary': re.sub('<[^<]+?>', '', data.get('summary', '')),
        'medium_image': data['image']['medium'],
        'original_image': data['image']['original']
    }

    return show_data

if __name__ == '__main__':
    api_link = 'http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes'

    downloaded_data = download_data(api_link)

    processed_data = process_data(downloaded_data['_embedded']['episodes'][0])

    print(json.dumps(processed_data, indent=4))
