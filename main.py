from PyQt5.QtWidgets import (QTableWidgetItem, QApplication,QMainWindow,
     QDesktopWidget,QWidget)
import sys
from view.index import Ui_MainWindow
from controller.InsertarController import VistaInsertar
from models.cargar_datos import CargarDatos

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
    # Cargar tablas ----- 
        CargarDatos(self.index.tabla_datos,QTableWidgetItem)
        #  abrir ventada insertar datos
    def show_insert(self): 
        self.fom_insertar = QWidget() 
        self.view_insertar = VistaInsertar()
        self.view_insertar.vista_insertar.setupUi(self.fom_insertar)
        self.fom_insertar.show()        
        
                      
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = App()
    my_app.show()
    sys.exit(app.exec_())