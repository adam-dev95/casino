#Un nombre entre 1 et 100 est choisi par le programme en aléatoire
#Le joueur entre un nombre
#Le programme prend le nombre du joueur et le divise par 2
#CASINO SEXTIUS SULLIVAN
import random
INCR_PARTY = 3
COMPTEUR = 0
MISE_JOUEUR = 0

nombre_user = 0
recommencer = "o"
print("Je viens de penser à un nombre entre 1 et 10. Devinez lequel? ")
print("	\t- Att : vous avez le droit à trois essais !\n \t- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n \t- Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n \t- Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n \t- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et")
NOMBRE_ALEATOIRE = random.randint(1, 10)
while(COMPTEUR >= 0 and INCR_PARTY >= 0 and recommencer == "o"):
        if(COMPTEUR == 0):
            MISE_ACTUEL  = int(input("Le jeu commence, entrez votre mise. Entrez une MISE :  "))
        if(INCR_PARTY == 1):
            print("Il vous reste une partie")
        nombre_user = int(input("Alors mon nombre est :  "))
        if(nombre_user > NOMBRE_ALEATOIRE):
            print("Votre nombre est trop grand")
        elif(nombre_user < NOMBRE_ALEATOIRE):
            print("Votre nombre est trop petit")
            #CAS GAGNANT
        if(nombre_user == NOMBRE_ALEATOIRE and INCR_PARTY == 3):
                print("Vous remportez le double de votre MISE soit",MISE_JOUEUR + MISE_ACTUEL * 2)
                recommencer = str(input("Voulez-vous recommencer [o/n]"))
                if(recommencer == "o"):
                    NOMBRE_ALEATOIRE = random.randint(1, 10)
                    COMPTEUR = 0
                    INCR_PARTY = 4
                else :
                    break
        if(nombre_user == NOMBRE_ALEATOIRE and INCR_PARTY == 2):
                print("Vous remportez votre MISE soit : ",MISE_JOUEUR + MISE_ACTUEL)
                recommencer = str(input("Voulez-vous recommencer [o/n]"))
                if(recommencer == "o"):
                    NOMBRE_ALEATOIRE = random.randint(1, 10)
                    COMPTEUR = 0
                    INCR_PARTY = 4
                else :
                    break
        if(nombre_user == NOMBRE_ALEATOIRE and INCR_PARTY == 1):
                print("Vous remportez le moitié de votre MISE soit : ",MISE_JOUEUR + MISE_ACTUEL / 2)
                recommencer = str(input("Voulez-vous recommencer [o/n]"))
                if(recommencer == "o"):
                    NOMBRE_ALEATOIRE = random.randint(1, 10)
                    COMPTEUR = 0
                    INCR_PARTY = 4
                else :
                    break
        #CAS PERDANT
        if(nombre_user != NOMBRE_ALEATOIRE and INCR_PARTY == 1):
                print("Perdu ! Vous avez perdu votre mise, ",MISE_ACTUEL - MISE_JOUEUR)
                recommencer = str(input("Voulez-vous recommencer [o/n]"))
                if(recommencer == "o"):
                    NOMBRE_ALEATOIRE = random.randint(1, 10)
                    COMPTEUR = 0
                    INCR_PARTY = 4
                else :
                    break
        INCR_PARTY-=1
        COMPTEUR+=1


