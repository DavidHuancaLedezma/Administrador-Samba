from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_ventana_add(object):
    def setupUi(self, ventana_add):
        if not ventana_add.objectName():
            ventana_add.setObjectName(u"ventana_add")
        ventana_add.resize(300, 428)
        self.frame = QFrame(ventana_add)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 300, 428))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 101, 21))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 91, 21))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 121, 21))
        self.input_nombre = QLineEdit(self.frame)
        self.input_nombre.setObjectName(u"input_nombre")
        self.input_nombre.setGeometry(QRect(30, 80, 251, 22))
        self.input_descripcion = QLineEdit(self.frame)
        self.input_descripcion.setObjectName(u"input_descripcion")
        self.input_descripcion.setGeometry(QRect(30, 140, 251, 22))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 170, 81, 21))
        self.radio_printer = QRadioButton(self.frame)
        self.radio_printer.setObjectName(u"radio_printer")
        self.radio_printer.setGeometry(QRect(30, 200, 89, 20))
        self.radio_directory = QRadioButton(self.frame)
        self.radio_directory.setObjectName(u"radio_directory")
        self.radio_directory.setGeometry(QRect(30, 230, 89, 20))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 260, 91, 21))
        self.input_path = QLineEdit(self.frame)
        self.input_path.setObjectName(u"input_path")
        self.input_path.setGeometry(QRect(30, 280, 251, 22))
        self.checkBox_read_only = QCheckBox(self.frame)
        self.checkBox_read_only.setObjectName(u"checkBox_read_only")
        self.checkBox_read_only.setGeometry(QRect(30, 310, 101, 20))
        self.checkBox_inherit_acls = QCheckBox(self.frame)
        self.checkBox_inherit_acls.setObjectName(u"checkBox_inherit_acls")
        self.checkBox_inherit_acls.setGeometry(QRect(30, 330, 101, 20))
        self.checkBox_utilize_btrfs = QCheckBox(self.frame)
        self.checkBox_utilize_btrfs.setObjectName(u"checkBox_utilize_btrfs")
        self.checkBox_utilize_btrfs.setGeometry(QRect(30, 350, 161, 20))
        self.boton_aceptar = QPushButton(self.frame)
        self.boton_aceptar.setObjectName(u"boton_aceptar")
        self.boton_aceptar.setGeometry(QRect(50, 380, 75, 24))
        self.boton_cancelar = QPushButton(self.frame)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setGeometry(QRect(170, 380, 75, 24))

        self.retranslateUi(ventana_add)

        QMetaObject.connectSlotsByName(ventana_add)
    # setupUi

    def retranslateUi(self, ventana_add):
        ventana_add.setWindowTitle(QCoreApplication.translate("ventana_add", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ventana_add", u"Identification", None))
        self.label_2.setText(QCoreApplication.translate("ventana_add", u"Share Name", None))
        self.label_3.setText(QCoreApplication.translate("ventana_add", u"Share Description", None))
        self.label_4.setText(QCoreApplication.translate("ventana_add", u"Share Type", None))
        self.radio_printer.setText(QCoreApplication.translate("ventana_add", u"Printer", None))
        self.radio_directory.setText(QCoreApplication.translate("ventana_add", u"Directory", None))
        self.label_5.setText(QCoreApplication.translate("ventana_add", u"Share Path", None))
        self.checkBox_read_only.setText(QCoreApplication.translate("ventana_add", u"Read-Only", None))
        self.checkBox_inherit_acls.setText(QCoreApplication.translate("ventana_add", u"Inherit acls", None))
        self.checkBox_utilize_btrfs.setText(QCoreApplication.translate("ventana_add", u"Utilize Btrfs Features", None))
        self.boton_aceptar.setText(QCoreApplication.translate("ventana_add", u"Aceptar", None))
        self.boton_cancelar.setText(QCoreApplication.translate("ventana_add", u"Cancelar", None))
    # retranslateUi

