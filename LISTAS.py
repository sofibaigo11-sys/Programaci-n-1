# Ejercicio 1: Creo una lista con los múltiplos de 4 del 1 al 100
multiplos = list(range(4, 101, 4))

# Muestro la lista por pantalla
print(multiplos)

# Ejercicio 2: Creo una lista con cinco elementos
Elementos = ["perro", "1.2", "Hola", "UTN", "luna"]

# Muestro el penúltimo elemento de la lista
print(Elementos[-2])

# Ejercicio 3: Creo una lista vacía
lista_vacia = []

# Agrego tres palabras a la lista
lista_vacia.append("Hola")
lista_vacia.append("Programacion")
lista_vacia.append("Mendoza")

# Muestro la lista por pantalla
print(lista_vacia)

# Ejercicio 4: Creo la lista de animales
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazo el segundo animal
animales[1] = "loro"

# Reemplazo el último animal
animales[-1] = "oso"

# Muestro la lista por pantalla
print(animales)

#Ejercicio 5: Analizar el programa y explicar que hace.
#El programa crea una lista de números. Con `remove(max())` elimina el número más grande de la lista, dejando los demás números.

#Ejercicio 6: Creo una lista con números del 10 al 30, saltando de 5 en 5
numeros = list(range(10, 31, 5))

# Muestro los dos primeros números
print(numeros[:2])

#Ejercicio 7: Creo la lista de autos
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazo el segundo auto
autos[1] = "fiat"

# Reemplazo el tercer auto
autos[2] = "renault"

# Muestro la lista
print(autos)

#Ejercicio 8: Creo una lista vacía
dobles = []

# Agrego el doble de 5
dobles.append(5 * 2)

# Agrego el doble de 10
dobles.append(10 * 2)

# Agrego el doble de 15
dobles.append(15 * 2)

# Muestro la lista
print(dobles)

#Ejercicio 9: 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# agregar jugo al tercer cliente
compras[2].append("jugo")

# cambiar fideos por tallarines
compras[1][1] = "tallarines"

# eliminar pan del primer cliente
compras[0].remove("pan")

print(compras)

#Ejercicio 10: Elaborar una lista anidada
Lista_anidada = [15,True,[25.5,57.9,30.6],False]
print(Lista_anidada)

