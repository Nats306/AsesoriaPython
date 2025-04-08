import random
M= int(input("Ingrese la cantidad de filas: "))
N= int(input("Ingrese la cantidad de columnas: "))
cantidadElementos = M*N
sumaElementos = 0
ValorMax = 0

if(M==N):
    print("La matriz es cuadrada")
else:
    print("La matriz no es cuadrada")

matriz = [[0 for j in range(N)] for i in range(M)]

for i in range(M):
    for j in range(N):
        matriz[i][j] = random.randrange(1, 100)
        sumaElementos += matriz[i][j]

for fila in matriz:
    print(fila)

promedio = sumaElementos/cantidadElementos
print("El promedio de los elementos es: ", promedio)

sumaElementosPorFila = 0
cantidadElementosPorFila = N

for i in range(M):
    for j in range(N):
        sumaElementosPorFila += matriz[i][j]
        if(j == N-1):
            promedioFila = sumaElementosPorFila/cantidadElementosPorFila
            print("El promedio de la fila ", i, " es: ", promedioFila)
            sumaElementosPorFila = 0

sumaElementosPorColumna = 0
cantidadElementosPorColumna = M

for j in range(N):
    for i in range(M):
        sumaElementosPorColumna += matriz[i][j]
        if(i == M-1):
            promedioColumna = sumaElementosPorColumna/cantidadElementosPorColumna
            print("El promedio de la columna ", j, " es: ", promedioColumna)
            sumaElementosPorColumna = 0


