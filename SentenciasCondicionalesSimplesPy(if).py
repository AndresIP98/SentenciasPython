print("Sistema para calcular el promedio de un alumno.")
nombre=input("para comenzar, ¿cual es tu nombre?: ")

matematicas=int(input(nombre + " ¿Cual es tu calificacion en matematicas?: "))
quimica=int(input(nombre + " ¿Cual es tu calificacion en quimica?: "))
biologia=int(input(nombre + " ¿Cual es tu calificacion en biologia? "))

promedio= (matematicas + quimica + biologia) / 3
promedio = int(promedio) #convertir valor a entero

if promedio >= 6:
    print('Excelente ' + nombre + ' "aprobaste" con un promedio de: ', promedio)


print("Fin.")
