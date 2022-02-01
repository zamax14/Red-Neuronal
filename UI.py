import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import numpy as np
import Perceptron as p

fig, ax= plt.subplots(facecolor='#8D96DA')

#Plano cartesiano
ejeX = np.arange(-2, 3, 1)
ejeY = np.arange(-2, 3, 1)
zeros = [0,0,0,0,0]
ax.plot(ejeX, zeros, 'k')
ax.plot(zeros, ejeY, 'k')

mainwindow = Tk()
mainwindow.geometry('650x650')
mainwindow.wm_title('Perceptron')

frame = Frame(mainwindow, bg='white', bd=3)
frame.pack(expand=1, fill='both')

canvas = FigureCanvasTkAgg(fig, master = frame)
canvas.draw()
canvas.get_tk_widget().pack(padx=5, pady=5, expand=1, fill='both')

mainwindow.mainloop()


#Abrimos el archivo de texto para tomar los inputs
with open('inputs.txt') as f:
    lines = f.readlines()

p.setInputs(lines)

w1 = float(input("W1: "))
w2 = float(input("W2: "))
theta = float(input("Theta: "))

p.setValues(w1,w2,theta)

F_u, X, m, b = p.ActivationFunc()

for i in range(len(X)):
    if F_u[i]:
        plt.plot(X[i][0],X[i][1],'og')
    else:
        plt.plot(X[i][0],X[i][1],'or')

#Linea de la pendiente
x = [X[0][0],X[1][0],X[2][0],X[3][0]]
plt.plot(x, np.dot(x,m) + b, 'b')

#Imprimir la grafica
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Perceptron')
plt.show()