from dotenv import dotenv_values
import requests
import pprint


api_key = dotenv_values(".env")['API_KEY']


def get_traffic_flow(point):
    base_url = 'api.tomtom.com'
    version_number = 4
    style = 'relative'
    zoom = 10
    format_ = 'json'

    url = f'https://{base_url}/traffic/services/{version_number}/'\
        f'flowSegmentData/{style}/{zoom}/{format_}?key={api_key}&point={point}'
    response = requests.get(url)
    return response.json()

def parse_data(response):
    response = response['flowSegmentData']
    parsed_dict = {
        'Velocidade atual': f"{response['currentSpeed']} km/h",
        'Velocidade ideal': f"{response['freeFlowSpeed']} km/h",
        'Tempo de viajem atual': f"{response['currentTravelTime']} segundos",
        'Tempo de viajem ideal': f"{response['freeFlowTravelTime']} segundos",
        'Confiança de 0 a 1': response['confidence'],
        'Situação da via': ('Fechada' if response['roadClosure'] else 'Aberta')
    }
    return parsed_dict

if __name__ == '__main__':
    point = '-18.9110465,-48.2707498'
    traffic = get_traffic_flow(point)
    pprint.pprint(parse_data(traffic))

