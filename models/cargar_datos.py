from  connection.connection import DataBase



def CargarDatos(tabla, QTableWidgetItem):
    bd = DataBase()
    data = bd.getData()
    tabla.setColumnCount(len(data[0]))
    tabla.setRowCount(len(data))
    for row in range(len(data)):
        for column in range(len(data[row])):
            tabla.setItem(
            row, column, QTableWidgetItem(str(data[row][column])))

def getDelete(id):
    bd = DataBase()
    bd.removeData(id)
    return "Dato eliminado con éxito"

def setDatos(act1,act2,act3,act4,act5,act6,estado):
    bd = DataBase()
    bd.setData(act1,act2,act3,act4,act5,act6,estado)
    return "Dato insertado con éxito"

def getDatos():
    bd = DataBase()
    data = bd.getData()
    return data 
    