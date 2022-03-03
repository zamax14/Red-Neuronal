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
    X.append((ix, iy))
    if good_or_bad:
        d.append(1)
        ax.plot(ix,iy, '.g')
    else:
        if func_value.get() == 0:
            d.append(0)
        else:
            d.append(-1)
        ax.plot(ix,iy, '.r')
    canvas.draw()

def print_axis():
    global ax
    #Imprimimos los ejes del plano cartesiano
    ejeX = [-5,5]
    ejeY = [-5,5]
    zeros = [0,0]
    ax.plot(ejeX, zeros, 'k')
    ax.plot(zeros, ejeY, 'k')
    plt.xlim(-1,1)
    plt.ylim(-1,1)

def ActivationFunc(X):
    global w1, w2, theta, func_value, a

    v = np.dot(X,[w1,w2])-theta

    if func_value.get() == 0:
        #Sigmoidal
        F_u = 1/(1+np.exp(-(float(a.get()))*v))

    elif func_value.get() == 1:
        #Tangente hiperbolica
        F_u = np.tanh(v)
    
    elif func_value.get() == 2:
        #Lineal
        F_u = float(a.get())*v

    return F_u

def ActivationFuncDerivated(Y):
    global func_value, a

    if func_value.get() == 0:
        #Sigmoidal
        F_u = float(a.get())*Y*(1-Y)

    elif func_value.get() == 1:
        #Tangente hiperbolica
        F_u = 1-(Y**2)
    
    elif func_value.get() == 2:
        #Lineal
        F_u = float(a.get())

    return F_u

def print_line():
    global w1, w2, theta, eta, X, d, a, func_value, min_error

    e = [1]

    diff_color = 0

    if func_value.get() == 0:
        diff_color = 0.5
    
    while np.average(np.power(e,2)) > float(min_error.get()):
        e = []
        for i in range(len(X)):
            Y = ActivationFunc(X[i])
            e.append(d[i]-Y)
            y_prima = ActivationFuncDerivated(Y)
            w1 = w1 + (float(eta.get())*e[-1]*y_prima*X[i][0])
            w2 = w2 + (float(eta.get())*e[-1]*y_prima*X[i][1])
            theta = theta - (float(eta.get())*e[-1]*y_prima)

        ax.cla()

        Y=[]
        m=-w1/w2
        b=theta/w2
        Y = ActivationFunc(X)
        #Imprimimos los puntos en la grafica
        for i in range(len(X)):
            if Y[i]>=diff_color:
                ax.plot(X[i][0],X[i][1],'.g')
            else:
                ax.plot(X[i][0],X[i][1],'.r')

        #Coloca una linea a partir de un punto dado y la pendiente
        plt.axline((X[0][0], (X[0][0]*m)+b), slope=m, color='b')
        print_axis()

        W1_label.config(text="W1: {:.4f}".format(w1))
        W2_label.config(text="W2: {:.4f}".format(w2))
        Theta_label.config(text="Theta: {:.4f}".format(theta))
        error_average_label.config(text="E.av: {:.5f}".format(np.average(np.power(e,2))))

        canvas.draw()

def clean_screen():
    global X, d
    X = []
    d = []
    ax.cla()
    print_axis()
    canvas.draw()
    w1 = random.random()
    w2 = random.random()
    theta = random.random()
    W1_label.config(text="W1: {:.4f}".format(w1))
    W2_label.config(text="W2: {:.4f}".format(w2))
    Theta_label.config(text="Theta: {:.4f}".format(theta))
    error_average_label.config(text="E.av: ")

    

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
a = StringVar(mainwindow, 0)
min_error = StringVar(mainwindow, 0)
func_value = IntVar(mainwindow, 0)

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

error_average_label = Label(mainwindow, text = "E.av: ")
error_average_label.place(x=600, y=110)

Eta_label = Label(mainwindow, text = "Eta: ")
Eta_label.place(x=600, y=140)

Eta_entry = Entry(mainwindow, textvariable=eta)
Eta_entry.place(x=600, y=160) 

a_label = Label(mainwindow, text = "A: ")
a_label.place(x=600, y=190)

a_entry = Entry(mainwindow, textvariable=a)
a_entry.place(x=600, y=210)

error_label = Label(mainwindow, text = "Min. Error: ")
error_label.place(x=600, y=240)

error_entry = Entry(mainwindow, textvariable=min_error)
error_entry.place(x=600, y=260)


start_button = Button(mainwindow, text="Go!", command=lambda:threading.Thread(target=print_line).start())
start_button.place(x=600, y=290)

start_button = Button(mainwindow, text="Clean", command=clean_screen)
start_button.place(x=600, y=320)

red_green_button = Button(mainwindow, text="Good", background="#2CA711", width=10, command=change_color)
red_green_button.place(x=600, y=350)

sigmoidal_rb = Radiobutton(mainwindow, text="Sigmoidal", variable=func_value, value=0)
sigmoidal_rb.place(x=600, y=380)

tangente_rb = Radiobutton(mainwindow, text="Tangente", variable=func_value, value=1)
tangente_rb.place(x=600, y=400)

Lineal_rb = Radiobutton(mainwindow, text="Lineal", variable=func_value, value=2)
Lineal_rb.place(x=600, y=420)

#Mostramos la interfaz
mainwindow.mainloop()
