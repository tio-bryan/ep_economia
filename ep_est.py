#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/python

import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def microeconomia():
   tkMessageBox.showinfo("Microeconomia", "Microeconomia")

def macroeconomia():
   tkMessageBox.showinfo("Macroeconomia", "Macroeconomia")

B = Tkinter.Button(top, text="Microeconomia", command=microeconomia)
B = Tkinter.Button(top, text="Macroeconomia", command=macroeconomia)

B.pack()
top.mainloop()