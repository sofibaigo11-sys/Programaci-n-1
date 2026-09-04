#ejercicio 1: Escribir un progama que solicite al usuario su edad y determine si es mayor de edad o no.
edad = int(input("Ingrese su edad: "))
#Si la edad es mayor de 18 años, imprimir "Es mayor de edad", caso contrario imprimir "No es mayor de edad".
if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#ejercicio 2: Escribir un programa que solicite al usuario su nota y determine si ha aprobado o no 
nota = float(input("Ingrese su nota: "))
#Si la nota es mayor o igual a 6, imprimir "Aprobado", caso contrario imprimir "Desaprobado".
if nota >= 6 and nota <= 10:
    print("Aprobado")
else:
    print("Desaprobado")

#ejercicio 3: Escribir un programa que permita ingresar solo numeros pares.
numero = int(input("Ingrese un número: "))
#Si el numero es par, imprimir "Ha ingresado un numero par".
if numero % 2 == 0:
    print("Ha ingresado un número par")
#Si el numero es impar, imprimir "Por favor, ingrese un numero par".
else:
    print("Ha ingresado un número impar")

#ejercicio 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a que categoria pertenece.
edad = int(input("Ingrese su edad: "))
if edad < 12:
    #Si la edad es menor de 12 años imprimir "Niño/a".
    print("Niño/a")
elif edad > 12 and edad < 18:
    #Si la edad es mayor o igual a 12 años y menor de 18 años imprimir "Adolescente".
    print("Adolescente")
elif edad >= 18 and edad < 30:
    #Si la edad es mayor o igual a 18 años y menor de 30 años imprimir "Adulto/a joven".
    print("Adulto/a joven")
else:
    #Si la edad es mayor o igual a 30 años imprimir "Adulto/a".
    print("Adulto/a")

#ejercicio 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (inclusive 8 y 14).
contraseña = input("Ingrese una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    #Si la contraseña tiene una longitud adecuada, imprimir "Ha ingresado una contraseña correcta".
    print("Ha ingresado una contraseña correcta")
else:
    #Si la contraseña no tiene una longitud adecuada imprimir "Por favor ingrese una contraseña de entre 8 y 14 caracteres".
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres:")

#ejercicio 6: Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y la compare para determinar si hay sesgo positivo, negativo o no hay sesgo.
import random
from statistics import mode, median, mean
#Generar una lista de 50 numeros aleatorios entre 1 y 100 utilizando la moda, la mediana y la media para determinar el sesgo de la distribucion de los numeros aleatorios. 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
#Imprimir la lista de numeros aleatorios, la media, la mediana y la moda.
print("Lista:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
#Comparar la media, la mediana y la moda para determinar si hay sesgo positivo, negativo o no hay sesgo.
if media > mediana and mediana > moda:
    print("Sesgo positivo")
    #Si la media es mayor que la mediana y la mediana es mayor que la moda, imprimir "Sesgo positivo".
elif media < mediana and mediana < moda:
    #Si la media es menor que la mediana y la mediana es menor que la moda, imprimir "Sesgo negativo".
    print("Sesgo negativo")
elif media == mediana and mediana == moda:
    #Si la media, la mediana y la moda son iguales, imprimir "Sin sesgo".
    print("Sin sesgo")
else:
    #Si no se puede determinar claramente el sesgo, imprimir "No se puede determinar claramente el sesgo".
    print("No se puede determinar claramente el sesgo")

#ejercicio 7: Escribir un programa que solicite al usuario una palabra o frase.
    texto = input("Ingrese una palabra o frase: ").strip()
    #Si la ultima letra del texto es una vocal (a,e,i,o,u), imprimir el texto seguido de un signo de exclamacion (!).
if texto : 
    ultima = texto[-1].lower()
    if ultima in "aeiouáéíóúAEIOU":
        print(texto + "!")
    else:
        #Si la ultima letra del texto no es una vocal, imprimir el texto tal cual.
        print(texto)
else:
    #Si el usuario no ingresa ningun texto, imprimir "No ingreso ningun texto".
    print("No ingresó ningún texto")

#ejercicio 8: Escribir un programa que solicite al usuario su nombre y luego le permita elegir entre convertirlo a mayusculas, minusculas o con la primera letra en mayuscula.
nombre = input("Ingrese su nombre:")
print("Seleccione una opción:")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con primera letra mayúscula")
opcion = input("Seleccione la opcion que desea 1,2 o 3:")
if opcion == "1":
        #Si el usuario elige la opcion 1, imprimir el nombre en mayusculas.
        print(nombre.upper())
elif opcion == "2":
        #Si el usuario elige la opcion 2, imprimir el nombre en minusculas.
        print(nombre.lower())
elif opcion == "3":
        #Si el usuario elige la opcion 3, imprimir el nombre con la primera letra en mayusculas.
        print(nombre.title())
else:
        #Si el usuario ingresa una opcion invalida, imprimir "Opcion invalida".
        print("Opción inválida")

#ejercicio 9: Escribir un programa que solicite al usuario la magnitud de un sismo y clasifique su intensidad segun la escala de Richter.
magnitud = float(input("Ingrese la magnitud del sismo: "))
if magnitud < 3:
        #Si la magnitud es menor a 3, imprimir "Muy leve (imperceptible)":
        clasificacion = "Muy leve (imperceptible)"
elif magnitud < 4:
        #Si la magnitud es mayor o igual a 3 y menor a 4, imprimir "Leve (ligeramente perceptible)".
        clasificacion = "Leve (ligeramente perceptible)"
elif magnitud < 5:
        #Si la magnitud es mayor o igual a 4 y menor a 5, imprimir "Moderado".
        clasificacion = "Moderado"
elif magnitud < 6:
        #Si la magnitud es mayor o igual a 5 y menor a 6, imprimir "Fuerte".
        clasificacion = "Fuerte"
elif magnitud < 7:
        #Si la magnitud es mayor o igual a 6 y menor a 7, imprimir "Muy fuerte".
        clasificacion = "Muy fuerte"
else:
        #Si la magnitud es mayor o igual a 7, imprimir "Extremo".
        clasificacion = "Extremo"
print(f"Clasificación: {clasificacion}")

#ejercicio 10: Escribir un programa que solicite al usuario eel hemisferio en el que se encuentra (N para norte, S para sur).
hemisferio = input("Ingrese hemisferio (N/S): ").upper()
#Solicitar al usuario el numero del mes y el dia para determinar la estacion del año en la que se encuentra segun el hemisferio.
mes = int(input("Ingrese el número del mes: "))
dia = int(input("Ingrese el día: "))
if hemisferio == "N":
    # Invierno 
    if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
        #Si el usuario se encuentra en el hemisferio norte y la fecha es entre  el 21 de diciembre y el 20 de marzo, imprimir "Invierno".
        print("Invierno")
    # Primavera
    elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
        #Si el usuario se encuentra en el hemisferio norte y la fecha es entre  el 21 de marzo y el 20 de junio, imprimir "Primavera".
        print("Primavera")
    # Verano
    elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
        #Si el usuario se encuentra en el hemisferio norte y la fecha es entre  el 21 de junio y el 20 de septiembre, imprimir "Verano".
        print("Verano")
    # Otoño
    else:
        #Si el usuario se encuentra en el hemisferio norte y la fecha no corresponde a ninguna de las anteriores, imprimir "Otoño".
        print("Otoño")
else:
    #Si el usuario se encuentra en el hemisferio sur, determinar la estacion del año segun la fecha ingresada y el hemisferio sur.
    # Verano
    if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
        print("Verano")
    #Si el usuario se encuentra en el hemisferio sur y la fecha es entre el 21 de diciembre y eel 20 de marzo, imprimir "Verano".
    # Otoño
    elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
        print("Otoño")
    #Si el usuario se encuentra en el hemisferio sur y la fecha es entre el 21 de marzo y el 20 de junio, imprimir "Otoño".
    # Invierno
    elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
        print("Invierno")
    #Si el usuario se encunetra en el hemisferio sur y la fecha es entre el 21 de junio y el 20 de septiembre, imprimir "Invierno".
    # Primavera
    else:
    #Si el usuario se encuentra en el hemisferio sur y la fecha no corresponde a ninguna de las anteriores, imprimir "Primavera".
        print("Primavera")