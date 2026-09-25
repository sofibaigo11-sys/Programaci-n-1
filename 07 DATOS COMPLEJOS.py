# Ejercicio 1: Creamos el diccionario con los precios iniciales
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agregamos nuevas frutas con sus respectivos precios
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Ejercicio 2: Actualizamos los precios de algunas frutas
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# Ejercicio 3: Creamos una lista que contiene solamente las claves del diccionario
lista_frutas = list(precios_frutas.keys())

# Mostramos la lista de frutas
print(lista_frutas)

# Ejercicio 4: Creamos un diccionario vacío para guardar los contactos
telefonos = {}

# Repetimos 5 veces para cargar los contactos
for i in range(5):
    nombre = input("Ingrese el nombre: ")
    numero = input("Ingrese el número: ")
    telefonos[nombre] = numero

# Pedimos el nombre que queremos buscar
nombre_buscar = input("Ingrese el nombre que desea consultar: ")

# Verificamos si el nombre existe en el diccionario
if nombre_buscar in telefonos:
    print("El número es:", telefonos[nombre_buscar])
else:
    print("El contacto no existe")

# Ejercicio 5: Pedimos una frase al usuario
frase = input("Ingrese una frase: ")

# Separamos la frase en palabras
palabras = frase.split()

# Creamos un set para tener solamente las palabras únicas
palabras_unicas = set(palabras)

# Creamos un diccionario vacío para contar las palabras
conteo = {}

# Recorremos todas las palabras de la frase
for palabra in palabras:

    # Verificamos si la palabra ya está en el diccionario
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

# Mostramos las palabras únicas
print(palabras_unicas)

# Mostramos cuántas veces aparece cada palabra
print(conteo)


# Ejercicio 6: Creamos un diccionario para guardar los alumnos y sus notas
alumnos = {}

# Repetimos 3 veces para ingresar los datos de los alumnos
for i in range(3):

    # Pedimos el nombre del alumno
    nombre = input("Ingrese el nombre del alumno: ")

    # Pedimos las tres notas
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))

    # Guardamos las notas en una tupla
    alumnos[nombre] = (nota1, nota2, nota3)

# Recorremos los alumnos
for nombre in alumnos:

    # Calculamos el promedio de las tres notas
    promedio = sum(alumnos[nombre]) / 3

    # Mostramos el nombre y el promedio
    print(nombre, promedio)


# Ejercicio 7: Creamos un set con los alumnos que aprobaron el parcial 1
parcial1 = {1, 2, 3, 4, 5}

# Creamos un set con los alumnos que aprobaron el parcial 2
parcial2 = {3, 4, 5, 6, 7}

# Mostramos los alumnos que aprobaron ambos parciales
print("Aprobaron ambos:", parcial1 & parcial2)

# Mostramos los alumnos que aprobaron solamente uno
print("Aprobaron solo uno:", parcial1 ^ parcial2)

# Mostramos todos los alumnos que aprobaron al menos un parcial
print("Aprobaron al menos uno:", parcial1 | parcial2)


# Ejercicio 8: Creamos un diccionario vacío para guardar los productos y su stock
stock = {}

# Repetimos para ingresar productos
for i in range(3):

    # Pedimos el nombre del producto
    producto = input("Ingrese el producto: ")

    # Pedimos la cantidad disponible
    cantidad = int(input("Ingrese el stock: "))

    # Guardamos el producto y su cantidad
    stock[producto] = cantidad

# Pedimos el producto que queremos consultar
producto = input("Ingrese el producto a consultar: ")

# Verificamos si el producto existe
if producto in stock:

    # Mostramos el stock actual
    print("Stock:", stock[producto])

    # Preguntamos cuántas unidades quiere agregar
    agregar = int(input("¿Cuántas unidades desea agregar?: "))

    # Sumamos las nuevas unidades al stock
    stock[producto] += agregar

else:

    # Si no existe, pedimos la cantidad del nuevo producto
    cantidad = int(input("El producto no existe. Ingrese la cantidad: "))

    # Agregamos el nuevo producto al diccionario
    stock[producto] = cantidad

# Mostramos el diccionario actualizado
print(stock)


# Ejercicio 9: Creamos un diccionario vacío para guardar la agenda
agenda = {}

# Repetimos para cargar eventos
for i in range(3):

    # Pedimos el día
    dia = input("Ingrese el día: ")

    # Pedimos la hora
    hora = input("Ingrese la hora: ")

    # Pedimos el evento
    evento = input("Ingrese el evento: ")

    # Guardamos el evento usando una tupla como clave
    agenda[(dia, hora)] = evento

# Pedimos el día que queremos consultar
dia = input("Ingrese el día a consultar: ")

# Pedimos la hora que queremos consultar
hora = input("Ingrese la hora a consultar: ")

# Verificamos si existe una actividad en ese día y hora
if (dia, hora) in agenda:

    # Mostramos la actividad
    print("Actividad:", agenda[(dia, hora)])

else:

    # Informamos que no hay actividad
    print("No hay actividad")


# Ejercicio 10: Creamos un diccionario con países y sus capitales
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia"
}

# Creamos un diccionario vacío para invertir las claves y valores
capitales = {}

# Recorremos los países
for pais in paises:

    # Obtenemos la capital del país
    capital = paises[pais]

    # Guardamos la capital como clave y el país como valor
    capitales[capital] = pais

# Mostramos el nuevo diccionario
print(capitales)