#5) Almacenar N números en un vector, mostrar cuantos términos son ceros, cuántos son negativos
#y cuantos positivos. Mostrar además la suma de los negativos y la suma de los positivos.*/

n = int(input("Ingrese cantidad de elementos: "))
array = [0]*n

for i in range(0,n):
    array[i] = int(input(f"Ingrese el valor del elemento en posición {i}:"))
   
contnegativos = 0
contpositivos = 0
contcero = 0
sumanegativos = 0
sumapositivos = 0

for i in range(0,n):
    if array[i] == 0:
        contcero += 1
    elif array[i] > 0:
        contpositivos += 1
        sumapositivos += array[i]
    else:
        contnegativos += 1
        sumanegativos += array[i]

print(f"La cantidad de elementos que son cero es de: {contcero}")
print(f"La cantidad de elementos que son negativos es de: {contnegativos}")
print(f"La cantidad de elementos que son positivos es de: {contpositivos}")
print(f"La suma de los números positivos es de: {sumapositivos}")
print(f"La suma de los números negativos es de: {sumanegativos}")
