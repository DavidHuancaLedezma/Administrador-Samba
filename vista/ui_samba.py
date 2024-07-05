
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_Samba(object):
    def setupUi(self, Samba):
        if not Samba.objectName():
            Samba.setObjectName(u"Samba")
        Samba.resize(731, 438)
        self.centralwidget = QWidget(Samba)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 40, 711, 361))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 141, 16))
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 30, 685, 121))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 6px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 171, 16))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.comboBox_configuracion = QComboBox(self.frame_2)
        self.comboBox_configuracion.addItem("")
        self.comboBox_configuracion.addItem("")
        self.comboBox_configuracion.addItem("")
        self.comboBox_configuracion.addItem("")
        self.comboBox_configuracion.addItem("")
        self.comboBox_configuracion.setObjectName(u"comboBox_configuracion")
        self.comboBox_configuracion.setGeometry(QRect(10, 30, 151, 22))
        self.comboBox_configuracion.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"    border:none;\n"
"}")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 60, 91, 16))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.comboBox_servicio_predeterminado = QComboBox(self.frame_2)
        self.comboBox_servicio_predeterminado.addItem("")
        self.comboBox_servicio_predeterminado.addItem("")
        self.comboBox_servicio_predeterminado.setObjectName(u"comboBox_servicio_predeterminado")
        self.comboBox_servicio_predeterminado.setGeometry(QRect(10, 80, 151, 22))
        self.comboBox_servicio_predeterminado.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"    border:none;\n"
"}")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 170, 181, 16))
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 190, 685, 81))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 6px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.checkBox = QCheckBox(self.frame_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QRect(10, 8, 151, 20))
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QRect(170, 10, 101, 24))
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 40, 121, 16))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	border:none;\n"
"}")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 10, 111, 16))
        self.tabla = QTableWidget(self.tab_2)
        if (self.tabla.columnCount() < 6):
            self.tabla.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(20, 30, 661, 151))
        self.boton_add = QPushButton(self.tab_2)
        self.boton_add.setObjectName(u"boton_add")
        self.boton_add.setGeometry(QRect(20, 190, 75, 24))
        self.boton_edit = QPushButton(self.tab_2)
        self.boton_edit.setObjectName(u"boton_edit")
        self.boton_edit.setGeometry(QRect(100, 190, 75, 24))
        self.boton_delete = QPushButton(self.tab_2)
        self.boton_delete.setObjectName(u"boton_delete")
        self.boton_delete.setGeometry(QRect(180, 190, 75, 24))
        self.boton_recargar_tabla = QPushButton(self.tab_2)
        self.boton_recargar_tabla.setObjectName(u"boton_recargar_tabla")
        self.boton_recargar_tabla.setGeometry(QRect(390, 190, 111, 24))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        font = QFont()
        font.setKerning(True)
        self.tab_3.setFont(font)
#if QT_CONFIG(accessibility)
        self.tab_3.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 20, 101, 21))
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(390, 20, 71, 21))
        self.frame_4 = QFrame(self.tab_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(50, 50, 271, 91))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 6px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.nombre_workgroup = QLineEdit(self.frame_4)
        self.nombre_workgroup.setObjectName(u"nombre_workgroup")
        self.nombre_workgroup.setGeometry(QRect(10, 40, 241, 22))
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 181, 16))
        self.label_9.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.frame_5 = QFrame(self.tab_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(390, 50, 271, 91))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	border: 2px solid rgb(170, 170, 170);\n"
"	border-radius: 6px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.radio_server_support = QRadioButton(self.frame_5)
        self.radio_server_support.setObjectName(u"radio_server_support")
        self.radio_server_support.setGeometry(QRect(10, 20, 161, 20))
        self.radio_remote_server = QRadioButton(self.frame_5)
        self.radio_remote_server.setObjectName(u"radio_remote_server")
        self.radio_remote_server.setGeometry(QRect(10, 60, 161, 20))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_11 = QLabel(self.tab_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 10, 101, 16))
        self.tabla_usuarios = QTableWidget(self.tab_4)
        if (self.tabla_usuarios.columnCount() < 1):
            self.tabla_usuarios.setColumnCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        self.tabla_usuarios.setObjectName(u"tabla_usuarios")
        self.tabla_usuarios.setGeometry(QRect(60, 40, 561, 171))
        self.boton_listar_usuarios = QPushButton(self.tab_4)
        self.boton_listar_usuarios.setObjectName(u"boton_listar_usuarios")
        self.boton_listar_usuarios.setGeometry(QRect(30, 250, 75, 24))
        self.boton_delete_usuario = QPushButton(self.tab_4)
        self.boton_delete_usuario.setObjectName(u"boton_delete_usuario")
        self.boton_delete_usuario.setGeometry(QRect(140, 250, 75, 24))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 6, 211, 31))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 733, 440))
        self.frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(220, 217, 235)\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.boton_cancelar = QPushButton(self.frame)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setGeometry(QRect(370, 410, 75, 24))
        self.boton_aceptar = QPushButton(self.frame)
        self.boton_aceptar.setObjectName(u"boton_aceptar")
        self.boton_aceptar.setGeometry(QRect(650, 410, 75, 24))
        Samba.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.tabWidget.raise_()
        self.label.raise_()

        self.retranslateUi(Samba)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Samba)
    # setupUi

    def retranslateUi(self, Samba):
        Samba.setWindowTitle(QCoreApplication.translate("Samba", u"MainWindow", None))
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_2.setText(QCoreApplication.translate("Samba", u"Service Configuration", None))
        self.label_3.setText(QCoreApplication.translate("Samba", u"After writing configuration:", None))
        self.comboBox_configuracion.setItemText(0, QCoreApplication.translate("Samba", u"Start", None))
        self.comboBox_configuracion.setItemText(1, QCoreApplication.translate("Samba", u"Stop", None))
        self.comboBox_configuracion.setItemText(2, QCoreApplication.translate("Samba", u"Restart", None))
        self.comboBox_configuracion.setItemText(3, QCoreApplication.translate("Samba", u"Reload", None))
        self.comboBox_configuracion.setItemText(4, QCoreApplication.translate("Samba", u"Keep current state", None))

        self.label_4.setText(QCoreApplication.translate("Samba", u"After reboot:", None))
        self.comboBox_servicio_predeterminado.setItemText(0, QCoreApplication.translate("Samba", u"Start on boot", None))
        self.comboBox_servicio_predeterminado.setItemText(1, QCoreApplication.translate("Samba", u"Do not start", None))

        self.label_5.setText(QCoreApplication.translate("Samba", u"Firewall Settings for firewalld", None))
        self.checkBox.setText(QCoreApplication.translate("Samba", u"Open Port in Firewall ", None))
        self.pushButton_3.setText(QCoreApplication.translate("Samba", u"Firewall Details...", None))
        self.label_6.setText(QCoreApplication.translate("Samba", u"Firewall is disabled", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Samba", u"Start-Up", None))
        self.label_7.setText(QCoreApplication.translate("Samba", u"Available Shares", None))
        ___qtablewidgetitem = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Samba", u"Status", None));
        ___qtablewidgetitem1 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Samba", u"Read-Only", None));
        ___qtablewidgetitem2 = self.tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Samba", u"Name", None));
        ___qtablewidgetitem3 = self.tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Samba", u"Path", None));
        ___qtablewidgetitem4 = self.tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Samba", u"Guest Acces", None));
        ___qtablewidgetitem5 = self.tabla.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Samba", u"Comment", None));
        self.boton_add.setText(QCoreApplication.translate("Samba", u"Add", None))
        self.boton_edit.setText(QCoreApplication.translate("Samba", u"Edit", None))
        self.boton_delete.setText(QCoreApplication.translate("Samba", u"Delete", None))
        self.boton_recargar_tabla.setText(QCoreApplication.translate("Samba", u"Recargar tabla", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Samba", u"Shares", None))
        self.label_8.setText(QCoreApplication.translate("Samba", u"Base settings", None))
        self.label_10.setText(QCoreApplication.translate("Samba", u"WINS", None))
        self.label_9.setText(QCoreApplication.translate("Samba", u"Workgroup or Domain Name", None))
        self.radio_server_support.setText(QCoreApplication.translate("Samba", u"WINS Server Support", None))
        self.radio_remote_server.setText(QCoreApplication.translate("Samba", u"Remote WINS server", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Samba", u"Identity", None))
        self.label_11.setText(QCoreApplication.translate("Samba", u"Trusted Domains", None))
        ___qtablewidgetitem6 = self.tabla_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Samba", u"USERS", None));
        self.boton_listar_usuarios.setText(QCoreApplication.translate("Samba", u"Listar", None))
        self.boton_delete_usuario.setText(QCoreApplication.translate("Samba", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Samba", u"Trusted Domains", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Samba", u"LDAP Settings", None))
        self.label.setText(QCoreApplication.translate("Samba", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Samba configuration</span></p></body></html>", None))
        self.boton_cancelar.setText(QCoreApplication.translate("Samba", u"Cancel", None))
        self.boton_aceptar.setText(QCoreApplication.translate("Samba", u"OK", None))
    # retranslateUi

