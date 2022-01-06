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
    
    def setData(self,act1,act2,act3,act4,act5,act6,estado):
        sql = "INSERT INTO actividades (actividad_1,actividad_2,actividad_3,actividad_4,actividad_5,actividad_6, estado) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (act1,act2,act3,act4,act5,act6,estado)
        self.cursor.execute(sql, val)
        self.connection.commit()
    
    def removeData(self,id):
        sql = f"DELETE FROM actividades WHERE id = {str(id)} "
        self.cursor.execute(sql)
        self.connection.commit()