import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import numpy as np
import threading

X = []
d = []
good_or_bad = True

def change_color():
    global good_or_bad
    good_or_bad = not(good_or_bad)
    if good_or_bad:
        red_green_button.config(text="Good", background="#2CA711")
    else:
        red_green_button.config(text="Bad", background="#FF0000")

def plot_point(event):
    ix, iy = event.xdata, event.ydata
    if good_or_bad:
        X.append((ix, iy))
        d.append(1)
        ax.plot(ix,iy, '.g')
    else:
        X.append((ix, iy))
        d.append(0)
        ax.plot(ix,iy, '.r')
    canvas.draw()

def print_axis():
    global ax
    #Imprimimos los ejes del plano cartesiano
    ejeX = [-20,20]
    ejeY = [-20,20]
    zeros = [0,0]
    ax.plot(ejeX, zeros, 'k')
    ax.plot(zeros, ejeY, 'k')

def ActivationFunc():
    global w1, w2, theta
    #Generamos el vector F(u) con true y false
    F_u = np.dot(X,[w1,w2])-theta >= 0
    #Retornamos f(u), los valores de X, m y b
    return F_u

def print_line():
    global w1, w2, theta, eta, X

    epoch = 250
    error = True
    while (epoch!=0) and error:
        e = []
        for i in range(len(X)):
            Y = np.dot(X[i],[w1,w2])-theta >= 0
            e.append(d[i]-Y)
            w1 = w1 + (float(eta.get())*e[-1]*X[i][0])
            w2 = w2 + (float(eta.get())*e[-1]*X[i][1])
            theta = theta + (float(eta.get())*e[-1]*1)

        ax.cla()
        print_axis()

        Y=[]
        m=-w1/w2
        b=theta/w2
        Y = ActivationFunc()
        #Imprimimos los puntos en la grafica
        for i in range(len(X)):
            #Si la funcion f(u) da 1, entonces el punto se imprime de color verde
            #En caso contrario será rojo
            if d[i]:
                ax.plot(X[i][0],X[i][1],'.g')
            else:
                ax.plot(X[i][0],X[i][1],'.r')

        #Coloca una linea a partir de un punto dado y la pendiente
        print(X[0][0], m, b)
        plt.axline((X[0][0], (X[0][0]*m)+b), slope=m, color='b')
        canvas.draw()
        W1_label.config(text="W1: {:.4f}".format(w1))
        W2_label.config(text="W2: {:.4f}".format(w2))
        Theta_label.config(text="Theta: {:.4f}".format(theta))

        if not(1 in e) and not(-1 in e):
            error = False
            
        epoch-=1

def clean_screen():
    global X
    ax.cla()
    print_axis()
    canvas.draw()
    X = []
    

#Inizializamos la grafica de matplotlib
fig, ax= plt.subplots(facecolor='#8D96DA')
fig.canvas.mpl_connect('button_press_event', plot_point)

print_axis()

mainwindow = Tk()
mainwindow.geometry('750x600')
mainwindow.wm_title('Perceptron')
#Creamos los valores de los pesos y humbral de activacion 
w1 = random.random()
w2 = random.random()
theta = random.random()
eta = StringVar(mainwindow, 0)
#Colocamos la grafica en la interfaz
canvas = FigureCanvasTkAgg(fig, master = mainwindow)
canvas.get_tk_widget().place(x=10, y=10, width=580, height=580)

#Colocamos las etiquetas, cuadros de entrada y boton
W1_label = Label(mainwindow, text = "W1: {:.4f}".format(w1))
W1_label.place(x=600, y=20) 

W2_label = Label(mainwindow, text = "W2: {:.4f}".format(w2))
W2_label.place(x=600, y=50) 

Theta_label = Label(mainwindow, text = "Theta: {:.4f}".format(theta))
Theta_label.place(x=600, y=80) 

Eta_label = Label(mainwindow, text = "Eta: ")
Eta_label.place(x=600, y=110)

Eta_entry = Entry(mainwindow, textvariable=eta)
Eta_entry.place(x=600, y=130) 

#button
start_button = Button(mainwindow, text="Go!", command=lambda:threading.Thread(target=print_line).start())
start_button.place(x=600, y=230)

start_button = Button(mainwindow, text="Clean", command=clean_screen)
start_button.place(x=600, y=270)

red_green_button = Button(mainwindow, text="Good", background="#2CA711", width=10, command=change_color)
red_green_button.place(x=600, y=300)

#Mostramos la interfaz
mainwindow.mainloop()
