import numpy as np

#Inicializamos las variables
Theta = 0
W = []
X = []
m = 0
b = 0

def setValues(w1, w2, theta):
    global Theta
    global W
    global m
    global b

    #Le damos los valores para W, X y Theta
    Theta = theta
    W = [w1, w2]

    #Calculamos los valores de m y b
    m = -W[0]/W[1]
    b = Theta/W[1]

def setInputs(lines):
    global X
    #Llenamos la matriz X con lo que se tomó del archivo
    for line in lines:
        vector = line.split(' ')
        vector[0] = int(vector[0])
        vector[1] = int(vector[1])
        X.append(vector)

def ActivationFunc():
    global Theta
    global W
    global X
    global m
    global b
    #Generamos el vector F(u) con true y false
    F_u = np.dot(X,W)-Theta >= 0
    #Retornamos f(u), los valores de X, m y b
    return F_u, X, m, b
    