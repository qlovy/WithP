# importe le module tkinter
from tkinter import *

def click():
    label.configure(text='ça fait plus')


# la variable window appelle l'interface
window = Tk()

window.geometry("300x400")

# label, applique du texte dans la fenêtre
label = Label(window, text="The Calculator", fg='blue', bg='white')

# place le "label" en haut de base
label.pack()

# les boutons de calculette
button = Button(window, text = "+", fg='white', bg='blue', command=click)
button.pack(side='right')


# affiche la fenêtre
window.mainloop()




#Moi