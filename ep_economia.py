#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ativa o virtualenv para não precisar instalar os packages
activate_this = "./bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

from Tkinter import * # Lib p/ criar janelas
from classes.microeconomia import microeconomia
from classes.macroeconomia import macroeconomia
import matplotlib # Lib p/ plotar graficos

root = Tk() # Cria menu principal
root.title('EP de Estatística')
root.geometry('250x250')

# Cria botões
microeconomia = Button(root, text='Microeconomia', command=microeconomia).pack()
macroeconomia = Button(root, text='Macroeconomia', command=macroeconomia).pack()
Button(root, text='Sair', fg='red', command=quit).pack()

root.mainloop()