import numpy as np
import matplotlib.pyplot as plt

#Función que define el método Runge-Kutta.
def step(funcion, x , h , t):
  K1 = funcion(x, t)
  K2 = funcion(x + h * K1/2 , t + h/2 )
  K3 = funcion(x + h *K2/2,  t + h/2)
  K4 = funcion(x + h*K3 , t + h)
  return x + (h/6)*(K1+2*K2+2*K3+K4) 

#Definimos la función que entrega las derivadas, con dx/dt = y[0] y dv/dt = y[1]
def funcion(x,t):
  y = np.zeros_like(x)
  y[0] = x[1] 
  y[1] = -omega**2*x[0] - 2*gamma*x[1] + f0*np.cos(omega2 * t)       #Función de oscilador forzado
  return y

#Constantes
omega = 1
gamma = 0.05
f0 = 1
omega2 = 1.5

nframes = 1000 #Como hacemos una iteración cada 0.1 unidades de tiempo, debemos realizar 1000 iteraciones para observar 100 unidades de tiempo
sol  = np.zeros((nframes,2)) #Creamos un arreglo para almacenar los resultados, siendo las columnas 0 y 1 los valores "x" y "x'" respectivamente
sol[0,:] = [1,0] #Definimos las condiciones iniciales 
t = 0 
h = 0.1 #Paso de tiempo hasta la siguiente iteración
ts = [] #Lista vacia "ts" dobnde almacenaremos cada instante de tiempo en una lista para graficar posteriormente

for i in range(1,nframes):
  sol[i,:] = step(funcion, sol[i-1,:], h, t) #Definimos la fila de los resultados como la fila anterior, pero luego de haber aplicado la función "step"
  t = t+h
  ts.append(t) #Al mismo tiempo que almacenamos los resultados, se guarda su correspondiente instante de tiempo en la lista "ts"

#Graficamos la posición(primera columna del arreglo sol), respecto al tiempo
plt.plot(ts,sol[:-1,0],color='k') 
plt.xlabel("Tiempo")
plt.ylabel("Posición")
plt.title("Oscilador Armónico Forzado")
plt.legend()
plt.show()
