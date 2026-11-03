from Plato import Plato
from Ingrediente import Ingrediente

cantidadPlatos = int(input("Ingrese la cantidad de platos: "))

platos = []

for i in range(cantidadPlatos):
    nombreCompleto = input("Ingrese el nombre del plato: ")
    precio = float(input("Ingrese el precio del plato: "))
    esBebida = input("¿Es una bebida? (si/no): ").lower() == "si"

    plato = Plato(nombreCompleto, precio, esBebida)

    if not esBebida:
    # Cargar ingredientes
        cantidadIngredientes = int(input("Ingrese la cantidad de ingredientes: "))

        while cantidadIngredientes < 1:
            cantidadIngredientes = int(input("Debe ingresar al menos un ingrediente: "))

        for j in range(cantidadIngredientes): 
            nombre = input("Ingrese el nombre del ingrediente: ")
            cantidad = float(input("Ingrese la cantidad del ingrediente: "))   
            unidadMedida = input("Ingrese la unidad de medida: ")

            ingrediente = Ingrediente(nombre, cantidad, unidadMedida)
            plato.agregar_ingrediente(ingrediente)

    
    platos.append(plato)     

for plato in platos:
    print("Plato:", plato.nombreCompleto)
    print("Precio:", plato.precio)
    print("Es bebida:", plato.esBebida)

    for ingrediente in plato.ingredientes:
        print("Ingrediente:", ingrediente.nombre)
        print("Cantidad:", ingrediente.cantidad)
        print("Unidad de medida:", ingrediente.unidadMedida)