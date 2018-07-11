#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import * # Lib p/ criar janelas

# Ativa o virtualenv para não precisar instalar os packages abaixo
activate_this = "./bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

import matplotlib # Lib p/ plotar gráficos
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

LARGE_FONT = ('VErdana', 12)

class epDeEconomia(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # Tk.iconbitmap(self, defaault='clienticon.ico')
        Tk.wm_title(self, 'EP de Economia')

        container = Frame(self)
        container.pack(side='top', fill='both', expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Microeconomia, pibPelaFormula, Macroeconomia):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text='Start Page', font=LARGE_FONT).pack(pady=10, padx=10)

        Button(self, text='Microeconomia', command=lambda: controller.show_frame(Microeconomia)).pack()
        Button(self, text='Macroeconomia', command=lambda: controller.show_frame(Macroeconomia)).pack()
        Button(self, text='Sair', fg='red', command=quit).pack()

class Microeconomia(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text='Microeconomia', font=LARGE_FONT).pack(pady=10, padx=10)

        Button(self, text='Voltar', command=lambda: controller.show_frame(StartPage)).pack()
















class Macroeconomia(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text='Macroeconomia', font=LARGE_FONT).pack(pady=10, padx=10)

        Button(self, text='PIB Pela Fórmula', command=lambda: controller.show_frame(pibPelaFormula)).pack()
        Button(self, text='PIB Pela Tabela', command=lambda: controller.show_frame(pibPelaFormula)).pack()

        Button(self, text='Voltar', command=lambda: controller.show_frame(StartPage)).pack()

class pibPelaFormula(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text='PIB Pela Fórmula', font=LARGE_FONT).pack(pady=10, padx=10)

        # f = Figure(figsize=(5,5), dpi=100)
        # a = f.add_subplot(111)
        # a.plot([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5])

        # canvas = FigureCanvasTkAgg(f, self)
        # canvas.show()
        # canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        self.c = DoubleVar()
        self.inv = DoubleVar()
        self.g = DoubleVar()
        self.e = DoubleVar()
        self.imp = DoubleVar()

        Label(self, text='Consumo Privado').pack()
        Entry(self, textvariable=self.c).pack()

        Label(self, text='Investimentos').pack()
        Entry(self, textvariable=self.inv).pack()

        Label(self, text='Gastos do Governo').pack()
        Entry(self, textvariable=self.g).pack()

        Label(self, text='Volume de Exportações').pack()
        Entry(self, textvariable=self.e).pack()

        Label(self, text='Volume de Importações').pack()
        Entry(self, textvariable=self.imp).pack()

        Button(self, text='Calcular', command=lambda: self.calcula_pib(self.c, self.inv, self.g, self.e, self.imp)).pack()
        Button(self, text='Voltar', command=lambda: controller.show_frame(Macroeconomia)).pack()

    def calcula_pib(self, c, inv, g, e, imp):
        try:
            print float(c.get()) + float(inv.get()) + float(g.get()) + (float(e.get()) - float(imp.get()))
        except ValueError:
            pass

app = epDeEconomia()
app.mainloop()