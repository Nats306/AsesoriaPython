import random 
temperaturas = [0]*30
i=0
contG = 0
contF = 0
contM = 0
contC = 0
contE = 0
sumTemperaturas = 0
maxTemp=0
minTemp=0
diaMaxTemp= -20
diaMinTemp= 50
diasCalor = []
diasConsecutivos = []

while i < 30:
    tipo=""
    temperaturas[i] = random.randint(-10,40)
    sumTemperaturas += temperaturas[i]
    if temperaturas[i] < 0:
        tipo = "Gélido"
        contG += 1
    elif temperaturas[i] > 0 and temperaturas[i] < 15:
        tipo = "Frío"
        contF += 1
    elif temperaturas[i] > 15 and temperaturas[i] < 25:
        tipo = "Moderado"
        contM += 1
    elif temperaturas[i] > 25 and temperaturas[i] < 35:
        tipo = "Caluroso"
        contC += 1
        diasCalor.append(i+1)
    else:
        tipo = "Extremo"
        contE += 1
        diasCalor.append(i+1)

    if temperaturas[i]<minTemp:
        minTemp = temperaturas[i]
        diaMinTemp = i+1
    
    if temperaturas[i]>maxTemp:
        maxTemp = temperaturas[i]
        diaMaxTemp = i+1
    
    print(f"En el dia {i+1} la temperatura fue de {temperaturas[i]} que cae en la categoria de {tipo}")

    i = i+1

print(f"El total de días en la categoria gélido fue: {contG}")
print(f"El total de días en la categoria frío fue: {contF}")
print(f"El total de días en la categoria moderado fue: {contM}")
print(f"El total de días en la categoria caluroso fue: {contC}")
print(f"El total de días en la categoria extremo fue: {contE}")

print(f"La temperatura media del mes fue de: {round(sumTemperaturas/30,0)}")

print(f"La temperatura máxima registrada fue {maxTemp} y ocurrió en el día {diaMaxTemp}")
print(f"La temperatura minima registrada fue {minTemp} y ocurrió en el día {diaMinTemp}")

diasConsecutivosTemp = []  

for j in range(len(diasCalor)):
    if not diasConsecutivosTemp or diasCalor[j] == diasConsecutivosTemp[-1] + 1:
        diasConsecutivosTemp.append(diasCalor[j])
    else:
        if len(diasConsecutivosTemp) >= 3:
            diasConsecutivos.append(diasConsecutivosTemp)
        diasConsecutivosTemp = [diasCalor[j]]

if len(diasConsecutivosTemp) >= 3:
    diasConsecutivos.append(diasConsecutivosTemp)

if diasConsecutivos:
    for rango in diasConsecutivos:
        print(f"Hubo al menos 3 días consecutivos de calor/extremos: desde el día {rango[0]} hasta el día {rango[-1]}")
else:
    print("No hubo al menos 3 días consecutivos de calor o extremos.")
