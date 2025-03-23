
#22. Un centro asistencial para lisiados recibe N pacientes por semana, con el fin de que les hagan alguna 
#prótesis. Teniendo en cuenta que el estado civil de los asistentes puede ser: soltero, casado, separado, viudo o 
#de unión libre, diseñe un algoritmo que determine:
#a) El porcentaje de hombres solteros que allí han asistido en una semana
#respecto al total de hombres asistentes.
#b) La edad promedio de mujeres mayores de edad que sean casadas.
#c) ¿Qué porcentaje de mujeres mayores de edad, pero menores de 25 años y de unión libre, respecto al total de
#asistentes, que han ido a dicho centro?
#d) El porcentaje de hombres solteros mayores de 30 años, respecto al total de asistentes.
#e) El porcentaje de mujeres entre 26 y 38 años, respecto al total de mujeres, que son viudas.
#f) ¿El asistente de más edad es hombre o mujer?, ¿cuál es su estado civil?*/

n = int(input("Introduce un número de clientes: "))

edadmayor=0
conthombressolteros = 0
conthombres = 0
contmujeres = 0
contmujerescasadas_mayoresdeedad = 0
contmuj18_25_unionlibre = 0
conthombressolterosmayores30 = 0
contmuj26_38_viudas = 0
sumaedadcasadas_mayoresdeed = 0
estadociviledadmayor = ""
sexoedadmayor = ""
nombreedadmayor = ""

i=0
for i in range(0,n):
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    sexo = input("Introduce tu sexo (H/M): ")
    estado_civil = input("Introduce tu estado civil (Sol, C, Sep, V, UL): ")

    if edad > edadmayor:
        nombreedadmayor = nombre
        edadmayor = edad
        estadociviledadmayor = estado_civil
        sexoedadmayor = sexo

    if sexo == 'H':
        conthombres += 1
        if estado_civil == 'S':
            conthombressolteros += 1
            if edad > 30:
                conthombressolterosmayores30 += 1
    else:
        contmujeres += 1
        if edad >= 18:
            if estado_civil == "C":
                contmujerescasadas_mayoresdeedad += 1
                sumaedadcasadas_mayoresdeed += edad
            
            if edad < 25 and estado_civil == "UL":
                contmuj18_25_unionlibre += 1
        
        if edad >= 35 and edad <= 38:
            if estado_civil == "V":
                contmuj26_38_viudas += 1


porcentajehombressolteros = 100 * conthombressolteros /conthombres
edadpromediopuntob = sumaedadcasadas_mayoresdeed / contmujerescasadas_mayoresdeedad
porcentajepuntoc = 100 * contmuj18_25_unionlibre / n
porcentajepuntod = 100 * conthombressolterosmayores30 / n
porcentajepuntoe = 100 * contmuj26_38_viudas / contmujeres


print(f"El porcentaje de hombres solteros respecto al total de hombres asistentes es de: {porcentajehombressolteros}%")
print(f"La edad promedio de mujeres mayores de edad que sean casadas es de: {edadpromediopuntob}")
print(f"El porcentaje de mujeres mayores de edad, pero menores de 25 años y de unión libre, respecto al total de asistentes es de: {porcentajepuntoc}%")
print(f"El porcentaje de hombres solteros mayores de 30 años, respecto al total de asistentes es de: {porcentajepuntod}%")
print(f"El porcentaje de mujeres entre 26 y 38 años, respecto al total de mujeres, que son viudas es de: {porcentajepuntoe}%")
print(f"La edad, el sexo y el estado civil del asistente de más edad son: {edadmayor}, {sexoedadmayor}, {estadociviledadmayor}")
