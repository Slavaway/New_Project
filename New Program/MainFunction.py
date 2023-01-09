import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from My_Application import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('')

        

        self.ui.pushButton.clicked.connect(self.Square)
        



    def Square(self):

        a = int(self.ui.lineEdit.text())
        b = int(self.ui.lineEdit_2.text())
        S = a * b
        self.ui.label_6.setText(str(S))

        self.ui.pushButton.clicked.connect(self.Perimeter)

    def Perimeter(self):
        
        a = int(self.ui.lineEdit.text())
        b = int(self.ui.lineEdit_2.text())
        P = 2 * (a + b)
        self.ui.label_7.setText(str(P))
    
        

app = QtWidgets.QApplication([])
application = Window()
application.show()

sys.exit(app.exec())

   
