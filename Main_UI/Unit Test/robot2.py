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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 561, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 100, 461, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(0, 110, 91, 25))
        self.comboBox.setObjectName("comboBox")
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

        #widget connection
        self.refreshButton.clicked.connect(self.refreshaction)
        self.startButton.clicked.connect(self.robotStart)

        #read comboBox
        options1=["Drugs","Foods", "Sprayer"]
        for i in options1 :
            self.comboBox.addItem(i)
      

        options2=["LSKK", "Mekanikal", "Ruang Tugas Akhir"]
        for i in options2 :
            self.comboBox_2.addItem(i)

        #spinbox
        #x=self.spinBox.value()
        self.retranslateUi(RobotGUI)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(RobotGUI)

    def robotStart(self):
        import os
        os.system('roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch')

    def refreshaction(self):
        import socket
        read_combo1=self.comboBox.currentText()
        read_combo2=self.comboBox_2.currentText()
        xstr=str(self.spinBox.value())

        #conversi dari int ke str dulu ntar
        self.labelPowerValue.setText(xstr+"%")
        hostname = socket.gethostname()
        a=[l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        astr=str(a)
        self.labelIPAddressValue.setText(astr)
        self.labelPositionValue.setText(read_combo2)
        self.labelPayloadValue.setText(read_combo1)

    def retranslateUi(self, RobotGUI):
        _translate = QtCore.QCoreApplication.translate
        RobotGUI.setWindowTitle(_translate("RobotGUI", "RobotGUI"))
        self.label.setText(_translate("RobotGUI", "Payload type"))
        self.label_2.setText(_translate("RobotGUI", "No. Laci"))
        self.label_3.setText(_translate("RobotGUI", "Tujuan"))
        self.label_4.setText(_translate("RobotGUI", "Status"))
        self.label_5.setText(_translate("RobotGUI", "Time Stamp"))
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

