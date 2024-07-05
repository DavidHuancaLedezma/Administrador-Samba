from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from vista.ui_samba import Ui_Samba
import paramiko
from controlador.recursos_compartidos import RecursosCompartidos
from controlador.ventana_add import VentanaAdd
from controlador.ventana_editar import VentanaEditar
class Samba(QMainWindow):
    def __init__(self):
        super(Samba, self).__init__()
        self.ui = Ui_Samba()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.ui.boton_cancelar.clicked.connect(self.cerrar_ventana)
        self.ui.boton_aceptar.clicked.connect(self.tab_actual)
        self.ui.boton_add.clicked.connect(self.abrir_ventana_add)
        self.ui.boton_delete.clicked.connect(self.eliminar_recursos)
        self.ui.boton_recargar_tabla.clicked.connect(self.recargar_tabla)
        self.ui.boton_edit.clicked.connect(self.abrir_ventana_editar)
        self.ui.boton_listar_usuarios.clicked.connect(self.listar_usuarios)
        self.ui.boton_delete_usuario.clicked.connect(self.eliminar_usuarios)
        self.cargar_nombre_workgroup()
        self.cargar_tabla()

    def tab_actual(self):
        posicion_actual = self.ui.tabWidget.currentIndex()
        if posicion_actual == 0:
            self.configurar_servicio()
        elif posicion_actual == 1:
            QMessageBox.information(self,"Shares","Modificación exitosa")
        elif posicion_actual == 2:
            self.configurar_identity()
        elif posicion_actual == 3:
            QMessageBox.information(self,"usuarios","Modificación exitosa")
        elif posicion_actual == 4:
            pass
    
    def listar_usuarios(self):
        self.ui.tabla_usuarios.setRowCount(0) # elimina todas las filas de la tabla
        comando_listar = "sudo pdbedit -L"
        usuarios = self.ejecutar_comando(comando_listar)
        usuarios = usuarios.split("\n")
        usuarios = usuarios[:-1]
        for i, usuario in enumerate(usuarios):
            self.ui.tabla_usuarios.insertRow(i)
            self.ui.tabla_usuarios.setItem(i,0,QTableWidgetItem(usuario))

    def eliminar_usuarios(self):
        
        fila_seleccionada = self.ui.tabla_usuarios.selectedItems()
        index_fila = fila_seleccionada[0].row()
        nombre_usuario = self.ui.tabla_usuarios.item(index_fila,0)
        nombre_usuario = nombre_usuario.text()
        nombre = ""
        for i in nombre_usuario:
            if i != ":":
                nombre += i
            else:
                break

        comando_eliminar_usuarios = "sudo pdbedit -x " + nombre
        self.ejecutar_comando(comando_eliminar_usuarios)
        self.ui.tabla_usuarios.removeRow(index_fila)

    def configurar_servicio(self):
        opcion_elegida = self.ui.comboBox_configuracion.currentText().lower()
        opcion_elegida2 = self.ui.comboBox_servicio_predeterminado.currentText().lower()
        comando = ""
        comando2 = ""
        if opcion_elegida == "start":
            comando = "sudo /usr/sbin/service smb start"
        elif opcion_elegida == "stop":
            comando = "sudo /usr/sbin/service smb stop"
        elif opcion_elegida == "restart":
            comando = "sudo /usr/sbin/service smb restart"
        elif opcion_elegida == "reload":
            comando = "sudo /usr/sbin/service smb reload"
        elif opcion_elegida == "keep current state":
            comando = ""

        if opcion_elegida2 == "start on boot":
            comando2 = "sudo systemctl enable smb"
        elif opcion_elegida2 == "do not start":
            comando2 = "sudo systemctl disable smb"
        
        self.ejecutar_comando(comando)
        self.ejecutar_comando(comando2)

        QMessageBox.information(self,"Start up","Cambios realizados con exito")

    def cargar_nombre_workgroup(self):
        comando_para_obtener_nombre = "grep -i '^\s*workgroup\s*=' /etc/samba/smb.conf | sed 's/^\s*workgroup\s*=\s*//' | tr -d ' '"
        workgroup = self.ejecutar_comando(comando_para_obtener_nombre)
        workgroup = workgroup[:-1]
        self.ui.nombre_workgroup.setText(workgroup)

    def configurar_identity(self):
        nuevo_workgroup = self.ui.nombre_workgroup.text()
        comando_para_modificar_workgroup = "sudo sed -i 's/^\s*workgroup\s*=.*/\tworkgroup = " + nuevo_workgroup + "/' /etc/samba/smb.conf"
        self.ejecutar_comando(comando_para_modificar_workgroup)


        if self.ui.radio_remote_server.isChecked():
            comando_nueva_fila = r"sudo sed -i '/^\[global\]/,/wins support = Yes/ s/wins support = Yes/&\n\twins server =/' /etc/samba/smb.conf"
            cambiar_permiso_wins_support_a_no = "sudo sed -i 's/^\s*wins support\s*=.*/\twins support = No/' /etc/samba/smb.conf"
            comando_verificar_duplicados = "grep -q 'wins server =' /etc/samba/smb.conf && echo 'true' || echo 'false'"

            duplicado = self.ejecutar_comando(comando_verificar_duplicados)
            duplicado = duplicado[:-1]
            if duplicado == "false":
                self.ejecutar_comando(comando_nueva_fila)

            self.ejecutar_comando(cambiar_permiso_wins_support_a_no)

        if self.ui.radio_server_support.isChecked():
            eliminar_wins_server = "sudo sed -i '/wins server/d' /etc/samba/smb.conf"
            cambiar_permiso_wins_support_a_yes = "sudo sed -i 's/^\s*wins support\s*=.*/\twins support = Yes/' /etc/samba/smb.conf"
            self.ejecutar_comando(eliminar_wins_server)
            self.ejecutar_comando(cambiar_permiso_wins_support_a_yes)

        QMessageBox.information(self,"Identity","Modificación exitosa")

    

    def cargar_tabla(self):

        filas = []

        comando_get_nombres_de_recursos = r"grep '^\[' /etc/samba/smb.conf | sed 's/[\[\]]//g'"
        nombres_de_recursos = self.ejecutar_comando(comando_get_nombres_de_recursos)
        nombres_de_recursos = nombres_de_recursos.split("\n")
        nombres_de_recursos.pop(len(nombres_de_recursos)-1)
        nombres_de_recursos.pop(0)

        for recurso in nombres_de_recursos:
            recurso = recurso[:-1]
            recurso = recurso[1:]

            if recurso[len(recurso)-1] == "$":
                recurso = recurso[:-1]
                recurso = recurso + "\$" 

            get_comment = r"awk '/\[" +recurso+ "\]/{flag=1;next} /^\[/{flag=0} flag {print}' /etc/samba/smb.conf | grep '^\s*comment\s*=' | sed 's/^\s*comment\s*=\s*//'"
            get_path = r"awk '/\[" +recurso+ "\]/{flag=1;next} /^\[/{flag=0} flag {print}' /etc/samba/smb.conf | grep '^\s*path\s*=' | sed 's/^\s*path\s*=\s*//'"
            get_read_only = r"awk '/\[" +recurso+ "\]/{flag=1;next} /^\[/{flag=0} flag {print}' /etc/samba/smb.conf | grep '^\s*read only\s*=' | sed 's/^\s*read only\s*=\s*//'"

            comment = self.ejecutar_comando(get_comment)
            path = self.ejecutar_comando(get_path)
            read_only = self.ejecutar_comando(get_read_only)
            
            if recurso[len(recurso)-1] == "$":
                recurso = recurso[:-1]
                recurso = recurso[:-1]
                recurso = recurso + "$"
            
            if comment == None:
                comment = ""
            if path == None:
                path = ""
            if read_only == None:
                read_only = ""
            if len(comment)>0:
                comment = comment[:-1]
            if len(path)>0:
                path = path[:-1]
            if len(read_only)>0:
                read_only = read_only[:-1]
            
            filas.append(RecursosCompartidos("Enable", read_only, recurso, path, "No", comment))
        
        for i, contenido in enumerate(filas):
            self.ui.tabla.insertRow(i)
            self.ui.tabla.setItem(i,0,QTableWidgetItem(contenido.get_status()))
            self.ui.tabla.setItem(i,1,QTableWidgetItem(contenido.get_read_only()))
            self.ui.tabla.setItem(i,2,QTableWidgetItem(contenido.get_name()))
            self.ui.tabla.setItem(i,3,QTableWidgetItem(contenido.get_path()))
            self.ui.tabla.setItem(i,4,QTableWidgetItem(contenido.get_guest_acces()))
            self.ui.tabla.setItem(i,5,QTableWidgetItem(contenido.get_comment()))



    def eliminar_recursos(self):
        
        fila_seleccionada = self.ui.tabla.selectedItems()
        index_fila = fila_seleccionada[0].row()
        row_data = []
        for col in range(self.ui.tabla.columnCount()):
            elemento = self.ui.tabla.item(index_fila,col)
            row_data.append(elemento.text())
        nombre = row_data[2]
        comando_eliminar_recurso = "sudo awk '/^\[" +nombre+ "\]/{f=1;next} /^\[/{f=0} !f' /etc/samba/smb.conf > temp && sudo mv temp /etc/samba/smb.conf"
        self.ejecutar_comando(comando_eliminar_recurso)
        self.ui.tabla.removeRow(index_fila)
    
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

    def abrir_ventana_add(self):
        self.ventana = VentanaAdd()
        self.ventana.exec()
    
    def abrir_ventana_editar(self):
        fila_seleccionada = self.ui.tabla.selectedItems()
        index_fila = fila_seleccionada[0].row()
        row_data = []
        for col in range(self.ui.tabla.columnCount()):
            elemento = self.ui.tabla.item(index_fila,col)
            row_data.append(elemento.text())
        nombre = row_data[2]

        
        comando_option = "awk '/\[" + nombre +"\]/ {flag=1; next} /^\[/ {flag=0} flag {print}' /etc/samba/smb.conf"
        option = self.ejecutar_comando(comando_option)
        option = option.split("\n")
        option = option[:-1]
        for i, contenido in enumerate(option):
            option[i] = contenido[1:]
        
        for i, contenido in enumerate(option):
            contenido = contenido.split("=")
            option[i] = contenido

        for i, filas in enumerate(option):
            option[i][0] = filas[0][:-1]
            option[i][1] = filas[1][1:]

        self.ventana_editar = VentanaEditar(option,nombre)
        self.ventana_editar.exec()

    def recargar_tabla(self):
        self.ui.tabla.setRowCount(0)
        self.cargar_tabla()