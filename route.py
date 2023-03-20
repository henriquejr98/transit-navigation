from dotenv import dotenv_values
import requests
import pprint

api_key = dotenv_values(".env")['ROUTE_KEY']

def get_route(points):
    url = 'https://api.tomtom.com/routing/1/calculateRoute/'\
    f'{points}/json?'\
    'instructionsType=text&language=pt-BR'\
    '&vehicleHeading=90&sectionType=traffic'\
    '&report=effectiveSettings&routeType=eco'\
    '&traffic=true&avoid=unpavedRoads'\
    '&travelMode=car'\
    '&vehicleCommercial=false&vehicleEngineType=combustion'\
    f'&key={api_key}'
    response = requests.get(url)
    return response.json()

def get_directions(route):
    directions = route['routes'][0]['guidance']['instructions']
    total_length = route['routes'][0]['summary']['lengthInMeters']
    total_time = route['routes'][0]['summary']['travelTimeInSeconds']
    my_dict = {}
    last_street = ''
    for k, v  in enumerate(directions):
        if k != 0:
            current_time = total_time - v['travelTimeInSeconds']
            unit = (f'{current_time // 60} minutos e {current_time % 60} segundos' if current_time > 60 else f'{current_time} segundos')
            street = (f'Contiue na {last_street} por' if last_street != '' else 'Contiue na rua por')
            my_dict[k] = f"{street} {v['routeOffsetInMeters'] - last_length} metros e depois {v['message']} -> {unit} para o destino"
            if 'street' in v:
                last_street = v['street']
            last_length = v['routeOffsetInMeters']
        else:
            if 'street' in v:
                last_street = v['street']
            last_length = 0
            my_dict[k] =v['message']
    my_dict['Tempo total viagem'] = (f'{total_time // 60} minutos e {total_time % 60} segundos' if total_time > 60 else f'{total_time} segundos')
    my_dict['Distância total viagem'] = (f'{total_length // 1000} km e {total_length % 1000} metros' if total_length > 1000 else f'{total_length} metros')
    return my_dict


if __name__ == '__main__':
    points = '-18.9111831,-48.270603:-18.916133,-48.289098'
    route = get_route(points)
    # pprint.pprint(route)
    # pprint.pprint(route)
    pprint.pprint(get_directions(route))
