from dotenv import dotenv_values
import requests
from requests.structures import CaseInsensitiveDict
import pprint

api_key = dotenv_values(".env")['API_KEY_2']

def format_adress(adress: str):
    formated_adress = adress.replace(' ', '%20').lower()
    return formated_adress

def get_data_location(adress: str):
    url = f'https://api.geoapify.com/v1/geocode/search?'\
        f'text={adress}&'\
        f'apiKey={api_key}'

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    response = requests.get(url, headers=headers)
    return response.json()

def get_coordinates(data):
    data = data['features']
    coord = data[0]['geometry']['coordinates']
    coord = [str(x) for x in coord]
    coord.append(coord.pop(0))
    return ','.join(coord)

if __name__ == '__main__':
    adress = format_adress('Avenida Floriano Peixoto Uberlândia 1525')
    data = get_data_location(adress)
    pprint.pprint(get_coordinates(data))

