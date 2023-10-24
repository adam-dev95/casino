from database import get_cursor

def getAllUsers():
    connection, cursor = get_cursor()
    if cursor:
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        return users

def getUserByName(name):
    connection, cursor = get_cursor()
    if cursor:
        query = "SELECT * FROM users WHERE name = %s"
        cursor.execute(query, (name,))
        user = cursor.fetchone()
        print(user)
        return user

def getUserStatistics(id):
    connection, cursor = get_cursor()
    if cursor:
        query = "SELECT * FROM statistics WHERE id_users = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()

        column_names = cursor.column_names
        if result:
            data = {column: value for column, value in zip(column_names, result)}
            print(data)
            return data
    return None

def increaseMaxWin(user_id, amount_to_increase):
    connection, cursor = get_cursor()
    if cursor:
        query = "UPDATE statistics SET maxWin = %s WHERE id_users = %s"
        cursor.execute(query, (amount_to_increase, user_id))
        connection.commit()


def loginOrInsertUser(name):
    connection, cursor = get_cursor()
    if cursor:
        query = "SELECT * FROM users WHERE name = %s"
        cursor.execute(query, (name,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            return f"Bon retour {name} !"
        else:
            insert_query = "INSERT INTO users (name) VALUES (%s)"
            cursor.execute(insert_query, (name,))
            connection.commit()
            return f"Nouvel utilisateur {name} inséré !"

loginOrInsertUser("adam")    