from ComponenteCPU import ComponenteCPU

class Computadora:
        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo
            self.componentes = []

        def agregar_componente(self, componente):
            self.componentes.append(componente)