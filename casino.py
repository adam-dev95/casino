import random

def recommencer_jeu():
    recommencer = input("Voulez-vous recommencer [o/n]")
    return recommencer == "o"


def casino_sextius_sullivan():
    INCR_PARTY = 3
    COMPTEUR = 0
    MISE_JOUEUR = 0

    print("Je viens de penser à un nombre entre 1 et 10. Devinez lequel?")
    print("\t- Att : vous avez le droit à trois essais!")
    print("\t- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise!")
    print("\t- Si vous le devinez au 2è coup, vous gagnez exactement votre mise!")
    print("\t- Si vous le devinez au 3è coup, vous gagnez la moitié de votre mise!")
    print("\t- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et")

    NOMBRE_ALEATOIRE = random.randint(1, 10)

    while COMPTEUR >= 0 and INCR_PARTY >= 0:
        if COMPTEUR == 0:
            MISE_ACTUEL = int(input("Le jeu commence, entrez votre mise. Entrez une MISE :  "))
            NIVEAU = int(input("Choississez un niveau [1 / 2 / 3] "))
            NOMBRE_ALEATOIRE = random.randint(1, int(NIVEAU*10))
        if INCR_PARTY == 1:
            print("Il vous reste une partie")

        nombre_user = int(input("Alors mon nombre est :  "))

        if nombre_user > NOMBRE_ALEATOIRE:
            print("Votre nombre est trop grand")
        elif nombre_user < NOMBRE_ALEATOIRE:
            print("Votre nombre est trop petit")
        # CAS GAGNANT
        if nombre_user == NOMBRE_ALEATOIRE and INCR_PARTY == 3:
            gain = MISE_JOUEUR + MISE_ACTUEL * 2
            print("Vous remportez le double de votre MISE soit", gain, "€")
            if not recommencer_jeu():
                break
        if nombre_user == NOMBRE_ALEATOIRE and INCR_PARTY == 2:
            gain = MISE_JOUEUR + MISE_ACTUEL
            print("Vous remportez votre MISE soit : ", gain)
            if not recommencer_jeu():
                break
        if nombre_user == NOMBRE_ALEATOIRE and INCR_PARTY == 1:
            gain = MISE_JOUEUR + MISE_ACTUEL / 2
            print("Vous remportez la moitié de votre MISE soit : ", gain, "€")
            if not recommencer_jeu():
                break
        # CAS PERDANT
        if nombre_user != NOMBRE_ALEATOIRE and INCR_PARTY == 1:
            perte = MISE_ACTUEL - MISE_JOUEUR
            print("Perdu ! Vous avez perdu votre mise, ", perte, "€", "Le nombre était :",NOMBRE_ALEATOIRE)
            if not recommencer_jeu():
                break
        INCR_PARTY -= 1
        COMPTEUR += 1

# Appel de la fonction principale
casino_sextius_sullivan()
