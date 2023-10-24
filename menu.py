from persistence import getUserStatistics

from casino import casino_sextius_sullivan
def showMenu():
    print("Menu:")
    print("1. Jouer")
    print("2. Règles")
    print("3. Statistiques")
    print("4. Quitter")

def showRules():
    print("*  *  *  *  *  *  *  *  *  *  * REGLES DU JEU *  *  *  *  *  *  *  *  *\n")
    print("""Le jeu comporte 3 levels avec la possibilié que le joueur choissise son level (si ce n'est pas sa 1è fois dans le Casino).
	En d'autres termes, tout nouveau joueur doit passer par le 1è level. Suite à la 1è partie, il a le droit de choisir son level en lui rappelant / proposant le dernier niveau atteint\n.
	Lors de chaque niveau, Python tire un nombre : level 1 (entre 1 et 10),
	level2 (1 et 20), level3 (1 et 30). C'est à vous de deviner le nombre mystérieux avec 3 essais (en tout) lors du 1è 
	level, 5 au 2è level et 7 au 3è level. Chaque essai ne durera pas plus de 10 secondes. Au-delà, 
	vous perdez votre essai. Att : si vous perdez un level, vous rejouez le level précédent.
	Quand vous souhaitez quitter le jeu, un compteur de 10 secondes est mis en place. 
	En absence de validation de la décision, le jeu est terminé.
	Python fournit enfin les statistiques du jeu""")

def getMenuChoice():
    try:
        choice = int(input("Votre choix: "))
        if choice < 1 or choice > 4:
            raise ValueError
        return choice
    except ValueError:
        print("Veuillez entrer un nombre entier entre 1 et 4")
        return getMenuChoice()

def mainMenu(user):
    showMenu()
    userChoice = getMenuChoice()
    if userChoice == 1:
        casino_sextius_sullivan(user)

    elif userChoice == 2:
        showRules()
        input("Appuyez sur la touche 'entrer' pour revenir au menu principal")
        mainMenu(user)
    elif userChoice == 3:
        stats = getUserStatistics(user[0])
        print(stats)
        print("Statistiques")

    elif userChoice == 4:
        print("Quitter")