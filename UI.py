from xml.dom.expatbuilder import makeBuilder
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import numpy as np
import Perceptron as p

def print_axis():
    global ax
    #Plano cartesiano
    ejeX = np.arange(-2, 3, 1)
    ejeY = np.arange(-2, 3, 1)
    zeros = [0,0,0,0,0]
    ax.plot(ejeX, zeros, 'k')
    ax.plot(zeros, ejeY, 'k')

def update_graphic():
    global w1, w2, theta
    p.setValues(float(w1.get()),float(w2.get()),float(theta.get()))

    F_u, X, m, b = p.ActivationFunc()

    ax.cla()
    print_axis()
    
    for i in range(len(X)):
        if F_u[i]:
            ax.plot(X[i][0],X[i][1],'og')
        else:
            ax.plot(X[i][0],X[i][1],'or')

    #Linea de la pendiente
    x = [X[0][0],X[1][0],X[2][0],X[3][0]]
    ax.plot(x, np.dot(x,m) + b, 'b')
    
    show_graphic()


def show_graphic():
    global mainwindow, w1, w2, theta, fig

    mainwindow.destroy()
    mainwindow = Tk()
    mainwindow.geometry('650x650')
    mainwindow.wm_title('Perceptron')

    w1 = StringVar(mainwindow)
    w2 = StringVar(mainwindow)
    theta = StringVar(mainwindow)
        
    canvas = FigureCanvasTkAgg(fig, master = mainwindow)
    canvas.get_tk_widget().pack(padx=5, pady=5, expand=1, fill='both')

    Label(mainwindow, text='W1', width=7).pack(pady=5, side='left', expand=1)
    Entry(mainwindow, width=15, textvariable=w1).pack(pady=5, side='left', expand=1)

    Label(mainwindow, text='W2', width=7).pack(pady=5, side='left', expand=1)
    Entry(mainwindow, width=15, textvariable=w2).pack(pady=5, side='left', expand=1)

    Label(mainwindow, text='Tetha', width=10).pack(pady=5, side='left', expand=1)
    Entry(mainwindow, width=15, textvariable=theta).pack(pady=5, side='left', expand=1)

    Button(mainwindow, text='Go!', width=10, command=update_graphic).pack(pady=5, side='left', expand=1)

    mainwindow.mainloop()


fig, ax= plt.subplots(facecolor='#8D96DA')

#Abrimos el archivo de texto para tomar los inputs
with open('inputs.txt') as f:
    lines = f.readlines()
p.setInputs(lines)

mainwindow = Tk()
w1 = w2 = theta = 0.0
print_axis()
show_graphic()