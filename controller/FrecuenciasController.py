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
        
    def InsertDataFrecAct(self,column):
        data = getDatos()
       
        conSiA = 0;conSiNp = 0;conSiR = 0;conNoA = 0;conNoNp = 0;conNoR = 0;
        si = 0
        no = 0 #vamos a contar cuantos si y no
        
        # Recorremos la tupla de datos y valídamos
        
        for i in range(len(data)):
            if str(data[i][column]).upper().strip() == "A" and str(data[i][7]).upper().strip()  == "SI":
                conSiA+=1
                si+=1
            elif str(data[i][column]).upper().strip() == "NP" and str(data[i][7]).upper().strip()  == "SI":
                conSiNp+=1
                si +=1
            elif str(data[i][column]).upper().strip() == "R" and str(data[i][7]).upper().strip()  == "SI":
                conSiR+=1
                si+=1
            elif  str(data[i][column]).upper().strip()  == "A" and str(data[i][7]).upper().strip()  == "NO":
                conNoA+=1
                no+=1
            elif str(data[i][column]).upper().strip()  == "NP" and str(data[i][7]).upper().strip()  == "NO":
                conNoNp+=1
                no+=1
            else:
                if str(data[i][column]).upper().strip()  == "R" and str(data[i][7]).upper().strip()  == "NO":
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
        self.insertTable(self.act1,QTableWidgetItem,0,2,self.getTotal(self.act1,0,0,self.act1,0,0 ) )
        self.insertTable(self.act1,QTableWidgetItem,1,2,self.getTotal(self.act1,1,0,self.act1,1,1) )
        self.insertTable(self.act1,QTableWidgetItem,2,2,self.getTotal(self.act1,2,0,self.act1,2,1 ) )
        self.insertTable(self.act1,QTableWidgetItem,3,2,self.getTotal(self.act1,3,0,self.act1,3,1 ))
        

    def getPosition(self,x,y):
        return float(self.vista_frecuencias.tabla_fre_act1.item(x,y).text())
    
    def getTotal(self,tabla,x,y, tabla2,x2,y2):
        return int(tabla.item(x,y).text()) + int(tabla2.item(x2,y2).text())
    