from PyQt5 import QtWidgets
from UIMainWindow import MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    appMainWindow = MainWindow()
    appMainWindow.show()
    sys.exit(app.exec_())
