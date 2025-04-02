N = int(input("Ingrese la cantidad de filas: "))
M = int(input("Ingrese la cantidad de columnas: "))
numero = 1

matriz = [[0 for j in range(M)] for i in range(N)]
# Se inicializa la matriz con ceros
#El bucle interno crea una fila con M ceros (cant columnas)
#El bucle externo crea N filas (cant filas)
#Es una lista de listas, donde cada sublista representa una fila de la matriz

for i in range(N):
    for j in range(M):
        matriz[i][j] = numero
        numero += 1

for fila in matriz:
    print(fila)