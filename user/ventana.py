import tkinter as tk
from tkinter import ttk

ventana=tk.Tk()
ventana.geometry('600x400')
ventana.title("Menu")
boton1 = ttk.Button(ventana,text='enviar')
boton1.grid(column=0,row=0)
ventana.mainloop()