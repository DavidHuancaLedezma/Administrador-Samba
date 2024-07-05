import sys
from PySide6.QtWidgets import QApplication
from controlador.samba import Samba

def main():
    app = QApplication(sys.argv)
    window = Samba()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()