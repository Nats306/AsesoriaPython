#1) Llenar un vector con N elementos, imprimir la posición y el valor del elemento mayor
#almacenado en el vector. Suponga que todos los elementos del vector son diferentes.

n = int(input("Ingrese la cantidad de elementos: "))

array = [0]*n

for i in range(n):
    array[i] = input(f"Ingrese el elemento en posición {i}:")
     
elementomayor = array[0]
posicionmayor = 0

for i in range(1,n):
    if array[i] > elementomayor:
        elementomayor = array[i]
        posicionmayor = i

print(f"El mayor elemento es {elementomayor} y está en posición {posicionmayor}")