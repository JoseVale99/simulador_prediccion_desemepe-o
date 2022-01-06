from PyQt5.QtWidgets import (QMessageBox,
     QDesktopWidget, QDialog,QTableWidgetItem,QWidget)
from view.probabilidad  import Ui_Probabilidad
from .FrecuenciasController import VistaFrecuencia


class VistaProbabilidad(QDialog):
    def __init__(self):
        super(VistaProbabilidad, self).__init__()
        self.vista_Probabilidad = Ui_Probabilidad()
        self.vista_Probabilidad.setupUi(self)

        # centrar ventana
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2),
                  int((screen.height() - size.height())/2))

    def insertTable(self,tabla, QTableWidgetItem,x,y,dato):
        tabla.setItem(x,y, QTableWidgetItem(str(dato)))
    
    def rellenarProbabilidadesAct(self):
        self.view_frecuencias = VistaFrecuencia()
        self.view_frecuencias.InsertDataFrecAct(1)
        self.view_frecuencias.InsertDataFrecAct(2)
        self.view_frecuencias.InsertDataFrecAct(3)
        self.view_frecuencias.InsertDataFrecAct(4)
        self.view_frecuencias.InsertDataFrecAct(5)
        self.view_frecuencias.InsertDataFrecAct(6)
        # haciendo la tabla de probabilidades para cada actividad usando la suavidad de Laplace
        for i in range(3):
            for j in range(3):
                a = self.view_frecuencias.getPosition(i,j)+1
                b = self.view_frecuencias.getPosition(3,j)+3
                res = float(a/b)
                self.insertTable(self.vista_Probabilidad.tabla_pro_act1,QTableWidgetItem,i,j,res)
        #  totales
        self.insertTable(self.vista_Probabilidad.tabla_pro_act1,QTableWidgetItem,3,0,float(
            self.view_frecuencias.getPosition(0,0)+self.view_frecuencias.getPosition(1,0)+
            self.view_frecuencias.getPosition(2,0)
        ))
        self.insertTable(self.vista_Probabilidad.tabla_pro_act1,QTableWidgetItem,3,1,float(
            self.view_frecuencias.getPosition(1,0)+self.view_frecuencias.getPosition(0,1)+
            self.view_frecuencias.getPosition(1,1)
        ))
        self.insertTable(self.vista_Probabilidad.tabla_pro_act1,QTableWidgetItem,3,2,float(
            self.view_frecuencias.getPosition(0,2)+self.view_frecuencias.getPosition(1,2)+
            self.view_frecuencias.getPosition(2,2)
        ))
    
        
   