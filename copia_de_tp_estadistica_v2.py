# -*- coding: utf-8 -*-
"""Copia de tp_estadistica_V2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mdCJWaIKjV-x5ku0ai3gutsxGoseyC1d
"""

!pip install PyDrive pandas numpy matplotlib scipy gdown

# LINK de share: https://drive.google.com/file/d/1EKnr9m--vsEeX9x4sJQ58m3dkl7_23ub/view?usp=sharing
# ID: 1EKnr9m--vsEeX9x4sJQ58m3dkl7_23ub
# LINK DE DESCARGA: https://drive.google.com/uc?id=1EKnr9m--vsEeX9x4sJQ58m3dkl7_23ub
!gdown https://drive.google.com/uc?id=1EKnr9m--vsEeX9x4sJQ58m3dkl7_23ub
#1_4
#!gdown https://drive.google.com/uc?id=1EKnr9m--vsEeX9x4sJQ58m3dkl7_23ub

#Nombre del archivo CAMBIAR
archivo = 'TUP2.txt'
with open(archivo, "r") as r:
  with open('data.csv', "w") as w:
    w.write(r.read().replace(';' , '\n'))

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statistics
# %matplotlib inline

df = pd.read_csv('data.csv', header=None)
res, bins = pd.cut(df[df.columns[0]],range(55000, 130000, 8000), right=False, retbins=True)
res = pd.DataFrame(res)
res

res.value_counts().to_csv('tabla_frecuencia.csv')
res.value_counts()

samples = res.value_counts().sort_index()
samples.to_numpy().flatten()

fig, ax = plt.subplots(figsize=(6, 3.5))
(
    pd.Series(samples).plot.bar(ax=ax)
)

# Creamos histograma de frecuencias
fig, ax = plt.subplots(figsize=(6, 3.5))
(
    pd.Series(samples/samples.sum(axis=0)).plot.bar(ax=ax, title='Frecuencia relativa')
)

cumulative = np.cumsum(pd.Series(samples))
# Creamos grafico de frecuencias acumuladas
plt.plot(bins[1:], cumulative, c='blue')
plt.show()

plt.plot(bins[1:], samples, c='green')
plt.show()

medidas_tendencia_central = {}
medidas_tendencia_central['Media'] = df[df.columns[0]].mean()
medidas_tendencia_central['Mediana'] = df[df.columns[0]].median()
medidas_tendencia_central['Moda'] = list(df[df.columns[0]].mode())
medidas_tendencia_central['Porcentaje de autos que realizan la VTV con menos de 70mil Km'] = 21.21159

medidas_tendencia_central

medidas_dispersion = {}
medidas_dispersion['Varianza'] = df[df.columns[0]].var()
medidas_dispersion['Desvio estándar'] = df[df.columns[0]].std()
medidas_dispersion['Cuartil 1'] = df[df.columns[0]].quantile(0.25)
medidas_dispersion['Cuartil 3'] = df[df.columns[0]].quantile(0.75)
medidas_dispersion['Rango intercuartilico'] = df[df.columns[0]].quantile(0.75) - df[df.columns[0]].quantile(0.25)
medidas_dispersion['Coeficiente de variación'] = (df[df.columns[0]].std() / df[df.columns[0]].mean()) * 100
medidas_dispersion['Coeficiente de asimetría de Pearson'] = df[df.columns[0]].skew()
medidas_dispersion['P30'] = 71000 + ((((30 * 212992) / 100) - 48157) / 23990) * 8000

medidas_dispersion

df.boxplot(column=[df.columns[0]])