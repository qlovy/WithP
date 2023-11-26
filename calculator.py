# importe le module tkinter
from tkinter import *

# la variable window appelle l'interface
window = Tk()

window.geometry("300x400")

# label, définit la fenêtre
label = Label(window, text="The Calculator")

# place le "label"
label.pack()

# les boutons de calculette
button = Button(window, text = "+")
button.pack()


# affiche la fenêtre
window.mainloop()
