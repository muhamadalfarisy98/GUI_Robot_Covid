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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setStyleSheet("\n"
"color: rgb(186, 189, 182);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setStyleSheet("color: rgb(186, 189, 182);")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(LoginForm)
        self.pushButton.setGeometry(QtCore.QRect(230, 160, 181, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(LoginForm)
        self.label_4.setGeometry(QtCore.QRect(530, 10, 71, 41))
        self.label_4.setStyleSheet("background-image: url(:/newPrefix/ros.png);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/ros.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(LoginForm)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 70, 91, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setStyleSheet("image: url(:/newPrefix/uname1.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setStyleSheet("image: url(:/newPrefix/pass.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.label.setText(_translate("LoginForm", "Welcome to Mobile Service Robot"))
        self.lineEdit_2.setToolTip(_translate("LoginForm", "<html><head/><body><p>Username</p></body></html>"))
        self.lineEdit_2.setText(_translate("LoginForm", "Username"))
        self.lineEdit.setText(_translate("LoginForm", "Password"))
        self.pushButton.setText(_translate("LoginForm", "Login"))

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

