from menu import mainMenu
from mysqlconnection import get_user, insert_user

def main():
    user = signin_user()
    print("Bienvenue {} !".format(user[1]))
    mainMenu()

def signin_user():
    print("*  *  *  *  *  *  *  *  *  *  *  BIENVENUE DANS LE CASINO  *  *  *  *  *  *  *  *  *  *  *\n")
    name = input("Je suis Python. Quel est votre pseudo ? \n")
    user = get_user(name)
    if user is None:
        insert_user(name)
        user = get_user(name)
    return user

if __name__ == "__main__":
    main()