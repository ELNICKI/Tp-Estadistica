import pandas as pd
import plotly.express as px

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

#Datos agrupados por intervalos.
listaDatosAgrupados = list(range(55000, 127000 + 1 , 6000))
menoresA70 = 0

#Recorremos la lista y añadimos los elementos que no se repiten a una nueva lista.
for i in listaDatos:
    if i != auxiliar:
        listaValores.append(i)
        auxiliar = i
    if i < 70000:
        menoresA70 = menoresA70 + 1

porcentajeMenoresA70 = round((menoresA70 / muestraTotal) * 100 ,2)

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

print("La cantidad de elementos no repetidos son:", len(listaValores))
print("La catidad de datos individuales, que aparecen 1 o más veces son:",len(listaFrecuenciasAbsolutas))

#Corroboramos que la sumatoria de frecuencias sea igual a el número de la muestra total.
print("La muestra es de:",muestraTotal)
print("La sumatoria de frecuencias es:",sum(listaFrecuenciasAbsolutas))

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
 
#Valores mínimo y máximo.
print("El valor mínimo es:", listaValores[0])
print("El valor máximo es:", listaValores[-1])
print("Datos agrupados de a 6000 km.")
print(listaDatosAgrupados)
print("Los autos que realizan la VTV con menos de 70 mil km son:",menoresA70)
print("El porcentaje de los autos que realizan la VTV con menos de 70 mil km son:", porcentajeMenoresA70, "%")


#Cierre del archivo.
miArchivo.close()


#Plotly.
numero_intervalos = max(listaDatos) - min(listaDatos) + 1

histograma = px.histogram(listaDatos,
                          nbins=numero_intervalos,
                          title='Histograma de edades - Plotly - codigopiton.com',
                          color_discrete_sequence=['#F2AB6D'])

# configuramos las etiquetas de los ejes
histograma.update_layout(
    xaxis_title="Edades",
    yaxis_title="Frecuencia"
)

histograma.show()