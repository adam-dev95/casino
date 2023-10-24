import random
import threading
from persistence import hasLostGame, insertUserStatistics, hasWinGame

def recommencer_jeu():
    recommencer = input("Voulez-vous recommencer [o/n]")
    return recommencer == "o"

def timeout(INCR_PARTY):
    print("Temps écoulé. Aucune réponse n'a été donnée.")
    INCR_PARTY[0] += 1  # Augmente INCR_PARTY de 1
    exit()

def casino_sextius_sullivan(user):
    
    COMPTEUR = 0
    MISE_JOUEUR = 0
    INCR_PARTY = [0]  # Utilisation d'une liste pour stocker INCR_PARTY

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
            MISE_ACTUEL = int(input("Le jeu commence, entrez votre mise. Entrez une MISE :  "))
            if MISE_ACTUEL > user[3]:
                print("Erreur, votre mise est plus élevée que votre solde.")
                break
            NIVEAU = int(input("Choisissez un niveau [1 / 2 / 3] "))
            
            NOMBRE_ALEATOIRE = random.randint(1, int(NIVEAU * 10))
            print(NOMBRE_ALEATOIRE, "nombre aléatoire")

            INCR_PARTY[0] = obj[NIVEAU]
        
        if INCR_PARTY[0] == 1:
            print("Il vous reste une partie")

        # Utilisation d'un thread de minuterie pour gérer le délai de 10 secondes
        timer = threading.Timer(10, timeout, args=(INCR_PARTY,))
        timer.start()

        try:
            nombre_user = int(input("Alors mon nombre est :  "))
        except ValueError:
            print("Entrée invalide. Vous devez saisir un nombre entier.")
            exit()
        
        # Annuler la minuterie si l'utilisateur a saisi un nombre
        timer.cancel()

        if nombre_user > NOMBRE_ALEATOIRE:
            print("Votre nombre est trop grand")
        elif nombre_user < NOMBRE_ALEATOIRE:
            print("Votre nombre est trop petit")
        
        # CAS GAGNANT
        if nombre_user == NOMBRE_ALEATOIRE:
            gain = MISE_ACTUEL * (INCR_PARTY[0] / obj[NIVEAU])
            print(obj[NIVEAU], INCR_PARTY[0])
            print("Vous remportez ", gain ,"€")
            hasWinGame(user[0], gain)

            if not recommencer_jeu():
                break
        
        # CAS PERDANT
        if nombre_user != NOMBRE_ALEATOIRE and INCR_PARTY[0] == 1:
            perte = MISE_ACTUEL - MISE_JOUEUR

            hasLostGame(user[0], perte)
            print("Perdu ! Vous avez perdu votre mise, ", perte, "€", "Le nombre était :", NOMBRE_ALEATOIRE)
            insertUserStatistics(user[0], perte, 0, NIVEAU, 3, 0)
            
            if not recommencer_jeu():
                break
        
        INCR_PARTY[0] -= 1
        COMPTEUR += 1


