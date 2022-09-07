import pandas as pd

#Abro el archivo como una variable.
miArchivo = open("TUP8.txt", "r")

#Creo una variable como el archivo leído
datos = miArchivo.read()

#Por cada ";" que aparezca en el archvio, creo un elemento singular en la lista 'datosLista'.
datosLista = datos.split(";")

#Creamos una comprensión de lista, que elimine los elementos vacíos y los saltos de línea.
listaLimpia = [i for i in datosLista if i != '' and i != "\n"]

for i in listaLimpia:
    if type(i) == str:
        i = int(i)

#Imprimimos la lista ya modificada (Desordenada).
print(listaLimpia)

#Imprimo la logitud total de la lista modificada.
print("El número total de datos es: ", len(listaLimpia))

#Creamos la variable muestraTotal (Es la cantidad total de elementos con los que contamos).
muestraTotal = int(len(listaLimpia))

#Ordenamos la listaLimpia(lista de todos los datos) de menor a mayor.
listaLimpia.sort()
print(listaLimpia)

#Cierre del archivo.
miArchivo.close()