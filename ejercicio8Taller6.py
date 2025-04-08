import random
M=3
N=5
matriz = [[0 for j in range(N)] for i in range(M)]
mayorValorMedioLitros = 0
litrosMedios = []
sumaFila = 0


for i in range(M):
    for j in range(N):
        matriz[i][j] = random.randrange(100, 800)

for i in range(M):
    for j in range(N):
        sumaFila += matriz[i][j]
        if(j == N-1):
            promedioFila = sumaFila/N
            litrosMedios.append(promedioFila)
            sumaFila = 0

valorMaximo = 0
for i in range(len(litrosMedios)):
    if(litrosMedios[i] > valorMaximo):
        valorMaximo = litrosMedios[i]

print("El mayor consumo de litros es: ", valorMaximo)

mayorConsumoCampo = []
mayorConsumoCampos = 0 
litrosCampo = 0
for j in range(N):
    for i in range(M):
        litrosCampo += matriz[i][j]
        if(i == M-1):
            mayorConsumoCampo.append(litrosCampo)
            litrosCampo = 0

for i in range(len(mayorConsumoCampo)):
    if(mayorConsumoCampo[i] > mayorConsumoCampos):
        mayorConsumoCampos = mayorConsumoCampo[i]
        
print("El mayor consumo de litros por campo es: ", mayorConsumoCampos)