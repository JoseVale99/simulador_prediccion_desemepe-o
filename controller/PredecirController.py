from PyQt5.QtWidgets import (QMessageBox,
     QDesktopWidget, QDialog,QTableWidgetItem)
from view.predecir  import Ui_Predecir
from .FrecuenciasController import VistaFrecuencia

class VistaPredecir(QDialog):
    def __init__(self):
        super(VistaPredecir, self).__init__()
        self.vista_pred = Ui_Predecir()
        self.vista_pred.setupUi(self)
        self.aPrioriNo = 0.0
        self.aPrioriSi = 0.0
        # centrar ventana
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2),
                  int((screen.height() - size.height())/2))
        
    
    def insertTable(self,tabla, QTableWidgetItem,x,y,dato):
        tabla.setItem(x,y, QTableWidgetItem(str(dato)))
        
    def probabilidadesAPriori(self):
        self.view_frec = VistaFrecuencia()
        a,b = self.view_frec.InsertDataFrecAct(6)
        print('valor de a: ',a)
        print('valor de b: ',b)
    def buscarProbPosi(self,act1,act2,act3,act4,act5,act6):
        aPostSi = 0.0;
        aPosterioriStringSi = "La cuenta de probabilidad a posterior es: " + aPrioriSi + " ";        
    