import mysql.connector

def execute_query():
    try:
        connection = mysql.connector.connect(
            host='mysql-casinoimieparis.alwaysdata.net',
            database='casinoimieparis_bdd',
            user='332916_admin',
            password='adminadmincasino'
        )

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()

            # Votre requête SQL ici
            query = "SELECT * FROM users"
            cursor.execute(query)
            records = cursor.fetchall()

            for record in records:
                print(record)

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    execute_query()
