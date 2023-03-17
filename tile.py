from dotenv import dotenv_values
import requests
import map_pb2 as MapList

config = dotenv_values(".env")  
api_key = config['API_KEY']
base_url = 'api.tomtom.com'
version_number = 2
layer = 'hybrid'
zoom = 5
x = 4
y = 8
format_ = 'pbf'


def get_tile(key, url, version, layer, zoom, x, y, format_):
    response = requests.get( f'https://{url}/map/{version}/tile/{layer}'\
                            f'/{zoom}/{x}/{y}.{format_}?key={key}')
    bin_response = response.content
    # Primeiro cria uma 'base' .proto roda no terminal a função pro protoc
    # criar um arquivo.py
    tile = MapList.Tile()
    tile.ParseFromString(bin_response)
    return tile


if __name__ == '__main__':
    print(get_tile( api_key,
                    base_url,
                    version_number, 
                    layer, 
                    zoom,
                    x, 
                    y, 
                    format_ ))