from PySide6.QtWidgets import QDialog
from vista.ui_ventana_add import Ui_ventana_add
import paramiko
from controlador.recursos_compartidos import RecursosCompartidos
class VentanaAdd(QDialog):
    def __init__(self):
        super(VentanaAdd, self).__init__()
        self.ui = Ui_ventana_add()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.ui.radio_printer.clicked.connect(self.desactivar_componentes)
        self.ui.radio_directory.clicked.connect(self.activar_componentes)
        self.ui.boton_cancelar.clicked.connect(self.cerrar_ventana)
        self.ui.boton_aceptar.clicked.connect(self.guardar_cambios)

    def desactivar_componentes(self):
        self.ui.input_path.setEnabled(False)
        self.ui.checkBox_read_only.setEnabled(False)
        self.ui.checkBox_inherit_acls.setEnabled(False)
    def activar_componentes(self):
        self.ui.input_path.setEnabled(True)
        self.ui.checkBox_read_only.setEnabled(True)
        self.ui.checkBox_inherit_acls.setEnabled(True)


    def guardar_cambios(self):
        nombre = self.ui.input_nombre.text()
        comment = self.ui.input_descripcion.text()

        if self.ui.radio_directory.isChecked():
            path = self.ui.input_path.text()
            read_only = "read only ="
            inherit_acls = "inherit acls ="
            if self.ui.checkBox_read_only.isChecked():
                read_only = read_only + " Yes"
            else:
                read_only = read_only + " No"
        
            if self.ui.checkBox_inherit_acls.isChecked():
                inherit_acls = inherit_acls + " Yes"
            else:
                inherit_acls = inherit_acls + " No"

            comando_nombre = r"sudo sh -c 'echo '[" + nombre + "]' >> /etc/samba/smb.conf'"
            comando_comment = f'sudo sh -c \'echo -e "\\tcomment = {comment}" >> /etc/samba/smb.conf\''
            comando_inherit = f'sudo sh -c \'echo -e "\\t{inherit_acls}" >> /etc/samba/smb.conf\''
            comando_path = f'sudo sh -c \'echo -e "\\tpath = {path}" >> /etc/samba/smb.conf\''
            comando_read_only = f'sudo sh -c \'echo -e "\\t{read_only}" >> /etc/samba/smb.conf\''
            print(comando_comment)

            self.ejecutar_comando(comando_nombre)
            self.ejecutar_comando(comando_comment)
            self.ejecutar_comando(comando_inherit)
            self.ejecutar_comando(comando_path)
            self.ejecutar_comando(comando_read_only)
            self.close()
        else:
            path = "path = /var/tmp"
            printable = "printable = Yes"

            comando_nombre = r"sudo sh -c 'echo '[" + nombre + "]' >> /etc/samba/smb.conf'"
            comando_comment = f'sudo sh -c \'echo -e "\\tcomment = {comment}" >> /etc/samba/smb.conf\''
            comando_path = f'sudo sh -c \'echo -e "\\t{path}" >> /etc/samba/smb.conf\''
            comando_printable = f'sudo sh -c \'echo -e "\\t{printable}" >> /etc/samba/smb.conf\''
    
            self.ejecutar_comando(comando_nombre)
            self.ejecutar_comando(comando_comment)
            self.ejecutar_comando(comando_path)
            self.ejecutar_comando(comando_printable)
            self.close()

    def ejecutar_comando(self,comando):
        try:
            host = ""  # Ingresar tu ip 
            user = ""   # Intresar tu usuario 
            password = ""  # Ingresar tu contraseña 
            cliente = paramiko.SSHClient()
            cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            cliente.connect(host,username=user,password=password)
            stdin, stdout, stderr = cliente.exec_command(comando)

            resultado = stdout.read().decode()
            error = stderr.read().decode()

            cliente.close()

            if error:
                print(error)

            if resultado:
                return resultado

        except Exception as e:
            print("Error SSH:", str(e))
        

    def cerrar_ventana(self):
        self.close()