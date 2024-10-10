import numpy as np
import matplotlib.pyplot as plt

def f(c):   #Función que retorna la cantidad de pasos que toma para un complejo diverger, recordemos que cualquier complejo con modulo mayor a 2 diverge, asi que
  z=0       #nos limitamos a esos
  for i in range (1000):
    z=z**2+c
    if abs(z) > 2:
      return i
  return -100

nframes=800 #Tamaño de particiones de los ejes
listax=np.linspace(-2,2.0,nframes)  #Ejes a graficar
listay=np.linspace(-2,2.0,nframes)

a=np.zeros((nframes,nframes))  #Cuadrilla compuesta por los ejes

for i in range(nframes):  #Bucle que aplica la función que retorna la cantidad de pasos para todo el espacio 
  for q in range(nframes):
    z=listax[i]+listay[q]*1j  #Espacio de numeros complejos
    a[q,i]=f(z)   #Almacena el numero de pasos que toma para diverger en una matriz del mismo tamaño que el espacio
    #print(a)

plt.imshow(a, cmap='hot')  #Visualización de la matriz con un mapa de densidades
plt.axis('off')
plt.title("Set de Mandelbrot")
plt.show()