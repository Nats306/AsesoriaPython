#3) Calcular el promedio de N valores almacenados en un vector. Determinar además cuantos son
#mayores que el promedio, imprimir el promedio, el número de datos mayores que el promedio y
#la lista de valores mayores que el promedio.

n = int(input("Ingrese la cantidad de elementos: "))
array = [0]*n
sumavalores = 0

for i in range(0,n):
    array[i] = int(input(f"Ingrese el valor de la posición {i}:"))
    sumavalores += array[i]

promedio =sumavalores/n
contmayores = 0

print("Los elementos mayores del promedio son:")

for i in range(0,n):
    if array[i] > promedio:
        contmayores += 1
        print(array[i])

print(f"La cantidad de elementos mayores al promedio son: {contmayores}")
