import pandas as pd

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
auxiliar = listaDatos[0]

#Recorremos la lista y añadimos los elementos que no se repiten a una nueva lista.
for i in listaDatos:
    if i != auxiliar:
        listaValores.append(i)
        auxiliar = i

#Rellenamos las frecuencias de los valores y creamos una variable para las frecuencias.
listaFrecuencia = [0]

#Creamos una variable iterador. Volvimos a valorizar el auxiliar con el primer dato de datosLista.
#Iteramos datosLista y para cada uno de sus elemento si son distintos al auxiliar, en la locación que tiene listaFrecuencia con índice(iterador) sumamos uno a la frecuencia.
#Sumamos uno al iterador una vez que no se repita más el número que tiene el auxiliar guardado.
iterador = 0
auxiliar = listaDatos[0]
for i in listaDatos:
    if i != auxiliar:
        auxiliar = i
        iterador += 1
        listaFrecuencia.append(0)
    listaFrecuencia[iterador] += 1

print(len(listaValores))
print(len(listaFrecuencia))

#Corroboramos que la sumatoria de frecuencias sea igual a el número de la muestra total.
print(muestraTotal)
print(sum(listaFrecuencia))

df = pd.DataFrame(list(zip(listaValores,listaFrecuencia)), columns=["Valores", "Frecuencia"])
print(df)


#Cierre del archivo.
miArchivo.close()
