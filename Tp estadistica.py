import pandas as pd
from statistics import mean, median, mode, multimode , variance
import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt

#Abro el archivo como una variable.
miArchivo = open("TUP2.txt", "r")

#Creo una variable como el archivo leído
datos = miArchivo.read()

#Por cada ";" que aparezca en el archvio, creo un elemento singular en la lista 'datosLista'.
listaDatos = datos.split(";")
listaDatos = list(map(int, listaDatos))

#Creamos la variable muestraTotal (Es la cantidad total de elementos con los que contamos).
muestraTotal = len(listaDatos)

#Ordenamos la datosLista(lista de todos los datos) de menor a mayor.
listaDatos.sort()

#Lista que contiene cada dato sin repetir.
listaValores = [listaDatos[0]]

#Guardamos el primer valor de la lista en un auxiliar.
auxiliar = 0

menoresA70 = 0

#Recorremos la lista y añadimos los elementos que no se repiten a una nueva lista.
for i in listaDatos:
    if i != auxiliar:
        listaValores.append(i)
        auxiliar = i
    if i < 70000:
        menoresA70 = menoresA70 + 1

porcentajeMenoresA70 = round((menoresA70 / muestraTotal) * 100 ,5)

#Variables para agrupados.
datosIntervalo1 = 0
datosIntervalo2 = 0
datosIntervalo3 = 0
datosIntervalo4 = 0
datosIntervalo5 = 0
datosIntervalo6 = 0
datosIntervalo7 = 0
datosIntervalo8 = 0
datosIntervalo9 = 0
frecuenciasAbsolutasIntervalos = []

for i in listaDatos:
    if i >= 55000 and i < 63000:
        datosIntervalo1 += 1
    elif i >= 63000 and i < 71000:
        datosIntervalo2 += 1
    elif i >= 71000 and i < 79000:
        datosIntervalo3 += 1
    elif i >= 79000 and i < 87000:
        datosIntervalo4 += 1
    elif i >= 87000 and i < 95000:
        datosIntervalo5 += 1
    elif i >= 95000 and i < 103000:
        datosIntervalo6 += 1
    elif i >= 103000 and i < 111000:
        datosIntervalo7 += 1
    elif i >= 111000 and i < 119000:
        datosIntervalo8 += 1
    else:
        datosIntervalo9 += 1

frecuenciasAbsolutasIntervalos.append(datosIntervalo1)
frecuenciasAbsolutasIntervalos.append(datosIntervalo2)
frecuenciasAbsolutasIntervalos.append(datosIntervalo3)
frecuenciasAbsolutasIntervalos.append(datosIntervalo4)
frecuenciasAbsolutasIntervalos.append(datosIntervalo5)
frecuenciasAbsolutasIntervalos.append(datosIntervalo6)
frecuenciasAbsolutasIntervalos.append(datosIntervalo7)
frecuenciasAbsolutasIntervalos.append(datosIntervalo8)
frecuenciasAbsolutasIntervalos.append(datosIntervalo9)


frecuenciasAbsAcumIntevalos = []
auxiliar = 0
for i in frecuenciasAbsolutasIntervalos:
    frecuenciasAbsAcumIntevalos.append(i + auxiliar)
    auxiliar= auxiliar + i

frecuenciasRelativasIntervalos = []
frecuenciasRelAcumIntervalos = []

for i in frecuenciasAbsolutasIntervalos:
    frecuenciasRelativasIntervalos.append(round((i / muestraTotal), 5))

for i in frecuenciasAbsAcumIntevalos:
    frecuenciasRelAcumIntervalos.append(round((i / muestraTotal), 2))

#Rellenamos las frecuencias de los valores y creamos una variable para las frecuencias.
listaFrecuenciasAbsolutas = [0]

#Creamos una variable iterador. Volvimos a valorizar el auxiliar con el primer dato de datosLista.
#Iteramos datosLista y para cada uno de sus elemento si son distintos al auxiliar, en la locación que tiene listaFrecuencia con índice(iterador) sumamos uno a la frecuencia.
#Sumamos uno al iterador una vez que no se repita más el número que tiene el auxiliar guardado.
iterador = 0
auxiliar = listaDatos[0]
for i in listaDatos:
    if i != auxiliar:
        auxiliar = i
        iterador += 1
        listaFrecuenciasAbsolutas.append(0)
    listaFrecuenciasAbsolutas[iterador] += 1

#Cálculo de frecuencias absoluta acumulada.
listaFrecuenciasAbsAcum = []
auxiliar = 0
for i in listaFrecuenciasAbsolutas:
    listaFrecuenciasAbsAcum.append(i + auxiliar)
    auxiliar += i

#Cálculos de frecuencias relativas y frecuencias relativas acumuladas.
listaFrecuenciasRelativas = []
listaFrecuenciasRelAcum = []

for i in listaFrecuenciasAbsolutas:
    listaFrecuenciasRelativas.append(round(i / muestraTotal, 5))

for i in listaFrecuenciasAbsAcum:
    listaFrecuenciasRelAcum.append(round(i / muestraTotal , 5))


intervalos = list(range(55000, 127000, 8000))
 
#Valores.
print("La muestra es de:",muestraTotal)
print("La sumatoria de frecuencias es:",sum(listaFrecuenciasAbsolutas))
print("La cantidad de elementos no repetidos son:", len(listaValores))
print("El valor mínimo es:", listaValores[0])
print("El valor máximo es:", listaValores[-1])
print("Datos agrupados en intervalos de 8000 km.")
print("Los autos que realizan la VTV con menos de 70 mil km son:",menoresA70)
print("El porcentaje de los autos que realizan la VTV con menos de 70 mil km son:", porcentajeMenoresA70, "%")
print("Frecuencias por cada intervalo:",frecuenciasAbsolutasIntervalos)
print("Frecuencias acumuladas por intervalos:", frecuenciasAbsAcumIntevalos)
print("Frecuencias relativas por intervalos:", frecuenciasRelativasIntervalos)
print("Frecuencias relativas acumuladas por intervalos:", frecuenciasRelAcumIntervalos)

#Cálculos de medidas de tendencias
print("Esta es la moda más pequeña:" , mode(listaDatos))
print("Esta es la mediana:" ,median(listaDatos))
print("Esta es la media:", round(mean(listaDatos),2))
print("Estas son todas las modas:", multimode(listaDatos), "C/U se repite 12 veces.")

#Cálculo de medidas de dispersión.
print("Esta es la varianza:" ,round(variance(listaDatos),4))
print("Este es el desvío estandar:", round(np.sqrt(variance(listaDatos)),4))
print("Este es el coeficiente de variación:", round((np.sqrt(variance(listaDatos))/ round(mean(listaDatos),2)) * 100, 2) , "%")
print("Este es el coeficiente de asimetría de pearson:", round(skew(listaDatos),4))
print("Posición de P sub 30 en la frecuencia absoluta acumulada.", (30 * muestraTotal)/ 100)
print("P sub 30, se encuentra en el tercer intervalo.")
print("Por debajo de", round((71000 + ((((30 * muestraTotal) / 100) - 48157) / 23990) * 8000)), "se encuentra el 30%" , "de los datos.")

#Cierre del archivo.
miArchivo.close()


df = pd.DataFrame({"x": intervalos, "f": frecuenciasAbsolutasIntervalos, "F": frecuenciasAbsAcumIntevalos, "fr": frecuenciasRelativasIntervalos, "Fr": frecuenciasRelAcumIntervalos})
print(df)


intervalos=[55000, 63000, 71000, 79000, 86000, 95000, 103000, 111000, 119000, 127000]

plt.xticks(intervalos)
plt.hist(listaDatos, bins=intervalos)

y,edges,_=plt.hist(listaDatos, bins=intervalos, histtype='step', edgecolor='k')

midpoints=0.5*(edges[1:]+edges[:-1])
plt.plot(midpoints,y, 'r-*')



plt.show()