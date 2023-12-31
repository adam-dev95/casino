import random
import threading
from persistence import hasLostGame, insertUserStatistics, hasWinGame

def recommencer_jeu():
    recommencer = input("Voulez-vous recommencer [o/n]")
    return recommencer == "o"

def timeout(INCR_PARTY):
    print("Temps écoulé. Aucune réponse n'a été donnée.")
    INCR_PARTY[0] -= 1

def demander_nombre_utilisateur():
    nombre_user = -1
    while nombre_user < 0:
        try:
            nombre_user = int(input("Alors mon nombre est :  "))
        except ValueError:
            print("Erreur, veuillez entrer un nombre entier")
    return nombre_user

def casino(user):
    COMPTEUR = 0
    MISE_JOUEUR = 0
    INCR_PARTY = [0] 

    print("Je viens de penser à un nombre entre 1 et 10. Devinez lequel?")
    print("\t- Att : vous avez le droit à trois essais!")
    print("\t- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise!")
    print("\t- Si vous le devinez au 2è coup, vous gagnez exactement votre mise!")
    print("\t- Si vous le devinez au 3è coup, vous gagnez la moitié de votre mise!")
    print("\t- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et")

    NOMBRE_ALEATOIRE = random.randint(1, 10)

    obj = {
        1: 3,
        2: 5,
        3: 9
    }

    while COMPTEUR >= 0 and INCR_PARTY[0] >= 0:
        if COMPTEUR == 0:
            print("Le jeu commence, entrez votre mise.")
            MISE_ACTUEL = 0 
            while MISE_ACTUEL <= 0:
                try:
                    MISE_ACTUEL = int(input("Entrez une MISE :  "))
                except ValueError:
                    print("Erreur, veuillez entrer un nombre entier")
            if MISE_ACTUEL > user[3]:
                print("Erreur, votre mise est plus élevée que votre solde.")
                break
            userLevel = user[2]
            array = []

            for i in range(1, userLevel + 1):
                array.append(i)

            result = ', '.join(map(str, array))

            NIVEAU = int(input("Choisissez un niveau [" + result + "] : "))
            
            NOMBRE_ALEATOIRE = random.randint(1, int(NIVEAU * 10))
            print(NOMBRE_ALEATOIRE, "nombre aléatoire")

            INCR_PARTY[0] = obj[NIVEAU]
        
        if INCR_PARTY[0] == 1:
            print("Il vous reste une partie")

        nombre_user = -1
        timer = threading.Timer(10, timeout, args=(INCR_PARTY,))
        timer.start()

        while nombre_user < 0:
            try:
                nombre_user = int(input("Alors mon nombre est :  "))
                if nombre_user < 0:
                    raise ValueError
            except ValueError:
                print("Erreur, veuillez entrer un nombre entier")
        
        timer.cancel()

        if nombre_user > NOMBRE_ALEATOIRE:
            print("Votre nombre est trop grand")
        elif nombre_user < NOMBRE_ALEATOIRE:
            print("Votre nombre est trop petit")
        
        if nombre_user == NOMBRE_ALEATOIRE:
            gain = MISE_ACTUEL * (INCR_PARTY[0] / obj[NIVEAU])
            hasWinGame(user, gain)
            insertUserStatistics(user[0], MISE_ACTUEL, gain, NIVEAU, obj[NIVEAU] - INCR_PARTY[0], 1)
            print("Bingo !! Vous avez gagné " + str(gain))
            if not recommencer_jeu():
                break
        
        if nombre_user != NOMBRE_ALEATOIRE and INCR_PARTY[0] == 1:
            perte = MISE_ACTUEL - MISE_JOUEUR

            hasLostGame(user[0], perte)
            print("Perdu ! Vous avez perdu votre mise, ", perte, "€", "Le nombre était :", NOMBRE_ALEATOIRE)
            insertUserStatistics(user[0], perte, 0, NIVEAU, 3, 0)
            
            if not recommencer_jeu():
                break
        
        INCR_PARTY[0] -= 1
        COMPTEUR += 1
