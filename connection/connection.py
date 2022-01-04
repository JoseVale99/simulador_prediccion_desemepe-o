# connection to database with Mysql. 
import mysql.connector

class DataBase:
    def __init__(self):
        self.connection = mysql.connector.connect(
        host = "localhost",
        user = "admin",
        password = "123456789",
        database = "actividades_ito"
        )
        self.cursor = self.connection.cursor()
    
    def getData(self):
        self.cursor.execute("SELECT * FROM actividades")
        data = self.cursor.fetchall()
        return data