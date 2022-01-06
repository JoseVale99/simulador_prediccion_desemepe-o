from PyQt5.QtWidgets import (QMessageBox,
     QDesktopWidget, QDialog)
from view.insertar import Ui_insertar
from models.cargar_datos import CargarDatos,setDatos

class VistaInsertar(QDialog):
    def __init__(self):
        super(VistaInsertar, self).__init__()
        self.vista_insertar = Ui_insertar()
        self.vista_insertar.setupUi(self)

        # centrar ventana
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2),
                  int((screen.height() - size.height())/2))

        
    def insertData(self,tabla, QTableWidgetItem):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.NoIcon)
        self.msg.setText(setDatos(self.vista_insertar.text_act1.text(),
                   self.vista_insertar.text_act2.text(),
                   self.vista_insertar.text_act3.text(),
                   self.vista_insertar.text_act4.text(),
                   self.vista_insertar.text_act5.text(),
                   self.vista_insertar.text_act6.text(),
                   self.vista_insertar.text_estado.text()))
        self.msg.setWindowTitle("Datos cargados")
        self.msg.exec_()
        CargarDatos(tabla,QTableWidgetItem)
        