from PyQt5.QtWidgets import (QMessageBox,
     QDesktopWidget, QDialog,QTableWidgetItem)
from view.frecuencias  import Ui_Frecuencias
from models.cargar_datos import getDatos

class VistaFrecuencia(QDialog):
    def __init__(self):
        super(VistaFrecuencia, self).__init__()
        self.vista_frecuencias = Ui_Frecuencias()
        self.vista_frecuencias.setupUi(self)

        # centrar ventana
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2),
                  int((screen.height() - size.height())/2))

    def insertTable(self,tabla, QTableWidgetItem,x,y,dato):
        tabla.setItem(x,y, QTableWidgetItem(str(dato)))
        
    def InsertDataFrecAct(self):
        data = getDatos()
       
        conSiA = 0;conSiNp = 0;conSiR = 0;conNoA = 0;conNoNp = 0;conNoR = 0;
        si = 0
        no = 0 #vamos a contar cuantos si y no
        
        # Recorremos la tupla de datos y valídamos
        for row in range(len(data)):
            for column in range(len(data[row])):
                if str(data[row][column]).upper().strip() == "A" and str(data[row][7]).upper().strip()  == "SI":
                    conSiA+=1
                    si+=1
                elif str(data[row][column]).upper().strip() == "NP" and str(data[row][7]).upper().strip()  == "SI":
                    conSiNp+=1
                    si +=1
                elif str(data[row][column]).upper().strip() == "R" and str(data[row][7]).upper().strip()  == "SI":
                    conSiR+=1
                    si+=1
                elif  str(data[row][column]).upper().strip()  == "A" and str(data[row][7]).upper().strip()  == "NO":
                    conNoA+=1
                    no+=1
                elif str(data[row][column]).upper().strip()  == "NP" and str(data[row][7]).upper().strip()  == "NO":
                    conNoNp+=1
                    no+=1
                else:
                    if str(data[row][column]).upper().strip()  == "R" and str(data[row][7]).upper().strip()  == "NO":
                        conNoR+=1
                        no+=1

        # rellenamos las tablas
        self.act1 = self.vista_frecuencias.tabla_fre_act1
        self.insertTable(self.act1,QTableWidgetItem,0,0,conNoA)
        self.insertTable(self.act1,QTableWidgetItem,1,0,conNoNp)
        self.insertTable(self.act1,QTableWidgetItem,2,0,conNoR)
        self.insertTable(self.act1,QTableWidgetItem,3,0,(conNoA + conNoNp + conNoR))
        self.insertTable(self.act1,QTableWidgetItem,0,1,conSiA)
        self.insertTable(self.act1,QTableWidgetItem,1,1,conSiNp)
        self.insertTable(self.act1,QTableWidgetItem,2,1,conSiR)
        self.insertTable(self.act1,QTableWidgetItem,3,1,(conSiA + conSiNp + conSiR))
        
        # totales
        self.insertTable(self.act1,QTableWidgetItem,0,2,int(self.act1.item(0,0).text()+self.act1.item(0,1).text()) )
        self.insertTable(self.act1,QTableWidgetItem,1,2,int(self.act1.item(1,0).text()+self.act1.item(1,1).text()) )
        self.insertTable(self.act1,QTableWidgetItem,2,2,int(self.act1.item(2,0).text()+self.act1.item(2,1).text()) )
        self.insertTable(self.act1,QTableWidgetItem,3,2,int(self.act1.item(3,0).text()+self.act1.item(3,1).text()) )
