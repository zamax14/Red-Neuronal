import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import numpy as np
import Perceptron as p

def print_axis():
    global ax
    #Imprimimos los ejes del plano cartesiano
    ejeX = [-2,2]
    ejeY = [-2,2]
    zeros = [0,0]
    ax.plot(ejeX, zeros, 'k')
    ax.plot(zeros, ejeY, 'k')

def update_graphic():
    global w1, w2, theta
    #Llamamos a la funcion del perceptron que settea los valores de los pesos y theta
    p.setValues(float(w1.get()),float(w2.get()),float(theta.get()))

    #Tomamos los valores que retorna el perceptron
    F_u, X, m, b = p.ActivationFunc()

    #Limpiamos todos los puntos y colocamos el plano cartesiano
    ax.cla()
    print_axis()
    
    #Imprimimos los puntos en la grafica
    for i in range(len(X)):
        #Si la funcion f(u) da 1, entonces el punto se imprime de color verde
        #En caso contrario será rojo
        if F_u[i]:
            ax.plot(X[i][0],X[i][1],'og')
        else:
            ax.plot(X[i][0],X[i][1],'or')

    #Linea de la pendiente
    x = [X[0][0],X[1][0],X[2][0],X[3][0]]
    ax.plot(x, np.dot(x,m) + b, 'b')
    
    #Imprimimos la grafica
    show_graphic()


def show_graphic():
    global mainwindow, w1, w2, theta, fig
    #Borramos la ventana anterior y generamos una nueva
    mainwindow.destroy()
    mainwindow = Tk()
    mainwindow.geometry('650x650')
    mainwindow.wm_title('Perceptron')
    #Limpiamos los valores de los pesos y theta
    w1 = StringVar(mainwindow)
    w2 = StringVar(mainwindow)
    theta = StringVar(mainwindow)
    #Colocamos la grafica en la interfaz
    canvas = FigureCanvasTkAgg(fig, master = mainwindow)
    canvas.get_tk_widget().pack(padx=5, pady=5, expand=1, fill='both')

    #Colocamos las etiquetas, cuadros de entrada y boton
    Label(mainwindow, text='W1', width=7).pack(pady=5, side='left', expand=1)
    Entry(mainwindow, width=15, textvariable=w1).pack(pady=5, side='left', expand=1)

    Label(mainwindow, text='W2', width=7).pack(pady=5, side='left', expand=1)
    Entry(mainwindow, width=15, textvariable=w2).pack(pady=5, side='left', expand=1)

    Label(mainwindow, text='Theta', width=10).pack(pady=5, side='left', expand=1)
    Entry(mainwindow, width=15, textvariable=theta).pack(pady=5, side='left', expand=1)

    Button(mainwindow, text='Go!', width=10, command=update_graphic).pack(pady=5, side='left', expand=1)

    #Mostramos la interfaz
    mainwindow.mainloop()

#Inizializamos la grafica de matplotlib
fig, ax= plt.subplots(facecolor='#8D96DA')

#Abrimos el archivo de texto para tomar los inputs
with open('inputs.txt') as f:
    lines = f.readlines()
p.setInputs(lines)

#Inicializamos la ventana y los valores de los pesos y theta
mainwindow = Tk()
w1 = w2 = theta = 0.0
print_axis()
show_graphic()