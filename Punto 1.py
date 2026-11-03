# Ejercicio 1: Clase Celda y Matriz

# Creamos la clase Celda
class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor


# Creamos la clase Matriz
class Matriz:
    def __init__(self):
        # Lista donde guardamos las celdas
        self.celdasMatriz = []

    # Método para agregar una celda
    def agregar_celda(self, fila, columna, valor):

        # Verificamos si la posición ya existe
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                print("Esta celda ya fue cargada.")
                return

        # Creamos el objeto Celda
        nueva_celda = Celda(fila, columna, valor)

        # Agregamos el objeto a la lista
        self.celdasMatriz.append(nueva_celda)

    # Método para mostrar las celdas
    def mostrar_celdas(self):
        for celda in self.celdasMatriz:
            print("Fila:", celda.fila)
            print("Columna:", celda.columna)
            print("Valor:", celda.valor)
            print("-------------------")

    # Método para buscar una celda
    def buscar_celda(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor

        return "La fila y columna indicada no ha sido asignada en ninguna celda"


# Programa principal

# Creamos un objeto Matriz
matriz = Matriz()

# Cargamos las celdas
while True:
    valor = input("Ingresá el valor de la celda (FIN para terminar): ")

    if valor.upper() == "FIN":
        break

    fila = int(input("Ingresá la fila: "))
    columna = int(input("Ingresá la columna: "))

    matriz.agregar_celda(fila, columna, valor)


# Mostramos las celdas cargadas
print("\nCeldas cargadas:")
matriz.mostrar_celdas()


# Buscamos una celda
fila_buscar = int(input("Ingresá la fila que querés buscar: "))
columna_buscar = int(input("Ingresá la columna que querés buscar: "))

resultado = matriz.buscar_celda(fila_buscar, columna_buscar)

print("Resultado:", resultado)