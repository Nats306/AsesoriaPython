n = int(input("Ingrese número total de estudiantes: "))

cont1 = 0  # Contador para promedios <= 3
cont2 = 0  # Contador para 3 < promedio <= 4
cont3 = 0  # Contador para promedios > 4

i = 0
while i < n:
    codigo = input("Ingrese su código: ")
    
    codigo = input("Ingrese su código: ")
    notaMateria1 = input("Ingrese la nota de la materia 1: ")
    creditosMateria1 = input("Ingrese los créditos de la materia 1: ")
    notaMateria2 = input("Ingrese la nota de la materia 2: ")
    creditosMateria2 = input("Ingrese los créditos de la materia 2: ")
    notaMateria3 = input("Ingrese la nota de la materia 3: ")
    creditosMateria3 = input("Ingrese los créditos de la materia 3: ")
    notaMateria4 = input("Ingrese la nota de la materia 4: ")
    creditosMateria4 = input("Ingrese los créditos de la materia 4: ")
    
    sumCreditos = creditosMateria1 + creditosMateria2 + creditosMateria3 + creditosMateria4
    promedioCreditos= (notaMateria1*creditosMateria1) + (notaMateria2*creditosMateria2) + (notaMateria3*creditosMateria3) + (notaMateria4*creditosMateria4)
    if promedioCreditos >5 or promedioCreditos < 0:
        print("Error, el promedio no puede ser mayor a 5 ni menor a 0")
        continue
    if promedioCreditos <= 3:
        cont1 += 1
    elif 3 < promedioCreditos <= 4:
        cont2 += 1
    else:
        cont3 += 1
    
    print(f"Los créditos cursados del estudiante con código {codigo} son: {sumCreditos}")
    print(f"Además, su promedio crédito es de: {promedioCreditos}\n")
    
    i += 1

print(f"La cantidad de estudiantes con promedio menor o igual a 3 son: {cont1}")
print(f"La cantidad de estudiantes con promedio mayor a 3 y menor o igual a 4 son: {cont2}")
print(f"La cantidad de estudiantes con promedio mayor que 4 son: {cont3}")
