import location
import flow
import pprint


# Coordenadas para qualquer endereço digitado
adress = str(input('Digite o endereço: '))
formated_adress = location.format_adress(adress)
data = location.get_data_location(formated_adress)
point = location.get_coordinates(data)

# Condições de tráfego para o endereço digitado
traffic_data = flow.get_traffic_flow(point)
result = flow.parse_data(traffic_data)
pprint.pprint(result)
