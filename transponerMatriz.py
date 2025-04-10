M = int(input("Ingrese la cantidad de filas:"))
N = int(input("Ingrese la cantidad de columnas:"))
matriz = [[0 for j in range(N)] for i in range(M)]
import random

for i in range(M):
    for j in range(N):
        matriz[i][j] = random.randrange(1, 100)

for fila in matriz:
    print(fila)

print()

#Lo de arriba es solo llenar la matriz
#Ahora la vamos a transponer
#Notese que si era una matriz MxN originalmente, la transpuesta quedará NxM

matrizTranspuesta = [[0 for j in range(M)] for i in range(N)]

for i in range(M):
    for j in range(N):
        matrizTranspuesta[j][i] = matriz[i][j]

for fila in matrizTranspuesta:
    print(fila)