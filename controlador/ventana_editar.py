from PySide6.QtWidgets import QDialog, QTableWidgetItem
from vista.ui_ventana_editar import Ui_ventana_editar
import paramiko
class VentanaEditar(QDialog):
    def __init__(self,option,nombre_arch_conf):
        super(VentanaEditar, self).__init__()
        self.ui = Ui_ventana_editar()
        self.__option = option #obtenemos todo lo que tiene a partir del []
        self.__nombre_arch_conf = nombre_arch_conf
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.ui.boton_cancelar.clicked.connect(self.cerrar_ventana)
        self.cargar_tabla()
        self.ui.boton_editar.clicked.connect(self.editar_valores)



    def cerrar_ventana(self):
        self.close()
    def cargar_tabla(self):
        filas = self.__option 
        for i, contenido in enumerate(filas):
            self.ui.tabla.insertRow(i)
            self.ui.tabla.setItem(i,0,QTableWidgetItem(contenido[0]))
            self.ui.tabla.setItem(i,1,QTableWidgetItem(contenido[1]))

    def editar_valores(self):
        numero_filas = self.ui.tabla.rowCount()
        comando_eliminar_recurso = "sudo awk '/^\[" +self.__nombre_arch_conf+ "\]/{f=1;next} /^\[/{f=0} !f' /etc/samba/smb.conf > temp && sudo mv temp /etc/samba/smb.conf"
        self.ejecutar_comando(comando_eliminar_recurso)
        row_data = []
        for n_fila in range(numero_filas):

            elemento1 = self.ui.tabla.item(n_fila,0)
            elemento1 = elemento1.text()
            elemento2 = self.ui.tabla.item(n_fila,1)
            elemento2 = elemento2.text()

            nueva_fila = elemento1 + " = " + elemento2
            row_data.append(nueva_fila)

        comando_nombre = r"sudo sh -c 'echo '[" + self.__nombre_arch_conf + "]' >> /etc/samba/smb.conf'"
        self.ejecutar_comando(comando_nombre)
        for insertar in row_data:
            comando_insertar_fila = f'sudo sh -c \'echo -e "\\t{insertar}" >> /etc/samba/smb.conf\''
            self.ejecutar_comando(comando_insertar_fila)
        self.close()
        
    

    
    
    def ejecutar_comando(self, comando):
        try:
            host = ""  # Ingresar tu ip 
            user = ""   # Intresar tu usuario 
            password = ""  # Ingresar tu contraseña 
            cliente = paramiko.SSHClient()
            cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            cliente.connect(host, username=user, password=password)
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
    