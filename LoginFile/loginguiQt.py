# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logingui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.UsernameEdit.setStyleSheet("\n"
"color: rgb(186, 189, 182);")
        self.UsernameEdit.setObjectName("UsernameEdit")
        self.verticalLayout.addWidget(self.UsernameEdit)
        self.PasswordEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PasswordEdit.setStyleSheet("color: rgb(186, 189, 182);")
        self.PasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.verticalLayout.addWidget(self.PasswordEdit)
        self.LoginButton = QtWidgets.QPushButton(LoginForm)
        self.LoginButton.setGeometry(QtCore.QRect(230, 160, 181, 41))
        self.LoginButton.setObjectName("LoginButton")
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

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Authentication Login"))
        self.label.setText(_translate("LoginForm", "Welcome to Mobile Service Robot"))
        self.UsernameEdit.setToolTip(_translate("LoginForm", "<html><head/><body><p>Username</p></body></html>"))
        self.UsernameEdit.setText(_translate("LoginForm", "Username"))
        self.PasswordEdit.setText(_translate("LoginForm", "Password"))
        self.LoginButton.setText(_translate("LoginForm", "Login"))

import new_rc
import test_rc
