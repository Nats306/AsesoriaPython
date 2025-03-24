#Almacenar N números en un vector, elevar al cuadrado cada valor almacenado en el mismo,
#almacenar el resultado en otro vector. Mostrar el vector original y el vector resultante.

n = int(input("Ingrese la cantidad de elementos: "))
vectorA = [0]*n
vectorB = [0]*n

for i in range(0,n):
    vectorA[i] = int(input(f"Ingrese el elemento en posición {i}: "))

print(f"Vector A: {vectorA}")

for i in range(0,n):
    vectorB[i] = vectorA[i]*vectorA[i]

print(f"Vector B: {vectorB}")
