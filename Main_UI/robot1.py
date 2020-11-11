# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RobotGUI(object):
    def setupUi(self, RobotGUI):
        RobotGUI.setObjectName("RobotGUI")
        RobotGUI.resize(570, 459)
        self.tabWidget = QtWidgets.QTabWidget(RobotGUI)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 571, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 161, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelPower = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelPower.setObjectName("labelPower")
        self.verticalLayout.addWidget(self.labelPower)
        self.labelIPAddress = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelIPAddress.setObjectName("labelIPAddress")
        self.verticalLayout.addWidget(self.labelIPAddress)
        self.labelPosition = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelPosition.setObjectName("labelPosition")
        self.verticalLayout.addWidget(self.labelPosition)
        self.labelPaylloadType = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelPaylloadType.setObjectName("labelPaylloadType")
        self.verticalLayout.addWidget(self.labelPaylloadType)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 50, 211, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelPowerValue = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelPowerValue.setText("")
        self.labelPowerValue.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPowerValue.setObjectName("labelPowerValue")
        self.verticalLayout_2.addWidget(self.labelPowerValue)
        self.labelIPAddressValue = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelIPAddressValue.setText("")
        self.labelIPAddressValue.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIPAddressValue.setObjectName("labelIPAddressValue")
        self.verticalLayout_2.addWidget(self.labelIPAddressValue)
        self.labelPositionValue = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelPositionValue.setText("")
        self.labelPositionValue.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPositionValue.setObjectName("labelPositionValue")
        self.verticalLayout_2.addWidget(self.labelPositionValue)
        self.labelPayloadValue = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelPayloadValue.setText("")
        self.labelPayloadValue.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPayloadValue.setObjectName("labelPayloadValue")
        self.verticalLayout_2.addWidget(self.labelPayloadValue)
        self.refreshButton = QtWidgets.QPushButton(self.tab_2)
        self.refreshButton.setGeometry(QtCore.QRect(240, 340, 141, 41))
        self.refreshButton.setObjectName("refreshButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.startButton = QtWidgets.QPushButton(self.tab_3)
        self.startButton.setGeometry(QtCore.QRect(180, 140, 201, 101))
        self.startButton.setObjectName("startButton")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(RobotGUI)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(RobotGUI)

    def retranslateUi(self, RobotGUI):
        _translate = QtCore.QCoreApplication.translate
        RobotGUI.setWindowTitle(_translate("RobotGUI", "RobotGUI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("RobotGUI", "Payload Robot"))
        self.labelPower.setText(_translate("RobotGUI", "Baterai Power :"))
        self.labelIPAddress.setText(_translate("RobotGUI", "IP Address :"))
        self.labelPosition.setText(_translate("RobotGUI", "Position:"))
        self.labelPaylloadType.setText(_translate("RobotGUI", "Payload type :"))
        self.refreshButton.setText(_translate("RobotGUI", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("RobotGUI", "Status Monitor"))
        self.startButton.setText(_translate("RobotGUI", "Start Robot ROS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("RobotGUI", "Startup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RobotGUI = QtWidgets.QWidget()
    ui = Ui_RobotGUI()
    ui.setupUi(RobotGUI)
    RobotGUI.show()
    sys.exit(app.exec_())

