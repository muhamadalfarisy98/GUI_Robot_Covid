#!/usr/bin/env python
from loginn import Ui_Form
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtCore as qtc 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
# class LoginWindow(qtw.QWidget, Ui_Form):
#     def __init__(self.*args, **kwargs):
#         super().__init__(*args,**kwargs)

#         self.ui=Ui_Form()

#         self.ui.setupUI(self)

#         self.pushButton.clicked.connect(self.authenticate)

#     def authenticate(self):
        
#         username= self.ui.lineEdit.text()
#         password= self.ui.lineEdit_2.text

#         if username == 'user' and password= 'pass':
#             qtw.QMessageBox.information(self,'Success','you are logged in')
#         else:
#             qtw.QMessageBox.critical(self,'Fail','Cannot login')


# if __name__ == "__main__":
#     app = qtw.QApplication([])

#     widget=LoginWindow()
#     widget.show()
#     app.exec_()


class Main(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.authenticate)

    def authenticate(self): 
        username= self.lineEdit_2.text()
        password= self.lineEdit.text()
        if username == 'user' and password== 'pass':
            qtw.QMessageBox.information(self,'Success','you are logged in')
        else:
            qtw.QMessageBox.critical(self,'Fail','Cannot login')

def main():
    app=QApplication(sys.argv)
    winForm=Main()
    winForm.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()