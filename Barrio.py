from Vivienda import Vivienda

class Barrio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.viviendas = []

    def agregar_vivienda(self, vivienda):
        self.viviendas.append(vivienda)

    def getSuperficieTotalTerrenos(self):
        superficie = 0

        for vivienda in self.viviendas:
            superficie = superficie + vivienda.superficieTerreno

        return superficie

    def getSuperficieTerrenosPorManzana(self, manzana):
        superficie = 0

        for vivienda in self.viviendas:
            if vivienda.manzana == manzana:
                superficie = superficie + vivienda.superficieTerreno

        return superficie

    def getSuperficieCubiertaTotal(self):
        superficie = 0

        for vivienda in self.viviendas:
            superficie = superficie + vivienda.getMetrosCuadradosCubiertos()

        return superficie