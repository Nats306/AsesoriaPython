import random
N = int(input("Ingrese el tamaño de la matriz:"))

matriz = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        matriz[i][j] = random.randrange(1, 100)

for fila in matriz:
    print(fila)

diagonalPrincipal = []
diagonalSecundaria = []

for i in range(N):
    for j in range(N):
        if i==j:
            diagonalPrincipal.append(matriz[i][j])
    diagonalSecundaria.append(matriz[i][N-i-1])

print("Diagonal Principal: ", diagonalPrincipal)
print("Diagonal Secundaria: ", diagonalSecundaria)
