#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/python

from Tkinter import * # Lib p/ criar janelas
import tkMessageBox
import matplotlib # Lib p/ plotar graficos

def microeconomia():
    tkMessageBox.showinfo('Microeconomia', 'Microeconomia')

def macroeconomia():
    tkMessageBox.showinfo('Macroeconomia', 'Macroeconomia')

root = Tk() # Cria menu principal
root.title('EP de Estatística')
root.geometry('250x250')

# Cria botões
microeconomia = Button(root, text='Microeconomia', command=microeconomia).pack()
macroeconomia = Button(root, text='Macroeconomia', command=macroeconomia).pack()
Button(root, text='Sair', fg='red', command=quit).pack()

root.mainloop()