from PyQt5.QtWidgets import (QTableWidgetItem, QApplication,QMainWindow,
     QDesktopWidget,QWidget,QMessageBox)

import sys
from view.index import Ui_MainWindow
from controller.InsertarController import VistaInsertar
from controller.FrecuenciasController import VistaFrecuencia
from controller.ProbabilidadController import VistaProbabilidad
from controller.PredecirController import VistaPredecir
from models.cargar_datos import CargarDatos, getDelete


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.index = Ui_MainWindow()
        self.index.setupUi(self)
        
        # centrar ventana
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2),
                  int((screen.height() - size.height())/2))
        
    # Eventos   
        self.index.btn_insert.clicked.connect(self.show_insert)
        self.index.btn_frecuencia.clicked.connect(self.show_frecuencias)
        self.index.btn_probabilidad.clicked.connect(self.show_Probabilidad)
        self.index.btn_predicir.clicked.connect(self.show_predecir)
        self.index.btn_delete.clicked.connect(self.delete)

        
    # Cargar tablas ----- 
        CargarDatos(self.index.tabla_datos,QTableWidgetItem)
    
    # abrir ventana predecir
    def show_predecir(self):
        self.fom_predecir = QWidget()
        self.view_fom_predecir = VistaPredecir()
        self.view_fom_predecir.vista_pred.setupUi(self.fom_predecir)
        self.view_fom_predecir.vista_pred.btn_pred.clicked.connect(
            lambda: self.view_fom_predecir.buscarProbPosi(
                self.view_fom_predecir.vista_pred.text_act1,
                self.view_fom_predecir.vista_pred.text_act2
            ))
        self.fom_predecir.show()
    
    # abrir ventana probabilidad
    def show_Probabilidad(self):
        self.fom_probabilidad = QWidget()
        self.view_probabilidad = VistaProbabilidad()
        self.view_probabilidad.vista_Probabilidad.setupUi(self.fom_probabilidad)
        self.view_probabilidad.rellenarProbabilidadesAct()
        self.fom_probabilidad.show() 
        
       
         
    # Abrir ventana de frecuencias
    def show_frecuencias(self):
        self.fom_frecuencias = QWidget()
        self.view_frecuencias = VistaFrecuencia()
        self.view_frecuencias.vista_frecuencias.setupUi(self.fom_frecuencias)
        self.view_frecuencias.InsertDataFrecAct(1)
        self.view_frecuencias.InsertDataFrecAct(2)
        self.view_frecuencias.InsertDataFrecAct(3)
        self.view_frecuencias.InsertDataFrecAct(4)
        self.view_frecuencias.InsertDataFrecAct(5)
        self.view_frecuencias.InsertDataFrecAct(6)
        
        self.fom_frecuencias.show() 
        
                
    #  abrir ventana insertar datos
    def show_insert(self): 
        self.fom_insertar = QWidget()
        self.view_insertar = VistaInsertar()
        self.view_insertar.vista_insertar.setupUi(self.fom_insertar)
        self.view_insertar.vista_insertar.btn_guardar.clicked.connect(lambda: self.view_insertar.insertData(self.index.tabla_datos,QTableWidgetItem))
        self.fom_insertar.show() 
    
    def delete(self):
        if len(self.index.tabla_datos.selectedRanges())>0:
            row = self.index.tabla_datos.currentRow()
            current_id = (self.index.tabla_datos.item(row, 0).text())
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.NoIcon)
            self.msg.setText(getDelete(current_id))
            self.msg.setWindowTitle("Datos cargados")
            self.msg.exec_()
            CargarDatos(self.index.tabla_datos,QTableWidgetItem)
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("??Seleciona la fila a eliminar!")
            self.msg.setWindowTitle("Error")
            self.msg.exec_()
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = App()
    my_app.show()
    sys.exit(app.exec_())