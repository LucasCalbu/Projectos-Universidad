import numpy as np
import matplotlib.pyplot as plt

#Función que define el método de Runge-Kutta, para derivadas sin dependencia temporal explícita.
def step(funcion, x , h):
  R1 = funcion(x)
  R2 = funcion(x + h * R1/2)  #t + h/2 )
  R3 = funcion(x + h *R2/2)   #t + h/2)
  R4 = funcion(x + h*R3)  #t + h)

  return x + (h/6)*(R1+2*R2+2*R3+R4) 

#Definimos la función que entrega las derivadas, con x = x[0], y = x[1], z = x[2]
def funcion(x):
  der = np.zeros_like(x)
  
  der[0] = sigma * ( x[1] - x[0] )
  der[1] = r*x[0] - x[1] - x[0]*x[2]
  der[2] = x[0]*x[1] - b*x[2]

  return der

#Constantes de las ecuaciones
sigma = 10  #Con este valor es posible visualizar el atractor, al contrario que con sigma = 109
r = 28
b = 8/3

nframes = 5000 #Como hacemos una iteración cada 0.01 unidades de tiempo, necesitamos 5000 iteraciones para visualizar 50 unidades de tiempo
sol  = np.zeros((nframes,3)) #Este arreglo almacena los resultados, con 3 columnas para x, y, z respectivamente
sol[0,:] = [0,1,0] #Definimos las condiciones iniciales
h = 0.01 #Paso de tiempo hasta la siguiente iteración
t = 0 
ts = [] #Creamos una lista vacia "ts" que almacena cada intervalo de tiempo en una lista para graficar respecto al tiempo

for i in range(1,nframes):
  
  sol[i,:] = step(funcion, sol[i-1,:], h) #Esto define la siguiente fila de los resultados como la fila anterior, luego de haberle aplicado la función "step"
  t = t+h
  ts.append(t) #Esto simplemente crea una lista con los intervalos de tiempo

#plt.plot(ts , sol[:-1,1],color='red')  #y en función de t, Figura 4
plt.plot(sol[:,0],sol[:,2],color='k')  #z en función de x Figura 5 si sigma = 109, Figura 6 si sigma = 10


#ax = plt.figure().add_subplot(projection='3d') 
#ax.plot(sol[:,0],sol[:,1],sol[:,2])  #Proyección en 3d
plt.title("Atractor de Lorenz")
plt.show()