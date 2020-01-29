from random import randint



class Case():
	"""admet une case possedant une valeur dans une grille"""
    def __init__(self, valeur):
        """initialise la valeur de la case, soit son contenu"""
        self.valeur = valeur
        # chaque case possède une valeur, lui permattant de définir son contenu

    def __str__(self):
    	"""retourne le contenu de la case sous forme texte"""
        return "[" + str(self.valeur) + "]"

    def getVal(self):
        """retourne la valeur de la case"""
        return self.valeur

    def reloadCase(self):
        """diminue la valeur de la case de 1 si supérieure à 0"""
    	if self.valeur > 0 :
    		self.valeur = self.valeur - 1


class Ligne:
	"""initiatie une ligne du jeu, composée de cases"""
    def __init__(self, taille = 10):
    	"""la taille de la ligne est changeable en fonction de la valeure entrée"""
        self.taille = taille
        self.ligneCase = []
        for i in range(taille):
        	#rempli la ligne du nombre de cases nécéssaires
            self.ligneCase.append(Case(1))

    def __str__(self):
    	"""retourne le contenu de la ligne sous forme texte"""
        resultat = ""
        for elem in self.ligneCase :
            resultat = resultat + str(elem) + ","
        return resultat

    def reloadLigne(self):
        """change la valeur des case de la ligne supérieur à 0"""
        for obj in self.ligneCase :
            obj.reloadCase()

    def snakeMoveLigne(self, xtete, valQueue):
        """permet de changer la valeur de l'absisse de la tete du serpent"""
        self.ligneCase[xtete].valeur = valQueue

    def pommePosLigne(self, xpomme):
        """change l'absisse des coordonnées de la pomme"""
        self.ligneCase[xpomme].valeur = -1

    def checkPosPommeLigne(self, Xpomme):
        """retourne la valeur de de la case désignée pour savoir si elle est occupée"""
        return self.ligneCase[Xpomme].valeur


class Grille():
	"""initiation de la grille de jeu à travers une colonne"""
    def __init__(self,taille=10):
    	"""la taille de la colonne et de la ligne est cheangeable"""
        self.taille = taille
        self.ColoneCase = []
        for i in range(taille):
        	#remplis la colonne de ligne
            self.ColoneCase.append(Ligne(taille))
            #la ligne aussi longue que la colonne

    def __str__(self):
    	"""retourne le contenu de la grille sous forme de texte"""
        resultat = "interieur de la grille :\n"
        for elem in self.ColoneCase:
            resultat = resultat + str(elem) + "\n"
        return resultat


    def reloadGrille(self):
        """change la valeur des cases de la grille supérieures à 0"""
        for obj in self.ColoneCase :
            obj.reloadLigne()

    def snakeMoveGrille(self,xtete,ytete,valQueue):
        """changenge l'ordonnée de la tete du serpent"""
        self.ColoneCase[ytete].snakeMoveLigne(xtete,valQueue)

    def pommePosGrille(self, xpomme, ypomme):
        """change l'ordonnée de la position de la pomme et appelle le changement de l'abscisse"""
        self.ColoneCase[ypomme].pommePosLigne(xpomme)

    def checkPosPommeGrille(self, Xpomme, Ypomme):
        """appelle et retourne la valeur de la case de la grille"""
        return self.ColoneCase[Ypomme].checkPosPommeLigne(Xpomme)


class Snake():
	"""correspond au serpent jouable de la grille"""
    def __init__(self, xtete = 0,ytete = 0, valQueue = 1):
        """initialise les coordonées de la tête et la taille de la queue"""
        self.xtete = xtete
        self.ytete = ytete
        self.valQueue = valQueue
        #permet de savoir la taille de la queue du serpent

    def __str__(self):
    	"""return les données du serpent"""
        reslutat = "pos : [" + self.xtete + "," + self.ytete + "] taille :" + self.valQueue
        return reslutat

    def manger(self):
        """augmente la taille de la queue"""
        self.valQueue = self.valQueue + 1


class Pomme():
	"""correspond à la pomme à recuperer dans la grille"""
    def __init__(self, Xpomme = 1, Ypomme = 1) :
        """initialise les coordonnées de la pomme"""
        self.Xpomme = Xpomme
        self.Ypomme = Ypomme

    def __str__(self):
        """return les coordonnées de la pomme"""
        resultat = "[" + self.Xpomme + "," + self.Ypomme + "]"
        return resultat

    def Positionnement(self, taille):
        """met un positionnement aléatoire à la pomme"""
        self.Xpomme = randint(0,taille-1)
        self.Ypomme = randint(0,taille-1)


class Jeu():
	"""main du jeu permettant de controller tout les details du jeu"""
    def __init__(self,taille=10):
        """crée le necessaire au jeu"""
        self.taille = taille
        self.grille = Grille(taille)
        self.snake = Snake()
        self.pomme = Pomme()
        #self.grille.append(Grille(taille))

    def __str__(self):
    	"""return la situation de la grille"""
        resultat = "" + str(self.grille)
        return resultat

    def reload(self):
        """appele la fonction realoadant la grille avec les nouvelles données"""
        self.grille.reloadGrille()

    def snakeMove(self):
        """change les coordonnées de la tete du serpent"""
        self.grille.snakeMoveGrille(self.snake.xtete,self.snake.ytete,self.snake.valQueue)

    def pommePos(self):
        """établis de nouvelles cordonnées à la pomme, censées être préalablement vide"""
        bonnePos = 1
        while bonnePos != 0 :
            self.pomme.Positionnement(self.taille)
            bonnePos = self.checkPosPomme()
        self.grille.pommePosGrille(self.pomme.Xpomme, self.pomme.Ypomme)

    def checkPosPomme(self):
        """fonction vérifiant que les coordonnées données matchent un case vide""" 
        return self.grille.checkPosPommeGrille(self.pomme.Xpomme,self.pomme.Ypomme)


def main():
    jeu = Jeu(5)
    print(jeu)
    jeu.reload()
    print(jeu)
    jeu.snakeMove()
    print(jeu)
    jeu.pommePos()
    print(jeu)
    jeu.reload()
    print(jeu)

if __name__ == "__main__" :
    main()