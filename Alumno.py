class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        suma = 0

        for nota in self.notas:
            suma = suma + nota.notaExamen

        promedio = suma / len(self.notas)
        return promedio