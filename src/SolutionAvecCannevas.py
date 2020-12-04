# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:54:31 2020

@author: alban
"""

## Avec utilisation de cannevas


import tkinter as tk ## on ne travaille pas sur un espace de nom par rapport à from Tkinter import *

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300) ## création cannevas(=rectangle). dans la fenêtre Tkinter
canvas1.pack()

## Entry est une méthode de la classe tk qui va créer une variable dans l'instance mère de type Tb

resultatTb = tk.Entry (root) ## méthode Entry: utilisation de Textbox Création d'une variable de type Entry
canvas1.create_window(200, 140, window=resultatTb)

def getSquareRoot ():  
    x1 = resultatTb.get() ##appel de la méthode get() de l'instance resultatTb car resultatTb est de type Entry
    
    label1 = tk.Label(root, text= float(x1)**0.5)
    canvas1.create_window(200, 230, window=label1)
    
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()