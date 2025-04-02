#Hacer un programa que forme dos vectores numéricos enteros A y B de igual tamaño.
#Dichos valores deben ser ingresados de a uno por teclado.
#Crear un tercer vector que, mediante una fucnion, almacene la suma de cada uno de los elementos de los dos vectores iniciales.

def sumaVector(vectorA, vectorB, vectorC):
    for i in range(n):
        vectorC[i] = vectorA[i] + vectorB[i]
    return vectorC
n = int(input("Ingrese el tamaño de los vectores: "))

vectorA = [0]*n
VectorB = [0]*n
VectorC = [0]*n

for i in range(n):
    vectorA[i] = int(input(f"Ingrese el elemento en posición {i} del vector A: "))
    VectorB[i] = int(input(f"Ingrese el elemento en posición {i} del vector B: "))

print("El vector A es: ", vectorA)
print("El vector B es: ", VectorB)
sumaVector(vectorA, VectorB, VectorC)
print("El vector C es: ", VectorC)