# -*- coding: utf-8 -*-
#pyinstaller -w -F -i namaikon.ico namascriptkamu.py
#logingui.ui
#Kamis 14.43 by Faris
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from robotgui import Ui_RobotGUI

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(613, 211)
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setGeometry(QtCore.QRect(120, 10, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(LoginForm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 70, 491, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.UsernameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.UsernameEdit.setStyleSheet("\n""color: rgb(0, 0, 0);")
        self.UsernameEdit.setObjectName("UsernameEdit")
        #setPLaceholde
        # self.PasswordEdit.setPlaceholderText("Masukkan Password")
        # self.UsernameEdit.setPlaceholderText("Masukkan Username")
        
        self.verticalLayout.addWidget(self.UsernameEdit)
        self.PasswordEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PasswordEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.PasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.verticalLayout.addWidget(self.PasswordEdit)
        self.LoginButton = QtWidgets.QPushButton(LoginForm)
        self.LoginButton.setGeometry(QtCore.QRect(230, 160, 181, 41))
        self.LoginButton.setObjectName("LoginButton")
        self.LoginButton.setAutoDefault(True)
        self.gambarROS = QtWidgets.QLabel(LoginForm)
        self.gambarROS.setGeometry(QtCore.QRect(530, 10, 71, 41))
        self.gambarROS.setStyleSheet("background-image: url(:/newPrefix/ros.png);")
        self.gambarROS.setText("")
        self.gambarROS.setPixmap(QtGui.QPixmap(":/newPrefix/ros.png"))
        self.gambarROS.setScaledContents(True)
        self.gambarROS.setObjectName("gambarROS")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(LoginForm)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 70, 91, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gambarUname = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.gambarUname.setStyleSheet("image: url(:/newPrefix/uname1.png);")
        self.gambarUname.setText("")
        self.gambarUname.setObjectName("gambarUname")
        self.verticalLayout_2.addWidget(self.gambarUname)
        self.gambarGembok = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.gambarGembok.setStyleSheet("image: url(:/newPrefix/pass.png);")
        self.gambarGembok.setText("")
        self.gambarGembok.setObjectName("gambarGembok")
        self.verticalLayout_2.addWidget(self.gambarGembok)

        #Widget Connection
        self.LoginButton.clicked.connect(self.auth)
        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Authentication Login"))
        self.label.setText(_translate("LoginForm", "Welcome to Mobile Service Robot"))
        self.UsernameEdit.setToolTip(_translate("LoginForm", "<html><head/><body><p>Username</p></body></html>"))
        # self.UsernameEdit.setText(_translate("LoginForm", "Username"))
        # self.PasswordEdit.setText(_translate("LoginForm", "Password"))
        self.PasswordEdit.setPlaceholderText("Masukkan Password")
        self.UsernameEdit.setPlaceholderText("Masukkan Username")
        self.LoginButton.setText(_translate("LoginForm", "Login"))

    def auth(self):
        # self.PasswordEdit.setPlaceholderText("Masukkan Password")
        # self.UsernameEdit.setPlaceholderText("Masukkan Username")
        username=self.UsernameEdit.text()
        password=self.PasswordEdit.text()

        if username=='faris' and password=='upsquared':
            QtWidgets.QMessageBox.information(None,'Success','you are logged in')
            self.openNewWindow()
        else:
            QtWidgets.QMessageBox.critical(None,'Fail','Please try again!')
            self.PasswordEdit.setText("")
            self.UsernameEdit.setText("")
            self.UsernameEdit.setFocus()
    def openNewWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_RobotGUI() #tinggal ganti nama objek window yang mau dibuka
        self.ui.setupUi(self.window)
        LoginForm.hide() #close previous windows
        self.window.show()

import new_rc
import test_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec_())

