from Barrio import Barrio
from Vivienda import Vivienda
from Habitacion import Habitacion

nombre = input("Ingrese el nombre del barrio: ")
barrio = Barrio(nombre)

cantidadViviendas = int(input("Ingrese la cantidad de viviendas: "))

for i in range(cantidadViviendas):

    calle = input("Ingrese la calle: ")
    numero = int(input("Ingrese el número de la calle: "))
    manzana = int(input("Ingrese la manzana: "))
    nroCasa = int(input("Ingrese el número de la casa: "))
    superficieTerreno = float(input("Ingrese la superficie del terreno en m2: "))
    vivienda = Vivienda(calle, numero, manzana, nroCasa, superficieTerreno)
    barrio.agregar_vivienda(vivienda)

    cantidadHabitaciones = int(input("Ingrese la cantidad de habitaciones: "))

    for j in range(cantidadHabitaciones):
        nombreHabitacion = input("Ingrese el nombre de la habitación: ")
        metrosCuadrados = float(input("Ingrese los metros cuadrados de la habitación: "))
        
        habitacion = Habitacion(nombreHabitacion, metrosCuadrados)
        vivienda.agregar_habitacion(habitacion)

print("Barrio:", barrio.nombre)
print("Superficie total de terrenos:", barrio.getSuperficieTotalTerrenos())
print("Superficie cubierta total:", barrio.getSuperficieCubiertaTotal())

manzanaConsulta = int(input("Ingrese la manzana que desea consultar: "))
print("Superficie de terrenos de la manzana:", barrio.getSuperficieTerrenosPorManzana(manzanaConsulta))
