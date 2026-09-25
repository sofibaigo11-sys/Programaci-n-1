#Ejercicio 1: Creo una función llamada imprimir_hola_mundo
def imprimir_hola_mundo():
    # Muestro el mensaje "Hola Mundo!" en pantalla
    print("Hola Mundo!")

# Llamo a la función para que se ejecute
imprimir_hola_mundo()

#Ejercicio 2: Creo una función que recibe un nombre
def saludar_usuario(nombre):
    # Devuelvo un saludo personalizado
    return "Hola " + nombre + "!"

# Le pido el nombre al usuario
nombre = input("¿Cómo te llamás? ")

# Llamo a la función y muestro el resultado
print(saludar_usuario(nombre))

#Ejercicio 3: Creo una función que recibe nombre, apellido, edad y residencia
def informacion_personal(nombre, apellido, edad, residencia):
    # Muestro la información personal en pantalla
    print("Soy " + nombre + " " + apellido + ", tengo " + str(edad) + " años y vivo en " + residencia)


# Pido los datos al usuario
nombre = input("Indique su nombre: ")
apellido = input("Indique su apellido: ")
edad = int(input("Indique su edad: "))
residencia = input("Lugar en el que reside: ")

# Llamo a la función utilizando los datos ingresados
informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4:
# Creo una función que calcula el área del círculo
def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2
    return area


# Creo una función que calcula el perímetro del círculo
def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro


# Pido al usuario el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Muestro el área del círculo
print("El área del círculo es:", calcular_area_circulo(radio))

# Muestro el perímetro del círculo
print("El perímetro del círculo es:", calcular_perimetro_circulo(radio))

#Ejercicio 5: Creo una función que convierte segundos a horas
def segundos_a_horas(segundos):
    # Divido los segundos por la cantidad de segundos que tiene una hora
    horas = segundos / 3600
    return horas

# Pido al usuario una cantidad de segundos
segundos = int(input("Ingrese la cantidad de segundos: "))

# Muestro el resultado de la conversión
print("La cantidad de horas es:", segundos_a_horas(segundos))

#Ejercicio 6: Creo una función que muestra la tabla de multiplicar
def tabla_multiplicar(numero):
    # Recorro los números del 1 al 10
    for i in range(1, 11):
        # Muestro cada multiplicación
        print(numero, "x", i, "=", numero * i)

# Pido un número al usuario
numero = int(input("Ingrese un número: "))

# Llamo a la función
tabla_multiplicar(numero)

#Ejercicio 7: Creo una función que recibe dos números
def operaciones_basicas(a, b):
    # Realizo las cuatro operaciones básicas
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    # Devuelvo los cuatro resultados dentro de una tupla
    return (suma, resta, multiplicacion, division)


# Pido los dos números al usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# Guardo cada resultado de la tupla en una variable
suma, resta, multiplicacion, division = operaciones_basicas(a, b)

# Muestro los resultados de forma clara
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

#Ejercicio 8: Creo una función que calcula el IMC
def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    return imc


# Pido los datos al usuario
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Calculo y muestro el IMC con dos decimales
print("Su IMC es:", round(calcular_imc(peso, altura), 2))

#Ejercicio 9: Creo una función que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Pido la temperatura al usuario
celsius = float(input("Ingrese la temperatura en Celsius: "))

# Muestro la temperatura convertida
print("La temperatura en Fahrenheit es:", celsius_a_fahrenheit(celsius))

#Ejercicio 10: Creo una función que calcula el promedio de tres números
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


# Pido los tres números al usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

# Muestro el promedio
print("El promedio es:", calcular_promedio(a, b, c))
