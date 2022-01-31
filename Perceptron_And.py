import numpy as np
import matplotlib.pyplot as plt

#Abrimos el archivo de texto para tomar los inputs
with open('inputs.txt') as f:
    lines = f.readlines()

#Inicializamos los valores para W, X y Theta
Theta = 1.5
W = [1,1]
X = []
#Llenamos la matriz X con lo que se tomó del archivo
for line in lines:
    vector = line.rstrip("\n").split(' ')
    vector[0] = int(vector[0])
    vector[1] = int(vector[1])
    X.append(vector)

#Valores de la pendiente
m = -W[0]/W[1]
b = Theta/W[1]

#Plano cartesiano
ejeX = np.arange(-2, 3, 1)
ejeY = np.arange(-2, 3, 1)
zeros = [0,0,0,0,0]
plt.plot(ejeX, zeros, 'k')
plt.plot(zeros, ejeY, 'k')

#Hardcode
plt.plot(X[0][0],X[0][1],'or')
plt.plot(X[1][0],X[1][1],'or')
plt.plot(X[2][0],X[2][1],'or')
plt.plot(X[3][0],X[3][1],'og')

#Linea de la pendiente
x = [X[0][0],X[1][0],X[2][0],X[3][0]]
plt.plot(x, np.dot(x,m) + b, 'b')

#Imprimir la grafica
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Perceptron')
plt.show()
