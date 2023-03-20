import location
import route
import pprint


# Coordenadas para qualquer endereço digitado
adress1 = str(input('Digite o endereço de partida: '))
adress2 = str(input('Digite o destino: '))
formated_adress1 = location.format_adress(adress1)
formated_adress2 = location.format_adress(adress2)
data1 = location.get_data_location(formated_adress1)
data2 = location.get_data_location(formated_adress2)
point1 = location.get_coordinates(data1)
point2 = location.get_coordinates(data2)
points = location.join_coordinates(point1, point2)

# Calculo de rota para endereços digitados
my_route = route.get_route(points)
pprint.pprint(route.get_directions(my_route))
