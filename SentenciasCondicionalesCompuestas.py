num_uno= 16
if num_uno == 16:
    print("El numero es dieciseis.")
else:
    print("El numero NO es dieciseis.")
print("Fin.")

num_uno= 10
if num_uno == 16:
    print("El numero es dieciseis.")
else:
    print("El numero NO es dieciseis.")
print("Fin.")


print("Sistema para calcular el promedio de un alumno.")
nombre=input("para comenzar, ¿cual es tu nombre?: ")

matematicas=int(input(nombre + " ¿Cual es tu calificacion en matematicas?: "))
quimica=int(input(nombre + " ¿Cual es tu calificacion en quimica?: "))
biologia=int(input(nombre + " ¿Cual es tu calificacion en biologia? "))

promedio= (matematicas + quimica + biologia) / 3
#promedio = int(promedio) #convertir valor a entero

if promedio >= 6:
    print('Excelente ' + nombre + ' "aprobaste" con un promedio de: ', promedio)
    print('Excelente ' + nombre + ' "aprobaste" con un promedio de: ', round(promedio,1))#round para elejir cuantos decimales mostrar
else:
    print("Lo sentimos " + nombre + " has 'reprobado' con un promedio de: ", promedio)
    print("Lo sentimos " + nombre + " has 'reprobado' con un promedio de: ", round(promedio,1))
print("Fin.")

    

    



