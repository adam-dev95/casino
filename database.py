import mysql.connector

def get_cursor():
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
        return connection, cursor
