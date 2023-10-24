from menu import mainMenu
from persistence import loginOrInsertUser

def main():
    user = signin_user()
    print("Hello {}, vous avez {} €, Très bien ! Installez vous SVP à la table de pari.\n\t\t\t Je vous expliquerai le principe du jeu : \n".format(user[1], user[3]))
    mainMenu()

def signin_user():
    print("*  *  *  *  *  *  *  *  *  *  *  BIENVENUE DANS LE CASINO  *  *  *  *  *  *  *  *  *  *  *\n")
    name = input("Je suis Python. Quel est votre pseudo ? \n")
    return loginOrInsertUser(name)

if __name__ == "__main__":
    main()