import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import Perceptron as p

X = []

def plot_point(event):
    ix, iy = event.xdata, event.ydata
    X.append((ix, iy))
    ax.plot(ix,iy, '.m')
    canvas.draw()

def print_axis():
    global ax
    #Imprimimos los ejes del plano cartesiano
    ejeX = [-20,20]
    ejeY = [-20,20]
    zeros = [0,0]
    ax.plot(ejeX, zeros, 'k')
    ax.plot(zeros, ejeY, 'k')

def print_line():
    global w1, w2, theta
    #Llamamos a la funcion del perceptron que settea los valores de los pesos y theta
    p.setValues(float(w1.get()),float(w2.get()),float(theta.get()))

    #Tomamos los valores que retorna el perceptron
    F_u, m, b = p.ActivationFunc(X)

    #Limpiamos todos los puntos y colocamos el plano cartesiano
    ax.cla()
    print_axis()
    
    #Imprimimos los puntos en la grafica
    for i in range(len(X)):
        #Si la funcion f(u) da 1, entonces el punto se imprime de color verde
        #En caso contrario será rojo
        if F_u[i]:
            ax.plot(X[i][0],X[i][1],'.g')
        else:
            ax.plot(X[i][0],X[i][1],'.r')

    #Coloca una linea a partir de un punto dado y la pendiente
    plt.axline((X[0][0], (X[0][0]*m)+b), slope=m, color='b')
    canvas.draw()
    

#Inizializamos la grafica de matplotlib
fig, ax= plt.subplots(facecolor='#8D96DA')
fig.canvas.mpl_connect('button_press_event', plot_point)

#Inicializamos la ventana y los valores de los pesos y theta
w1 = w2 = theta = 0.0
print_axis()

mainwindow = Tk()
mainwindow.geometry('650x650')
mainwindow.wm_title('Perceptron')
#Limpiamos los valores de los pesos y theta
w1 = StringVar(mainwindow, 0)
w2 = StringVar(mainwindow, 0)
theta = StringVar(mainwindow, 0)
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

Button(mainwindow, text='Go!', width=10, command=print_line).pack(pady=5, side='left', expand=1)

#Mostramos la interfaz
mainwindow.mainloop()
