from Computadora import Computadora
from ComponenteCPU import ComponenteCPU

cantidadComputadoras = int(input("Ingrese la cantidad de computadoras: "))

computadoras = []

for i in range(cantidadComputadoras):
    marca = input("Ingrese la marca de la computadora: ")
    modelo = input("Ingrese el modelo de la computadora: ")
    computadora = Computadora(marca, modelo)
    computadoras.append(computadora)

    cantidadComponentes = int(input("Ingrese la cantidad de componentes: "))

    for j in range(cantidadComponentes):
        componente = input("Ingrese el nombre del componente: ")
        marcaComponente = input("Ingrese la marca del componente: ")
        cantidad = int(input("Ingrese la cantidad del componente: "))
        precio = float(input("Ingrese el precio del componente: "))
        componenteCPU = ComponenteCPU(componente, marcaComponente, cantidad, precio)
        computadora.agregar_componente(componenteCPU)
    
        costoTotal = 0

    for componente in computadora.componentes:
        costoTotal = costoTotal + (componente.precio * componente.cantidad)

    if costoTotal < 50000:
        precioVenta = costoTotal * 1.40
    elif costoTotal > 50000:
        precioVenta = costoTotal * 1.30
    else:
        precioVenta = costoTotal * 1.30

    print("Marca:", computadora.marca)
    print("Modelo:", computadora.modelo)
    print("Costo total:", costoTotal)
    print("Precio de venta:", precioVenta)

else:
    precioVenta = costoTotal * 1.30
    