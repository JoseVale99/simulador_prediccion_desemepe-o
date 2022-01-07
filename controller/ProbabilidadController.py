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
        
        self.view_frecuencias.getProbability(self.view_frecuencias.vista_frecuencias.tabla_fre_act1,
                  self.vista_Probabilidad.tabla_pro_act1, QTableWidgetItem)
        
        #  totales
        self.insertTable(self.vista_Probabilidad.tabla_pro_act1,QTableWidgetItem,3,0,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act1,0,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act1,1,0)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act1,2,0)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act1,QTableWidgetItem,3,1,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act1,1,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act1,0,1)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act1,1,1)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act1,QTableWidgetItem,3,2,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act1,0,2)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act1,1,2)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act1,2,2)))
        
        
        # tabla 2
        self.view_frecuencias.getProbability(self.view_frecuencias.vista_frecuencias.tabla_fre_act2,
                  self.vista_Probabilidad.tabla_pro_act2, QTableWidgetItem)
        #  totales
        self.insertTable(self.vista_Probabilidad.tabla_pro_act2,QTableWidgetItem,3,0,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act2,0,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act2,1,0)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act2,2,0)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act2,QTableWidgetItem,3,1,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act2,1,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act2,0,1)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act2,1,1)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act2,QTableWidgetItem,3,2,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act2,0,2)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act2,1,2)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act2,2,2)))
        	# tabla 2
        self.view_frecuencias.getProbability(self.view_frecuencias.vista_frecuencias.tabla_fre_act2,
                  self.vista_Probabilidad.tabla_pro_act2, QTableWidgetItem)
        #  totales
        self.insertTable(self.vista_Probabilidad.tabla_pro_act2,QTableWidgetItem,3,0,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act2,0,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act2,1,0)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act2,2,0)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act2,QTableWidgetItem,3,1,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act2,1,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act2,0,1)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act2,1,1)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act2,QTableWidgetItem,3,2,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act2,0,2)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act2,1,2)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act2,2,2)))
        # tabla 3
        self.view_frecuencias.getProbability(self.view_frecuencias.vista_frecuencias.tabla_fre_act3,
                  self.vista_Probabilidad.tabla_pro_act3, QTableWidgetItem)
        #  totales
        self.insertTable(self.vista_Probabilidad.tabla_pro_act3,QTableWidgetItem,3,0,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act3,0,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act3,1,0)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act3,2,0)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act3,QTableWidgetItem,3,1,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act3,1,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act3,0,1)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act3,1,1)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act3,QTableWidgetItem,3,2,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act3,0,2)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act3,1,2)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act3,2,2)))
        # tabla 4
        self.view_frecuencias.getProbability(self.view_frecuencias.vista_frecuencias.tabla_fre_act4,
                  self.vista_Probabilidad.tabla_pro_act4, QTableWidgetItem)
        #  totales
        self.insertTable(self.vista_Probabilidad.tabla_pro_act4,QTableWidgetItem,3,0,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act4,0,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act4,1,0)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act4,2,0)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act4,QTableWidgetItem,3,1,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act4,1,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act4,0,1)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act4,1,1)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act4,QTableWidgetItem,3,2,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act4,0,2)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act4,1,2)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act4,2,2)))
        # tabla 5
        self.view_frecuencias.getProbability(self.view_frecuencias.vista_frecuencias.tabla_fre_act5,
                  self.vista_Probabilidad.tabla_pro_act5, QTableWidgetItem)
        #  totales
        self.insertTable(self.vista_Probabilidad.tabla_pro_act5,QTableWidgetItem,3,0,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act5,0,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act5,1,0)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act5,2,0)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act5,QTableWidgetItem,3,1,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act5,1,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act5,0,1)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act5,1,1)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act5,QTableWidgetItem,3,2,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act5,0,2)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act5,1,2)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act5,2,2)))
        # tabla 6
        self.view_frecuencias.getProbability(self.view_frecuencias.vista_frecuencias.tabla_fre_act6,
                  self.vista_Probabilidad.tabla_pro_act6, QTableWidgetItem)
        #  totales
        self.insertTable(self.vista_Probabilidad.tabla_pro_act6,QTableWidgetItem,3,0,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act6,0,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act6,1,0)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act6,2,0)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act6,QTableWidgetItem,3,1,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act6,1,0)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act6,0,1)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act6,1,1)))
        
        self.insertTable(self.vista_Probabilidad.tabla_pro_act6,QTableWidgetItem,3,2,
        float(self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act6,0,2)
        +self.view_frecuencias.getPosition( self.vista_Probabilidad.tabla_pro_act6,1,2)+
        self.view_frecuencias.getPosition(self.vista_Probabilidad.tabla_pro_act6,2,2)))
        
   