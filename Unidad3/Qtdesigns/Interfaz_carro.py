
import sys
from PyQt5 import uic, QtWidgets
from os import path

#Inicializa las ventanas
qtCreatorFile = "Interfaz_carro.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile) 

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow): 

    def __init__(self): 
        QtWidgets.QMainWindow.__init__(self) 
        Ui_MainWindow.__init__(self) 
        self.setupUi(self) 
        self.show()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv) 
    window = MyApp() 
    app.exec_()
 
