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
        si=0
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
        #tabla 1
        
        if column == 1:
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
            self.insertTable(self.act1,QTableWidgetItem,0,2,self.getTotal(self.act1,0,0,self.act1,0,1) )
            self.insertTable(self.act1,QTableWidgetItem,1,2,self.getTotal(self.act1,1,0,self.act1,1,1) )
            self.insertTable(self.act1,QTableWidgetItem,2,2,self.getTotal(self.act1,2,0,self.act1,2,1 ) )
            self.insertTable(self.act1,QTableWidgetItem,3,2,self.getTotal(self.act1,3,0,self.act1,3,1 ))
        #tabla 2
        elif column == 2:
            self.act2 = self.vista_frecuencias.tabla_fre_act2
            self.insertTable(self.act2,QTableWidgetItem,0,0,conNoA)
            self.insertTable(self.act2,QTableWidgetItem,1,0,conNoNp)
            self.insertTable(self.act2,QTableWidgetItem,2,0,conNoR)
            self.insertTable(self.act2,QTableWidgetItem,3,0,(conNoA + conNoNp + conNoR))
            self.insertTable(self.act2,QTableWidgetItem,0,1,conSiA)
            self.insertTable(self.act2,QTableWidgetItem,1,1,conSiNp)
            self.insertTable(self.act2,QTableWidgetItem,2,1,conSiR)
            self.insertTable(self.act2,QTableWidgetItem,3,1,(conSiA + conSiNp + conSiR))
            
            # totales
            self.insertTable(self.act2,QTableWidgetItem,0,2,self.getTotal(self.act2,0,0,self.act2,0,1 ) )
            self.insertTable(self.act2,QTableWidgetItem,1,2,self.getTotal(self.act2,1,0,self.act2,1,1) )
            self.insertTable(self.act2,QTableWidgetItem,2,2,self.getTotal(self.act2,2,0,self.act2,2,1 ) )
            self.insertTable(self.act2,QTableWidgetItem,3,2,self.getTotal(self.act2,3,0,self.act2,3,1 ))
        #tabla 3
        elif column == 3:
            self.act3 = self.vista_frecuencias.tabla_fre_act3
            self.insertTable(self.act3,QTableWidgetItem,0,0,conNoA)
            self.insertTable(self.act3,QTableWidgetItem,1,0,conNoNp)
            self.insertTable(self.act3,QTableWidgetItem,2,0,conNoR)
            self.insertTable(self.act3,QTableWidgetItem,3,0,(conNoA + conNoNp + conNoR))
            self.insertTable(self.act3,QTableWidgetItem,0,1,conSiA)
            self.insertTable(self.act3,QTableWidgetItem,1,1,conSiNp)
            self.insertTable(self.act3,QTableWidgetItem,2,1,conSiR)
            self.insertTable(self.act3,QTableWidgetItem,3,1,(conSiA + conSiNp + conSiR))
            
            # totales
            self.insertTable(self.act3,QTableWidgetItem,0,2,self.getTotal(self.act3,0,0,self.act3,0,1 ) )
            self.insertTable(self.act3,QTableWidgetItem,1,2,self.getTotal(self.act3,1,0,self.act3,1,1) )
            self.insertTable(self.act3,QTableWidgetItem,2,2,self.getTotal(self.act3,2,0,self.act3,2,1 ) )
            self.insertTable(self.act3,QTableWidgetItem,3,2,self.getTotal(self.act3,3,0,self.act3,3,1 ))
        #tabla 4
        elif column == 4:
            self.act4 = self.vista_frecuencias.tabla_fre_act4
            self.insertTable(self.act4,QTableWidgetItem,0,0,conNoA)
            self.insertTable(self.act4,QTableWidgetItem,1,0,conNoNp)
            self.insertTable(self.act4,QTableWidgetItem,2,0,conNoR)
            self.insertTable(self.act4,QTableWidgetItem,3,0,(conNoA + conNoNp + conNoR))
            self.insertTable(self.act4,QTableWidgetItem,0,1,conSiA)
            self.insertTable(self.act4,QTableWidgetItem,1,1,conSiNp)
            self.insertTable(self.act4,QTableWidgetItem,2,1,conSiR)
            self.insertTable(self.act4,QTableWidgetItem,3,1,(conSiA + conSiNp + conSiR))
            
            # totales
            self.insertTable(self.act4,QTableWidgetItem,0,2,self.getTotal(self.act4,0,0,self.act4,0,1 ) )
            self.insertTable(self.act4,QTableWidgetItem,1,2,self.getTotal(self.act4,1,0,self.act4,1,1) )
            self.insertTable(self.act4,QTableWidgetItem,2,2,self.getTotal(self.act4,2,0,self.act4,2,1 ) )
            self.insertTable(self.act4,QTableWidgetItem,3,2,self.getTotal(self.act4,3,0,self.act4,3,1 ))
        #tabla 5
        elif column == 5:
            self.act5 = self.vista_frecuencias.tabla_fre_act5
            self.insertTable(self.act5,QTableWidgetItem,0,0,conNoA)
            self.insertTable(self.act5,QTableWidgetItem,1,0,conNoNp)
            self.insertTable(self.act5,QTableWidgetItem,2,0,conNoR)
            self.insertTable(self.act5,QTableWidgetItem,3,0,(conNoA + conNoNp + conNoR))
            self.insertTable(self.act5,QTableWidgetItem,0,1,conSiA)
            self.insertTable(self.act5,QTableWidgetItem,1,1,conSiNp)
            self.insertTable(self.act5,QTableWidgetItem,2,1,conSiR)
            self.insertTable(self.act5,QTableWidgetItem,3,1,(conSiA + conSiNp + conSiR))
            
            # totales
            self.insertTable(self.act5,QTableWidgetItem,0,2,self.getTotal(self.act5,0,0,self.act5,0,1 ) )
            self.insertTable(self.act5,QTableWidgetItem,1,2,self.getTotal(self.act5,1,0,self.act5,1,1) )
            self.insertTable(self.act5,QTableWidgetItem,2,2,self.getTotal(self.act5,2,0,self.act5,2,1 ) )
            self.insertTable(self.act5,QTableWidgetItem,3,2,self.getTotal(self.act5,3,0,self.act5,3,1 ))
        #tabla 6
        elif column == 6:
            self.act6 = self.vista_frecuencias.tabla_fre_act6
            self.insertTable(self.act6,QTableWidgetItem,0,0,conNoA)
            self.insertTable(self.act6,QTableWidgetItem,1,0,conNoNp)
            self.insertTable(self.act6,QTableWidgetItem,2,0,conNoR)
            self.insertTable(self.act6,QTableWidgetItem,3,0,(conNoA + conNoNp + conNoR))
            self.insertTable(self.act6,QTableWidgetItem,0,1,conSiA)
            self.insertTable(self.act6,QTableWidgetItem,1,1,conSiNp)
            self.insertTable(self.act6,QTableWidgetItem,2,1,conSiR)
            self.insertTable(self.act6,QTableWidgetItem,3,1,(conSiA + conSiNp + conSiR))
            
            # totales
            self.insertTable(self.act6,QTableWidgetItem,0,2,self.getTotal(self.act6,0,0,self.act6,0,1 ) )
            self.insertTable(self.act6,QTableWidgetItem,1,2,self.getTotal(self.act6,1,0,self.act6,1,1) )
            self.insertTable(self.act6,QTableWidgetItem,2,2,self.getTotal(self.act6,2,0,self.act6,2,1 ) )
            self.insertTable(self.act6,QTableWidgetItem,3,2,self.getTotal(self.act6,3,0,self.act6,3,1 ))
        return si,no

    
    
    def getTotal(self,tabla,x,y, tabla2,x2,y2):
        return int(tabla.item(x,y).text()) + int(tabla2.item(x2,y2).text())
    
    def getProbability(self,tabla1,tabla2,QTableWidgetItem):
        for i in range(3):
            for j in range(3):
                a = float(tabla1.item(i,j).text())+1
                b = float(tabla1.item(3,j).text())+3
                res = float(a/b) 
                tabla2.setItem(i,j, QTableWidgetItem(str(res)))

    def getPosition(self,tabla,x,y):
        return float(tabla.item(x,y).text())
               
    