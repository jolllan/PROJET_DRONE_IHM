from tkinter import *
from tkinter import ttk

primary = Tk()

frm = ttk.Frame(primary,padding=25)

frm.grid()


ttk.Label(frm, text="Bonjour, Que voulez vous faire aujourd'hui ?", justify=CENTER).grid(column=2, row=0)


ttk.Button(frm, text="Voir le trajet en cours", command=primary.children).grid(column=0, row=2)
ttk.Button(frm, text="Programmation d'un trajet", command=primary.destroy).grid(column=2, row=2)
ttk.Button(frm, text="Voir un ancien trajet", command=primary.destroy).grid(column=3, row=2)
ttk.Button(frm, text="Quitter", command=primary.destroy).grid(column=4, row=3)


primary.mainloop()
