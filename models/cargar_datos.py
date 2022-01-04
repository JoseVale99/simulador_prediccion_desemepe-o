from  connection.connection import DataBase

bd = DataBase()

def CargarDatos(tabla, QTableWidgetItem):
    global bd
    data = bd.getData()
    tabla.setColumnCount(len(data[0]))
    tabla.setRowCount(len(data))
    for row in range(len(data)):
        for column in range(len(data[row])):
            tabla.setItem(
            row, column, QTableWidgetItem(str(data[row][column])))