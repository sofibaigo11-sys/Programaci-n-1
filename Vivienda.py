from Habitacion import Habitacion

class Vivienda:
    def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self):
        superficie = 0

        for habitacion in self.habitaciones:
            superficie = superficie + habitacion.metrosCuadrados
# Si la superficie cubierta supera la superficie del terreno, tenemos que lanzar una excepción.
        if superficie > self.superficieTerreno:
            raise Exception("La superficie cubierta no puede ser mayor a la superficie del terreno")

        return superficie
            