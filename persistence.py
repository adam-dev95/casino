from database import get_cursor
connection, cursor = get_cursor()

def getUserByName(name):
    if cursor:
        query = "SELECT * FROM users WHERE name = %s"
        cursor.execute(query, (name,))
        user = cursor.fetchone()
        print(user)
        return user

def getUserStatistics(id):
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
    if cursor:
        query = "UPDATE statistics SET maxWin = %s WHERE id_users = %s"
        cursor.execute(query, (amount_to_increase, user_id))
        connection.commit()


def loginOrInsertUser(name):
    if cursor:
        query = "SELECT * FROM users WHERE name = %s"
        cursor.execute(query, (name,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            return existing_user
        else:
            insert_query = "INSERT INTO users (name) VALUES (%s)"
            cursor.execute(insert_query, (name,))
            connection.commit()
            return getUserByName(name)

def insertUserStatistics(id_users, bet, gain, level, attempts, hasWin):
    if cursor:
        query = "INSERT INTO statistics (id_users, bet, gain, level, attempts, hasWin) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id_users, bet, gain, level, attempts, hasWin))
        connection.commit()

def getUserStatistics(id):
    if cursor:
        query = "SELECT AVG(bet) AS average_bet, AVG(gain) AS average_gain, MAX(bet) AS max_bet, MAX(gain) AS max_gain, (SUM(hasWin) / COUNT(hasWin)) * 100 FROM statistics WHERE id_users = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        
        column_names = cursor.column_names
        statistics = {column_names[i]: result[i] for i in range(len(column_names))}
        return statistics

def hasLostGame(user_id, decrement_amount):
    if cursor:
        check_query = "SELECT balance FROM users WHERE id = %s"
        cursor.execute(check_query, (user_id,))
        result = cursor.fetchone()

        if result:
            current_balance = result[0]
            if current_balance >= decrement_amount:
                update_query = "UPDATE users SET balance = balance - %s WHERE id = %s"
                cursor.execute(update_query, (decrement_amount, user_id))
                connection.commit()
                return f"Balance mise à jour avec succès. Nouvelle balance : {current_balance - decrement_amount}"
            else:
                return "Fonds insuffisants pour le décrément."
        else:
            return "L'utilisateur avec l'ID spécifié n'existe pas."
        
def hasWinGame(user, increment_amount):
    if cursor:
        check_query = "SELECT balance FROM users WHERE id = %s"
        cursor.execute(check_query, (user[0],))
        result = cursor.fetchone()

        if result:
            current_balance = result[0]
            update_query = "UPDATE users SET balance = balance + %s WHERE id = %s"
            cursor.execute(update_query, (increment_amount, user[0]))
            connection.commit()
            if user[2] < 3:
                level_query = "UPDATE users SET level = level + 1 WHERE id = %s"
                cursor.execute(level_query, ( user[0], ))
                connection.commit()
        else:
            return "L'utilisateur avec l'ID spécifié n'existe pas."
