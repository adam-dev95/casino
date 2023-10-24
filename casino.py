import random
from persistence import hasLostGame, insertUserStatistics, hasWinGame

def recommencer_jeu():
    recommencer = input("Voulez-vous recommencer [o/n]")
    return recommencer == "o"


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
           
            MISE_ACTUEL = int(input("Le jeu commence, entrez votre mise. Entrez une MISE :  "))
            if MISE_ACTUEL > user[3]:
                print("Erreur, votre mise est plus elevé que votre solde.")
                break
            NIVEAU = int(input("Choississez un niveau [1 / 2 / 3] "))

            NOMBRE_ALEATOIRE = random.randint(1, int(NIVEAU*10))
            print(NOMBRE_ALEATOIRE, "nombre aléatoire")

            INCR_PARTY = obj[NIVEAU]
        if INCR_PARTY == 1:
            print("Il vous reste une partie")

        nombre_user = int(input("Alors mon nombre est :  "))

        if nombre_user > NOMBRE_ALEATOIRE:
            print("Votre nombre est trop grand")
        elif nombre_user < NOMBRE_ALEATOIRE:
            print("Votre nombre est trop petit")
        # CAS GAGNANT
        if nombre_user == NOMBRE_ALEATOIRE:
            gain = MISE_ACTUEL * ( INCR_PARTY / obj[NIVEAU])
            print(obj[NIVEAU], INCR_PARTY)
            print("Vous remportez ", gain ,"€")
            hasWinGame(user[0], gain)

            if not recommencer_jeu():
                break
        # CAS PERDANT
        if nombre_user != NOMBRE_ALEATOIRE and INCR_PARTY == 1:
            perte = MISE_ACTUEL - MISE_JOUEUR

            hasLostGame(id, perte)
            print("Perdu ! Vous avez perdu votre mise, ", perte, "€", "Le nombre était :",NOMBRE_ALEATOIRE)
            insertUserStatistics(user[0], perte, 0, NIVEAU, 3, 0)
            if not recommencer_jeu():
                break
        INCR_PARTY -= 1
        COMPTEUR += 1


