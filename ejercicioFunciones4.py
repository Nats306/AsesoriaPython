# Hacer un algoritmo que genere dos vectores de igual tamaño. Estos vectores son numericos enteros.
# Hacer un algoritmo que cree un tercer vector del mismo tamaño y almacene en este el factorial de la 
# suma de cada elemento correlacionado de los dos vectores anteriores. Esto mediante subprograma.
# Luego, hacer un cuarto vector que intercambie el orden del vector C.

def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def sumaVectores(vectorA, vectorB, vectorSum, n):
    for i in range(n):
        vectorSum[i] = vectorA[i] + vectorB[i]
    return vectorSum

def vecFactorial (vectorSum, vectorC, n):
    for i in range(n):
        vectorC[i] = factorial(vectorSum[i])
    return vectorC

def intercambiar(vectorC, vectorD, n):
    for i in range(n):
        vectorD[i] = vectorC[n-i-1]
    return vectorD

n = int(input("Ingrese el tamaño de los vectores: "))
vectorA = [0]*n
vectorB = [0]*n
vectorSum = [0]*n
vectorC = [0]*n
vectorD = [0]*n

for i in range(n):
    vectorA[i] = int(input(f"Ingrese el elemento en posición {i} del vector A: "))
    vectorB[i] = int(input(f"Ingrese el elemento en posición {i} del vector B: "))

print(vectorA)
print(vectorB)

sumaVectores(vectorA, vectorB, vectorSum, n)
vecFactorial(vectorSum, vectorC, n)
print(vectorC)

intercambiar(vectorC, vectorD, n)
print(vectorD)