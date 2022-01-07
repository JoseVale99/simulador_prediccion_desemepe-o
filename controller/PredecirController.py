from PyQt5.QtWidgets import (QMessageBox,
     QDesktopWidget, QDialog,QTableWidgetItem)
from view.predecir  import Ui_Predecir
from .FrecuenciasController import VistaFrecuencia
from  models.cargar_datos import getDatos
from .ProbabilidadController import VistaProbabilidad

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
        datos = getDatos()
        self.view_frec = VistaFrecuencia()
        si,no = self.view_frec.InsertDataFrecAct(6)
        aPrioriNo = float(no / len(datos));
        aPrioriSi = float(si / len(datos));
        return (aPrioriNo, aPrioriSi)
    
    def buscarProbPosi(self,act1,act2
                    #    ,act3,act4,act5,act6
                       ):
        self.v_p = VistaProbabilidad()
        self.v_p.rellenarProbabilidadesAct()
        aPrioriNo, aPrioriSi = self.probabilidadesAPriori()
        aPostSi = 0.0
        # aPosterioriStringSi = "La cuenta de probabilidad a posterior es: " + str(aPrioriSi)+ " "       
        
        if str(act1.text()).strip().upper() == "A":
            aPostSi  = float(self.v_p.vista_Probabilidad.tabla_pro_act1.item(0,1).text()) 
        elif str(act1.text()).strip().upper() == "NP":
            aPostSi  = float(self.v_p.vista_Probabilidad.tabla_pro_act1.item(1,1).text())
        elif str(act1.text()).strip().upper() == "R":
            aPostSi  = float(self.v_p.vista_Probabilidad.tabla_pro_act1.item(2,1).text())
        else:
            if str(act1.text()).strip().upper() == "NP":
                aPostSi  = float(self.v_p.vista_Probabilidad.tabla_pro_act1.item(1,1).text())
        
        if str(act2.text()).strip().upper() == "A":
            aPostSi  *= float(self.v_p.vista_Probabilidad.tabla_pro_act1.item(0,1).text()) 
        elif str(act2.text()).strip().upper() == "NP":
            aPostSi  *= float(self.v_p.vista_Probabilidad.tabla_pro_act1.item(1,1).text())
        elif str(act2.text()).strip().upper() == "R":
            aPostSi  *= float(self.v_p.vista_Probabilidad.tabla_pro_act1.item(2,1).text())
        else:
            if str(act3.text()).strip().upper() == "NP":
                aPostSi  *= float(self.v_p.vista_Probabilidad.tabla_pro_act1.item(1,1).text())
       
        #  Sacamos el valor final de la probabilidad positiva a Posteriori
        aPostSi  *= aPrioriSi
        self.vista_pred.txt_priori_pos.setText(str(aPostSi))