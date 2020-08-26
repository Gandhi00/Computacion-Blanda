#
# Estudiante: Esteban Sanchez Lopez - 1004717342
#

import numpy as np

#leemos los datos del archivo de texto
datos = np.genfromtxt("web_traffic.tsv", delimiter="\t")
#Imprimimos las primeras 10 lineas de todas las columnas
print(datos[:10], '\n')
# Mostramos en numero de datos
print(datos.shape)

#separamos las columnas de los datos en 2 (Horas y numero de intentos)

Time = datos[:,0]
Attemps = datos[:,1]
# Se muestran los valores en x, y
print(Time, '\n')
print(Attemps, '\n')

# Imprimimos las dimensiones de los 2 arreglos nuevos.

print(Time.ndim, '\n')
print(Attemps.ndim, '\n')

# Elementos contenidos en los vectores x, y
print(Time.shape, '\n')
print(Attemps.shape)

# Investigamos el número de valores nan que contiene el vector y

print(np.sum(np.isnan(Attemps)))

# Número de elementos en x, y, antes de ser comprimidos

print(Time.shape, '\n')
print(Attemps.shape, '\n')

# Eliminamos los elementos invalidos (nan) de los arreglos.
Time = Time[~np.isnan(Attemps)]
Attemps = Attemps[~np.isnan(Attemps)]

# Mostramos el numero de elementos de los 2 arreglos.
print(Time.shape, '\n')
print(Attemps.shape, '\n')

# Se importa la librería para graficar
import matplotlib.pyplot as plt

# Dibuja los puntos (x,y) con círculos de tamaño 10
plt.scatter(Time, Attemps, s=10)

# Informacion de la grafica
plt.title("Tráfico Web del ultimo mes")
plt.xlabel("Tiempo (en semanas)")
plt.ylabel("Intentos por Hora")
plt.xticks([w*7*24 for w in range(10)],['semana %i' % w for w in range(10)])
plt.autoscale(tight=True)
# dibuja una cuadrícula punteada con opacidad reducida
plt.grid(True, linestyle='-', color='0.75')
# Muestra el gráfico
plt.show()