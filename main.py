from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFrame, QGridLayout

calcul = resultat = "" 

symbols = ["⌫","AC","=","+",
           "7","8","9","-",
           "4","5","6","*",
           "1","2","3","/",
           ".","0","**","%",
           "(",")","┤"]


#A chaque saisie de l'utilisateur, la valeur est ajoutée à la fin du string calcul.
#Si l'utilisateur saisi un caractère particulier (= ; ┤ ; AC ; ⌫), le programme agira différement. 

def addToCalcul(value):
    global calcul, resultat
    if value == "=":
        #Affichage de la division euclidienne
        if "┤" in calcul:       
            operateur = calcul.index("┤")
            div_euclide = [int(eval(calcul[:operateur])),int(eval(calcul[operateur+1:]))]
            div_euclide.append(div_euclide[0] // div_euclide[1])
            div_euclide.append(div_euclide[0] % div_euclide[1])

            div_euclide.append(calcul)
            div_euclide.append(f"{div_euclide[0]} = {div_euclide[1]} * {div_euclide[2]} + {div_euclide[3]}")

            quotient = f"Quotient : {div_euclide[2]}"
            reste = f"Reste : {div_euclide[3]}"
            resultat = f"{div_euclide[4]}"+"\n"+f"{div_euclide[5]}\n"+quotient+"     ;     "+ reste
            window.label_render_text.setText(resultat)
        else :
            #Tentative de calcul et affichage du résultat ou des erreurs
            try:    
                resultat = str(eval(calcul))
            except ZeroDivisionError :
                resultat = "Error : Divide by 0"
            except Exception:
                resultat = "Error "
            print(f"{calcul} = {resultat}")
            window.label_render_text.setText(f"{calcul} \n = {resultat}")
        calcul = ""
    
    # AC : Supprimer le calcul
    elif value == "AC":
        calcul = ""
        window.label_render_text.setText(f" \n")
        print("AC")
    
    # ⌫ : Supprimer le dernier caractère du calcul
    elif value == "⌫":
        calcul = calcul[:-1]
        window.label_render_text.setText(calcul +  "\n" )
        print(f"{calcul}⌫")
    
    #On ajoute le caractère à la fin du calcul
    else : 
        calcul += str(value)
        window.label_render_text.setText(calcul +  "\n" )
        print(f"{calcul}")


class Calculatrice(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculatrice PyQt6')
        # self.setWindowIcon(QIcon('app-icon.png'))
        self.setFixedSize(400, 325)

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label_render_text = QLabel("\n")
        self.label_render_text.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Raised)
        self.label_render_text.setFixedHeight(60)
        layout.addWidget(self.label_render_text)
        
        grid = QGridLayout()
        layout.addLayout(grid)

        cols = 4
        #Affichage des boutons 
        for index, symbol in enumerate(symbols):
            button = QPushButton(symbol)
        
            button.clicked.connect(lambda _, s=symbol: addToCalcul(s))
            row = index // cols
            col = index % cols
            grid.addWidget(button, row, col)

app = QApplication([])
window = Calculatrice()
window.show()
app.exec()
