#Hacer un programa que cree un vector númerico entero A de tamaño n.
#Los valores de dicho vector deben ser ingresados de uno por teclado.
#Luego, crear un segundo vector de igual tamaño que el anterior llamado producto.
#Mediante una función, almacenar el producto de de cada uno de los elementos del vector A con sus correspondientes subindices.

def productoPorIndice(A, n, producto):
    for i in range(n):
        producto[i] = A[i] * i
    return producto

n = int(input("Ingrese la cantidad de elementos: "))
A = [0]*n
producto = [0]*n

for i in range(n):
    A[i] = int(input(f"Ingrese el elemento en posición {i}:"))

print("El vector A es: ", A)
productoPorIndice(A, n, producto)
print("El vector producto es: ", producto)

