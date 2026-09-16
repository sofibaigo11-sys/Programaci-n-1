import random

# 1) Mostrar los números del 0 al 100
for numero in range(101):
        print(numero)


# 2) Contar la cantidad de dígitos de un número
numero = int(input("Ingrese un número entero: "))

# abs() permite trabajar también con números negativos
cantidad_digitos = len(str(abs(numero)))

print("La cantidad de dígitos es:", cantidad_digitos)


# 3) Sumar los números entre dos valores, sin incluirlos
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

menor = min(valor1, valor2)
mayor = max(valor1, valor2)
suma = 0

for numero in range(menor + 1, mayor):
    suma += numero

print("La suma es:", suma)


# 4) Sumar números hasta que se ingrese 0
suma = 0
numero = int(input("Ingrese un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número (0 para terminar): "))

print("El total acumulado es:", suma)


# 5) Juego de adivinar un número
numero_secreto = random.randint(0, 9)
intentos = 0
numero_ingresado = -1

while numero_ingresado != numero_secreto:
    numero_ingresado = int(input("Adivine el número entre 0 y 9: "))
    intentos += 1

    if numero_ingresado < numero_secreto:
        print("El número secreto es mayor.")
    elif numero_ingresado > numero_secreto:
        print("El número secreto es menor.")

print("¡Correcto!")
print("Cantidad de intentos:", intentos)


# 6) Mostrar números pares del 100 al 0
for numero in range(100, -1, -2):
    print(numero)


# 7) Sumar los números entre 0 y un número positivo
numero = int(input("Ingrese un número entero positivo: "))

while numero < 0:
    print("El número debe ser positivo.")
    numero = int(input("Ingrese un número entero positivo: "))

suma = 0

for valor in range(numero + 1):
    suma += valor

print("La suma es:", suma)


# 8) Contar pares, impares, positivos y negativos
CANTIDAD = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

for contador in range(CANTIDAD):
    numero = int(input(f"Ingrese el número {contador + 1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)


# 9) Calcular la media de 100 números
CANTIDAD = 100
suma = 0

for contador in range(CANTIDAD):
    numero = int(input(f"Ingrese el número {contador + 1}: "))
    suma += numero

media = suma / CANTIDAD

print("La media es:", media)


# 10) Invertir los dígitos de un número
numero = int(input("Ingrese un número entero: "))

signo = ""

if numero < 0:
    signo = "-"
    numero = abs(numero)

numero_invertido = str(numero)[::-1]

print("Número invertido:", signo + numero_invertido)
