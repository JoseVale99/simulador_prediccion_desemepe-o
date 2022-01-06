from PyQt5.QtWidgets import (QMessageBox,
     QDesktopWidget, QDialog)
from view.frecuencias  import Ui_Frecuencias
# from models.cargar_datos import CargarDatos,setDatos

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

        
