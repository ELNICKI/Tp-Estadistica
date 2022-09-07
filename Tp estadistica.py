from itertools import count
import pandas as pd

#Abro el archivo como una variable.
miArchivo = open("TUP8.txt", "r")

#Creo una variable como el archivo leído
datos = miArchivo.read()

#Por cada ";" que aparezca en el archvio, creo un elemento singular en la lista 'datosLista'.
datosLista = datos.split(";")

#Creamos una comprensión de lista, que elimine los elementos vacíos.
listaLimpia = [int(i) for i in datosLista if i != '']

#Creamos la variable muestraTotal (Es la cantidad total de elementos con los que contamos).
muestraTotal = int(len(listaLimpia))

#Ordenamos la listaLimpia(lista de todos los datos) de menor a mayor.
listaLimpia.sort()

#Imprimimos la longitud total de la lista
print("La muestra es de:" , muestraTotal, "datos.")

#Lista que contiene el dato y su frecuencia.
listaValores = []
auxiliar = 0

#Guardamos el primer valor de la lista en un auxiliar.
if listaLimpia[0] != auxiliar:
    listaValores.append(listaLimpia[0])
    auxiliar = listaLimpia[0]

#Recorremos la lista y añadimos los elementos que no se repiten a una nueva lista.
for i in listaLimpia:
    if i != auxiliar:
        listaValores.append(i)
        auxiliar = i

#Imprimimos la lista con los valores que no se repiten
print(listaValores)

#Rellenamos las frecuencias de los valores y creamos una variable para las frecuencias.
listaFrecuencia = [0]

#Creamos una variable iterador. Volvimos a valorizar el auxiliar con el primer dato de listaLimpia.
#Iteramos listaLimpia y para cada uno de sus elemento si son distintos al auxiliar, en la locación que tiene listaFrecuencia con índice(iterador) sumamos uno a la frecuencia.
#Sumamos uno al iterador una vez que no se repita más el número que tiene el auxiliar guardado.
iterador = 0
auxiliar = listaLimpia[0]
for i in listaLimpia:
    if i != auxiliar:
        auxiliar = i
        iterador += 1
        listaFrecuencia.append(0)
    listaFrecuencia[iterador] += 1

print(listaFrecuencia)
print(len(listaValores))
print(len(listaFrecuencia))

#Corroboramos que la sumatoria de frecuencias sea igual a el número de la muestra total.
print(muestraTotal)
print(sum(listaFrecuencia))

#Cierre del archivo.
miArchivo.close()