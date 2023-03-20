from dotenv import dotenv_values
import requests
from requests.structures import CaseInsensitiveDict

api_key = dotenv_values(".env")['API_KEY_2']

def format_adress(adress: str) -> str:
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

def get_coordinates(data: dict) -> str:
    data = data['features']
    coord = data[0]['geometry']['coordinates']
    coord = [str(x) for x in coord]
    coord.append(coord.pop(0))
    return ','.join(coord)

def get_coordinates_route(data: dict) -> list:
    data = data['features']
    coord = data[0]['geometry']['coordinates']
    coord.append(coord.pop(0))
    return coord

def join_coordinates(adress1: str, adress2: str) -> str:
    points = adress1 + ':' + adress2
    return points 


if __name__ == '__main__':

    adress = format_adress('Floriano Peixoto 1525 Uberlândia ')
    adress2 = format_adress('Rafael Rinaldi 523 Uberlândia')
    data = get_data_location(adress)
    data2 = get_data_location(adress2)
    ex1 = get_coordinates(data)
    ex2 = get_coordinates(data2)
    print(join_coordinates(ex1, ex2))

