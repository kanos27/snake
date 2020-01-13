from random import randint



class Case():
	#initiation de ce qu'est une case du jeu
    def __init__(self, valeur):
        self.valeur = valeur
        # chaque case possède une valeur, lui permattant de définir son contenu

    def __str__(self):
    	#ressort la valeur de la case
        return "[" + str(self.valeur) + "]"

    def getVal(self):
        return self.valeur

    def reloadCase(self):
    	if self.valeur > 0 :
    		self.valeur = self.valeur - 1

class Ligne:
	#initiation d'une ligne du jeu
    def __init__(self, taille = 10):
    	#la taille de la ligne est changeable
        self.taille = taille
        self.ligneCase = []
        for i in range(taille):
        	#rempli la ligne du nombre de cases nécéssaires
            self.ligneCase.append(Case(1))

    def __str__(self):
    	#ressort le contenu de la ligne
        resultat = ""
        for elem in self.ligneCase :
            resultat = resultat + str(elem) + ","
        return resultat

    def reloadLigne(self):
        for obj in self.ligneCase :
            obj.reloadCase()

    def snakeMoveLigne(self, xtete, valQueue):
        self.ligneCase[xtete].valeur = valQueue 


class Grille():
	#initiation de la grille de jeu à trevers une colonne
    def __init__(self,taille=10):
    	#la taille de la colonne et ainsi de la ligne est cheangeable
        self.taille = taille
        self.ColoneCase = []
        for i in range(taille):
        	#remplis la colonne de ligne
            self.ColoneCase.append(Ligne(taille))
            #la ligne aussi longue que la colonne

    def __str__(self):
    	#ressort l'interieur de la grille
        resultat = "interieur de la grille :\n"
        for elem in self.ColoneCase:
            resultat = resultat + str(elem) + "\n"
        return resultat


    def reloadGrille(self):
        for obj in self.ColoneCase :
            obj.reloadLigne()

    def snakeMoveGrille(self,xtete,ytete,valQueue):
        self.ColoneCase[ytete].snakeMoveLigne(xtete,valQueue)


class Snake():
	#initiation du serpent et des coordonnées de sa tete
    def __init__(self, xtete = 0,ytete = 0, valQueue = 1):
        self.xtete = xtete
        self.ytete = ytete
        self.valQueue = valQueue
        #permet de savoir la taille de la queue du serpent

    def __str__(self):
    	#ressort les coordonées et la taille du serpent
        reslutat = "pos : [" + self.xtete + "," + self.ytete + "] taille :" + self.valQueue
        return reslutat


class Pomme():
	#initialisation de la pomme et de ses coordonées
    def __init__(self, Xpomme, Ypomme) :
        self.Xpomme = Xpomme
        self.Ypomme = Ypomme

    def __str__(self):
    	#ressort les coordonnées de la pomme
        resultat = "[" + self.Xpomme + "," + self.Ypomme + "]"
        return resultat


class Jeu():
	#mise en place du jeu, qui gerera le déroulement de la partie
    def __init__(self,taille=10):
        self.taille = taille
        self.grille = Grille(taille)
        self.snake = Snake()
        #self.grille.append(Grille(taille))

    def __str__(self):
    	#ressort la situation de la grille
        resultat = "" + str(self.grille)
        return resultat

    def reload(self):
        self.grille.reloadGrille()

    def snakeMove(self):
        self.grille.snakeMoveGrille(self.snake.xtete,self.snake.ytete,self.snake.valQueue)



def main():
    jeu = Jeu(5)
    print(jeu)
    jeu.reload()
    print(jeu)
    jeu.snakeMove()
    print(jeu)


if __name__ == "__main__" :
    main()