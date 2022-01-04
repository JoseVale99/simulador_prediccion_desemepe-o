from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabla_datos = QtWidgets.QTableWidget(self.frame)
        self.tabla_datos.setRowCount(10)
        self.tabla_datos.setColumnCount(8)
        self.tabla_datos.setObjectName("tabla_datos")
        item = QtWidgets.QTableWidgetItem()
        self.tabla_datos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_datos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_datos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_datos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_datos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_datos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_datos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_datos.setHorizontalHeaderItem(7, item)
        self.verticalLayout_3.addWidget(self.tabla_datos)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_insert = QtWidgets.QPushButton(self.frame_2)
        self.btn_insert.setObjectName("btn_insert")
        self.horizontalLayout.addWidget(self.btn_insert)
        self.btn_delete = QtWidgets.QPushButton(self.frame_2)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.btn_refrescar = QtWidgets.QPushButton(self.frame_2)
        self.btn_refrescar.setObjectName("btn_refrescar")
        self.horizontalLayout.addWidget(self.btn_refrescar)
        self.btn_frecuencia = QtWidgets.QPushButton(self.frame_2)
        self.btn_frecuencia.setObjectName("btn_frecuencia")
        self.horizontalLayout.addWidget(self.btn_frecuencia)
        self.btn_probabilidad = QtWidgets.QPushButton(self.frame_2)
        self.btn_probabilidad.setObjectName("btn_probabilidad")
        self.horizontalLayout.addWidget(self.btn_probabilidad)
        self.btn_predicir = QtWidgets.QPushButton(self.frame_2)
        self.btn_predicir.setObjectName("btn_predicir")
        self.horizontalLayout.addWidget(self.btn_predicir)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tabla de datos de entrenamiento "))
        self.groupBox.setTitle(_translate("MainWindow", "Tabla de datos"))
        item = self.tabla_datos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tabla_datos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Actividad 1"))
        item = self.tabla_datos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Actividad 2"))
        item = self.tabla_datos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Actividad 3"))
        item = self.tabla_datos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Actividad 4"))
        item = self.tabla_datos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Actividad 5"))
        item = self.tabla_datos.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Actividad 6"))
        item = self.tabla_datos.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Aprueba"))
        self.btn_insert.setText(_translate("MainWindow", "Insertar"))
        self.btn_delete.setText(_translate("MainWindow", "Eliminar"))
        self.btn_refrescar.setText(_translate("MainWindow", "refrescar"))
        self.btn_frecuencia.setText(_translate("MainWindow", "Calcular frecuencia"))
        self.btn_probabilidad.setText(_translate("MainWindow", "Calcular Probalidad"))
        self.btn_predicir.setText(_translate("MainWindow", "Predicir"))


