from tkinter import *
from tkinter import ttk

# Windows For label Insert
wfli = Tk()

frame = ttk.Frame(wfli, padding=30)

frame.grid()

ttk.Label(frame, text="Nom de la mission", justify="center").grid(column=0, row=0)
ttk.Entry(frame, justify='left').grid(column=0, row=1)

ttk.Label(frame, text="Description", justify="center").grid(column=0, row=2)
ttk.Entry(frame, justify='left', show="hey").grid(column=0, row=3)

ttk.Label
# Essayer de trouver le parametre d'un champ dans une frame 

# ttk.Button(frame, text="Ok").grid(column=1, row=1)

frame.mainloop()
