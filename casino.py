import random
import threading
from persistence import hasLostGame, insertUserStatistics, hasWinGame

def recommencer_jeu():
    recommencer = input("Voulez-vous recommencer [o/n]")
    return recommencer == "o"

def timeout():
    print("Temps écoulé. Aucune réponse n'a été donnée.")
    exit()

def casino_sextius_sullivan(user):
    
    COMPTEUR = 0
    MISE_JOUEUR = 0
    INCR_PARTY = 0
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

    while COMPTEUR >= 0 and INCR_PARTY >= 0:
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
            NIVEAU = int(input("Choisissez un niveau [1 / 2 / 3] "))
            
            NOMBRE_ALEATOIRE = random.randint(1, int(NIVEAU * 10))
            print(NOMBRE_ALEATOIRE, "nombre aléatoire")

            INCR_PARTY = obj[NIVEAU]
        
        if INCR_PARTY == 1:
            print("Il vous reste une partie")

        nombre_user = -1

        while nombre_user < 0:
            try:
                nombre_user = int(input("Alors mon nombre est :  "))
            except ValueError:
                print("Erreur, veuillez entrer un nombre entier")
        # Utilisation d'un thread de minuterie pour gérer le délai de 10 secondes
        timer = threading.Timer(10, timeout)
        timer.start()

        try:
            nombre_user = int(input("Alors mon nombre est :  "))
        except ValueError:
            INCR_PARTY = INCR_PARTY + 1
            COMPTEUR = COMPTEUR + 1
            print("Entrée invalide. Vous devez saisir un nombre entier.")
            #exit()
        
        # Annuler la minuterie si l'utilisateur a saisi un nombre
        timer.cancel()

        if nombre_user > NOMBRE_ALEATOIRE:
            print("Votre nombre est trop grand")
        elif nombre_user < NOMBRE_ALEATOIRE:
            print("Votre nombre est trop petit")
        
        # CAS GAGNANT
        if nombre_user == NOMBRE_ALEATOIRE:
            gain = MISE_ACTUEL * (INCR_PARTY / obj[NIVEAU])
            print(obj[NIVEAU], INCR_PARTY)
            print("Vous remportez ", gain ,"€")
            hasWinGame(user[0], gain)
            insertUserStatistics(user[0], MISE_ACTUEL, gain, NIVEAU, obj[NIVEAU] - INCR_PARTY, 1)

            if not recommencer_jeu():
                break
        
        # CAS PERDANT
        if nombre_user != NOMBRE_ALEATOIRE and INCR_PARTY == 1:
            perte = MISE_ACTUEL - MISE_JOUEUR

            hasLostGame(user[0], perte)
            print("Perdu ! Vous avez perdu votre mise, ", perte, "€", "Le nombre était :", NOMBRE_ALEATOIRE)
            insertUserStatistics(user[0], perte, 0, NIVEAU, 3, 0)
            if not recommencer_jeu():
                break
        INCR_PARTY -= 1
        COMPTEUR += 1
