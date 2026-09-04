# Práctico 1: Estructuras Secuenciales

# Ejercicio 1: Imprimir "Hola Mundo!" en pantalla
print("Hola Mundo!")

# Ejercicio 2: Solicitar al usuario su nombre y saludarlo
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3: Solicitar al usuario su nombre, apellido, edad y lugar de nacimiento
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# Ejercicio 4: Solicitar al usuario el radio de un círculo y calcular su área y perímetro
radio = float(input("Ingrese el radio del círculo: "))
area = 3.14159 * radio ** 2
perimetro = 2 * 3.14159 * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# Ejercicio 5: Solicitar al usuario una cantidad de segundos y convertirlo a horas.
segundos = float(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas} horas")

# Ejercicio 6: Solicitar al usuario un número y mostrar su tabla de multiplicar
numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {numero}")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7: Solicitar al usuario dos números distintos de 0 
a = int(input("Ingrese el primer número distinto de 0: "))
b = int(input("Ingrese el segundo número distinto de 0: "))
# Mostrar la suma, la resta, la multiplicación, y la división de ambos números.
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")

# Ejercicio 8: Solicitar al usuario su peso y altura.
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
# Calcular el índice de masa corporal (IMC) y mostrarlo en pantalla.
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {imc}")

# Ejercicio 9: Solicitar al usuario una temperatura en grados Celsius y convertirlo a Farenheit.
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit}°F")

# Ejercicio 10: Solicitar al usuario tres números y calcular su promedio.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio}")
