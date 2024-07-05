
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_ventana_editar(object):
    def setupUi(self, ventana_editar):
        if not ventana_editar.objectName():
            ventana_editar.setObjectName(u"ventana_editar")
        ventana_editar.resize(320, 418)
        self.frame = QFrame(ventana_editar)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 321, 421))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tabla = QTableWidget(self.frame)
        if (self.tabla.columnCount() < 2):
            self.tabla.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(50, 30, 202, 221))
        self.boton_editar = QPushButton(self.frame)
        self.boton_editar.setObjectName(u"boton_editar")
        self.boton_editar.setGeometry(QRect(40, 310, 75, 24))
        self.boton_cancelar = QPushButton(self.frame)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setGeometry(QRect(200, 310, 75, 24))

        self.retranslateUi(ventana_editar)

        QMetaObject.connectSlotsByName(ventana_editar)
    # setupUi

    def retranslateUi(self, ventana_editar):
        ventana_editar.setWindowTitle(QCoreApplication.translate("ventana_editar", u"Dialog", None))
        ___qtablewidgetitem = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ventana_editar", u"Option", None));
        ___qtablewidgetitem1 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ventana_editar", u"Value", None));
        self.boton_editar.setText(QCoreApplication.translate("ventana_editar", u"Editar", None))
        self.boton_cancelar.setText(QCoreApplication.translate("ventana_editar", u"Cancelar", None))
    # retranslateUi

