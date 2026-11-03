from Alumno import Alumno
from Nota import Nota

cantidadAlumnos = int(input("Ingrese la cantidad de alumnos: "))

alumnos = []

for i in range(cantidadAlumnos):

    nombreCompleto = input("Ingrese su nombre completo: ")
    legajo = int(input("Ingrese el numero de legajo: "))

    alumno = Alumno(nombreCompleto, legajo)

    cantidadNotas = int(input("Ingrese la cantidad de notas: "))

    while cantidadNotas < 1:
        cantidadNotas = int(input("Debe ingresar al menos una nota: "))

    for j in range(cantidadNotas):

        catedra = input("Ingrese el nombre de la catedra: ")
        notaExamen = float(input("Ingrese la nota del examen: "))

        nota = Nota(catedra, notaExamen)
        alumno.agregar_nota(nota)

    alumnos.append(alumno)

    for alumno in alumnos:

      print("Nombre:", alumno.nombreCompleto)
    print("Legajo:", alumno.legajo)
        
    for nota in alumno.notas:
                print("Catedra:", nota.catedra)
                print("Nota:", nota.notaExamen)
        
    print("Promedio:", alumno.calcular_promedio())