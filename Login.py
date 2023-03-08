from tkinter import *
from tkinter import ttk


class Login:
    #Tipo constructor de la clase.
    def __init__(self, raiz):
        raiz.title("Inicio de Sesion")

        self.Usuario="Ivan"
        self.Contraseña="123"
       
       #Padding(izquierda,arriba,derecha,abajo)
        mainFrame = ttk.Frame(raiz, padding="3 3 12 12")
        mainFrame.grid(column=0, row=0) 
        usuarioEntry=ttk.Entry(mainFrame,width=30,textvariable=self.Usuario)
        usuarioEntry.grid(column=1, row=0)

        ttk.Label(mainFrame,text="Usuario").grid(column=0,row=0)
        usuarioEntry=ttk.Entry(mainFrame, width=30, textvariable=self.Usuario)
        usuarioEntry.grid(column=1, row=3)
        ttk.Label(mainFrame,textvariable=self.Contraseña).grid(column=1,row=1)
        ttk.Label(mainFrame,text="Contraseña").grid(column=0,row=3)
        ttk.Label(mainFrame).grid(column=0,row=4)  
        ttk.Button(mainFrame,text="Ingresar",command=self.Contraseña).grid(column=1,row=5,sticky=(E))       