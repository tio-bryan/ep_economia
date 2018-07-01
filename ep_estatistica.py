#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/python

import Tkinter as tk # Lib p/ criar janelas
import tkMessageBox
import matplotlib # Lib p/ plotar graficos

def microeconomia():
    tkMessageBox.showinfo('Microeconomia', 'Microeconomia')

def macroeconomia():
    tkMessageBox.showinfo('Macroeconomia', 'Macroeconomia')

root = tk.Tk() # Cria menu principal
root.title('EP de Estatística')

# Cria botões
microeconomia = tk.Button(root, text='Microeconomia', command=microeconomia)
macroeconomia = tk.Button(root, text='Macroeconomia', command=macroeconomia)
quit = tk.Button(root, text='Sair', fg='red', command=quit)

microeconomia.pack()
macroeconomia.pack()
quit.pack()

root.mainloop()