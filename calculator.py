# importe le module tkinter
from tkinter import *

# config de l'interface
    # la variable window appelle l'interface
window = Tk()

    # titre de l'interface
window.title("Calculatrice")

    #icone de l'interface
window.iconbitmap("icone.ico")

    #couleur de l'interface
window.config(bg = "#808080")

# résultat des calculs
result = Label(window, text=0)

class Calculator:
    # exécuté à la création de l'objet
    def __init__(self):
        self.result = 0
        self.values = []
        
# Ajout des chiffres

    # ajoute 0 aux valeurs utilisées pours les calculs    
    def add_0(self):
        # ajoute 0 comme nouvel élément du tableau
        self.values.append(0)

    # ajoute 1 aux valeurs utilisles pours les calculs
    def add_1(self):
        self.values.append(1)
    
    # ajoute 2, ...
    def add_2(self):
        self.values.append(2)

    def add_3(self):
        self.values.append(3)

    def add_4(self):
        self.values.append(4)

    def add_5(self):
        self.values.append(5)
        
    def add_6(self):
        self.values.append(6)
        
    def add_7(self):
        self.values.append(7)
    
    def add_8(self):
        self.values.append(8)

    def add_9(self):
        self.values.append(9)

# les opérations : addition, soustraction, division et multiplication

    def do_plus(self):
        for i in range(len(self.values)):
            # additione les valeurs du tableau
            self.result = self.result + self.values[i]
            # fin de la phase de calcul
            if i + 1 == len(self.values):
                # la première valeure du tableau devient le résultat de l'opération
                self.values[0] = self.result
                # supprime le reste de la liste à part la position 0
                del self.values[1:len(self.values)]

    def do_minus(self):
        for i in range(len(self.values)):
            # soustraient les valeurs du tableau
            self.result = self.result - self.values[i]
            if i + 1 == len(self.values):
                self.values[0] = self.result
                del self.values[1:len(self.values)]

    def do_divide(self):
        for i in range(len(self.values)):
            # définition de résultat pour la division
            if i == 0:
                self.result = self.values[i]
            else:
                # divise le résultat par la prochaine valeurs du tableau
                self.result = self.result / self.values[i]
            # fin de l'opération, même chose que l'addition
            if i + 1 == len(self.values):
                self.values[0] = self.result
                del self.values[1:len(self.values)]
        
    def do_multiple(self):
        for i in range(len(self.values)):
            if i == 0:
                self.result = self.values[i]
            else:
                # multiplie les valeurs
                self.result = self.result / self.values[i]
            if i + 1 == len(self.values):
                self.values[0] = self.result
                del self.values[1:len(self.values)]

    def do_egal(self):
        # f sting qui affiche le résultat
        print(f'The result of your operation is {self.result}')


# définir l'objet
calc = Calculator()

# taille de la fenêtre
window.geometry("300x400")

# label, applique du texte dans la fenêtre
label = Label(window, text="The Calculator", fg='blue', bg='white')

# place le "label" en haut de base "grid" permet de generer une grille ex: pour palcer les bouton ensuite
label.grid()

# les boutons de calculette, appelé en fonction de leur position dans la  grille.

# affichage 


# bouton pour la ligne 1
button_divide = Button(window, text = "/",width=6, height=2, fg='white', bg='blue', command=calc.add_7)
button_divide.grid(row=2, column=4) # place le bouton dans une grille, ligne 1 et colonne 1.

# bouton pour la ligne 2
# bouton 1 qui appelle la fonciton calc.add_1. fg = forground, bg = background, commande = action au moment du clique 
button_7 = Button(window, text = "7",width=6, height=2, fg='white', bg='blue', command=calc.add_7)
button_7.grid(row=3, column=1) # place le bouton dans une grille, ligne 1 et colonne 1.

button_8 = Button(window, text = "8",width=6, height=2, fg='white', bg='blue', command=calc.add_8)
button_8.grid(row=3, column=2)

button_9 = Button(window, text = "9",width=6, height=2, fg='white', bg='blue', command=calc.add_9)
button_9.grid(row=3, column=3)

button_multiply = Button(window, text = "x",width=6, height=2, fg='white', bg='blue', command=calc.add_9)
button_multiply.grid(row=3, column=4)

# bouton pour la ligne 3
button_4 = Button(window, text = "4",width=6, height=2, fg='white', bg='blue', command=calc.add_4)
button_4.grid(row=4, column=1)

button_5 = Button(window, text = "5",width=6, height=2, fg='white', bg='blue', command=calc.add_5)
button_5.grid(row=4, column=2)

button_6 = Button(window, text = "6",width=6, height=2, fg='white', bg='blue', command=calc.add_6)
button_6.grid(row=4, column=3)

button_minus = Button(window, text = "-",width=6, height=2, fg='white', bg='blue', command=calc.do_minus)
button_minus.grid(row=4, column=4)

# bouton pour la ligne 4
button_1 = Button(window, text = "1",width=6, height=2, fg='white', bg='blue', command=calc.add_1)
button_1.grid(row=5, column=1)
 
button_2 = Button(window, text = "2",width=6, height=2, fg='white', bg='blue', command=calc.add_2)
button_2.grid(row=5, column=2)

button_3 = Button(window, text = "3",width=6, height=2, fg='white', bg='blue', command=calc.add_3)
button_3.grid(row=5, column=3)

button_plus = Button(window, text = "+",width=6, height=2, fg='white', bg='blue', command=calc.do_plus)
button_plus.grid(row=5, column=4)

# bouton pour la ligne 5
button_0 = Button(window, text = "0",width=6, height=2, fg='white', bg='blue', command=calc.add_0)
button_0.grid(row=6, column=2)

button_point = Button(window, text = ".",width=6, height=2, fg='white', bg='blue', command=calc.add_0)
button_point.grid(row=6, column=3)

button_egal = Button(window, text = "=",width=6, height=2, fg='white', bg='blue', command=calc.do_egal)
button_egal.grid(row=6, column=4)


# appelle la fenêtre
window.mainloop()

