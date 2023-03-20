from dotenv import dotenv_values
import requests
import pprint

api_key = dotenv_values(".env")['ROUTE_KEY']

def get_route_id(adress1, adress2):
    url = f'https://api.tomtom.com/routemonitoring/2/routes?key={api_key}'
    data = {
    "name": "Test Route",
    "pathPoints": [
        {
        "latitude": adress1[0],
        "longitude": adress1[1]
        },
        {
        "latitude": adress2[0],
        "longitude": adress2[1]
        }
    ]
    }
    r = requests.get(url, data)
    return r.status_code

if __name__ == '__main__':
    adress1 = [-18.8879438, -48.253286]
    adress2 = [-18.916133, -48.289098]
    print(api_key)
    print(get_route_id(adress1, adress2))