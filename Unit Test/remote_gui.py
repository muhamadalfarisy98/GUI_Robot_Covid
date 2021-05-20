#!/usr/bin/env python
# -*- coding: utf-8 -*-
#https://career.catapa.com/GDPLabs/jobs
# Form implementation generated from reading ui file 'MainUI.ui'
# Author: Muhamad Alfarisy (Selasa, 3 November 2020)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QDate,QTime,Qt
from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
import socket
import json
import os
import rospy
from std_msgs.msg import *
from rospkg import RosPack

#variable global
rows=0
stringFile1=''
stringFile2=''
class Ui_RemoteUI(object):
    def setupUi(self, RemoteUI):
        RemoteUI.setObjectName("RemoteUI")
        RemoteUI.resize(596, 452)
        self.tabWidget = QtWidgets.QTabWidget(RemoteUI)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.refreshButton = QtWidgets.QPushButton(self.tab_2)
        self.refreshButton.setGeometry(QtCore.QRect(210, 330, 141, 41))
        self.refreshButton.setObjectName("refreshButton")
        self.tableWidgetRobotStatus = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidgetRobotStatus.setGeometry(QtCore.QRect(0, 80, 260, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetRobotStatus.sizePolicy().hasHeightForWidth())
        self.tableWidgetRobotStatus.setSizePolicy(sizePolicy)
        self.tableWidgetRobotStatus.setMinimumSize(QtCore.QSize(260, 0))
        self.tableWidgetRobotStatus.setObjectName("tableWidgetRobotStatus")
        self.tableWidgetRobotStatus.setColumnCount(1)
        self.tableWidgetRobotStatus.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRobotStatus.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRobotStatus.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRobotStatus.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRobotStatus.setHorizontalHeaderItem(0, item)
        self.tableWidgetRobotStatus.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetRobotStatus.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidgetRobotStatus.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetRobotStatus.verticalHeader().setDefaultSectionSize(40)
        self.tableWidgetRobotStatus.verticalHeader().setMinimumSectionSize(40)
        self.tableWidgetPayloadStatus = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidgetPayloadStatus.setGeometry(QtCore.QRect(270, 60, 311, 192))
        self.tableWidgetPayloadStatus.setObjectName("tableWidgetPayloadStatus")
        self.tableWidgetPayloadStatus.setColumnCount(4)
        self.tableWidgetPayloadStatus.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPayloadStatus.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPayloadStatus.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPayloadStatus.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPayloadStatus.setHorizontalHeaderItem(3, item)
        self.tableWidgetPayloadStatus.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidgetPayloadStatus.verticalHeader().setDefaultSectionSize(30)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(70, 30, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(360, 26, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(140, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.navButton = QtWidgets.QPushButton(self.tab_3)
        self.navButton.setGeometry(QtCore.QRect(30, 80, 221, 61))
        self.navButton.setObjectName("navButton")
        self.teleopButton = QtWidgets.QPushButton(self.tab_3)
        self.teleopButton.setGeometry(QtCore.QRect(330, 80, 231, 61))
        self.teleopButton.setObjectName("teleopButton")
        self.changeButton = QtWidgets.QPushButton(self.tab_3)
        self.changeButton.setGeometry(QtCore.QRect(350, 320, 141, 41))
        self.changeButton.setObjectName("changeButton")
        self.tableWidgetCekMode = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidgetCekMode.setGeometry(QtCore.QRect(130, 230, 351, 61))
        self.tableWidgetCekMode.setObjectName("tableWidgetCekMode")
        self.tableWidgetCekMode.setColumnCount(2)
        self.tableWidgetCekMode.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCekMode.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCekMode.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCekMode.setHorizontalHeaderItem(1, item)
        self.tableWidgetCekMode.horizontalHeader().setDefaultSectionSize(250)
        self.refreshModeButton = QtWidgets.QPushButton(self.tab_3)
        self.refreshModeButton.setGeometry(QtCore.QRect(100, 320, 131, 41))
        self.refreshModeButton.setObjectName("refreshModeButton")
        self.tabWidget.addTab(self.tab_3, "")
        #Widget connection
        self.refreshModeButton.clicked.connect(self.refreshModeAction)
        self.changeButton.clicked.connect(self.changeAction)
        self.navButton.clicked.connect(self.navAction)
        self.teleopButton.clicked.connect(self.teleopAction)
        self.refreshButton.clicked.connect(self.refreshAction)
        #MAIN WINDOW CMD
        self.retranslateUi(RemoteUI)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(RemoteUI)


    """PUSHBUTTON ACTION"""
    def teleopAction(self):
        self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('Teleop Mode'))
        os.system('roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch &')
    def navAction(self):
        self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('Navigasi Mode'))

    def changeAction(self):
        self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('')) 
        
    def refreshModeAction(self):
        #ngambil yang harus dibaca
        print('')
        a=str(self.tableWidgetCekMode.item(0,0).text())
        print(a)
        self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem(a)) 
    
    def refreshAction(self):
        #ngeload atau subscribe topic dari robot gui dan node commander
        self.tableWidgetPayloadStatus.setRowCount(2)
        #----PayLoad Type handling
        #subscribe topic dari robotgui yang tipe payload
        # payLoadReturn=self.comboBoxPayload.currentText()
        # payLoadReturn=payloadtype
        payLoadReturn='Drugs'
        self.tableWidgetRobotStatus.setItem(2,0,QtWidgets.QTableWidgetItem(payLoadReturn))

        #----Power batre handling
        #subscribe nilai power
        powerValue=str(80)
        self.tableWidgetRobotStatus.setItem(0,0,QtWidgets.QTableWidgetItem(powerValue+"%"))

         #----Position Handling
        #subscribe current position
        positionValue=str('LSKK')
        self.tableWidgetRobotStatus.setItem(1,0,QtWidgets.QTableWidgetItem(positionValue))

        #ROS PARAM SUBSCRIBER
        rospy.Subscriber('voltage_bat',Float32,self.callbackPower)
        rospy.Subscriber('status_topic',Bool,self.callbackStatus)
        rospy.Subscriber('payloadtype',String,self.callbackPayloadtype)
        rospy.Subscriber('numitems',String,self.callbackNumitems)
        rospy.Subscriber('Json_NoLaci',String,self.callbackJsonNoLaci)
        rospy.Subscriber('Json_Tujuan',String,self.callbackJsonTujuan)
        # rospy.spin()
    """CALL-BACK FUNCTION"""
    def callbackJsonNoLaci(self,data):
        global stringFile1
        stringFile1=data.data
        my_new_list1=stringFile1.split()
        iter=0
        
        while iter<2 :
            self.tableWidgetPayloadStatus.setItem(iter,0,QtWidgets.QTableWidgetItem(str(my_new_list1[iter])))
            print(my_new_list1[iter])
            iter+=1

    def callbackJsonTujuan(self,data):
        global stringFile2
        stringFile2=data.data
        my_new_list2=stringFile2.split()
        iter=0
        
        while iter<2 :
            self.tableWidgetPayloadStatus.setItem(iter,1,QtWidgets.QTableWidgetItem(str(my_new_list2[iter])))
            print(my_new_list2[iter])
            iter+=1

    def callbackPower(self,data):
        global powerValue  
        powerValue=data.data
        str_pow=str(powerValue)
        self.tableWidgetRobotStatus.setItem(0,0,QtWidgets.QTableWidgetItem(str_pow+"%"))

    def callbackPayloadtype(self,data):
        global typePayload
        typePayload=data.data
        self.tableWidgetRobotStatus.setItem(2,0,QtWidgets.QTableWidgetItem(typePayload))

    def callbackNumitems(self,data):
        global numitems_data
        numitems_data=data.data
        self.tableWidgetPayloadStatus.setRowCount(int(numitems_data))

    def callbackStatus(self,data):   
        global statusRobot
        status1=data.data 
        global rows
        #pending dan ongoing aku sendiri
        #setiap nerima ini aku konversiin sendiri waktu terima time stampnya
        Time=QTime.currentTime()
        Timestr=Time.toString(Qt.DefaultLocaleShortDate)
        self.tableWidgetPayloadStatus.setItem(rows,3,QtWidgets.QTableWidgetItem(Timestr))
        if status1== True:
            statusRobot='Done'
            self.tableWidgetPayloadStatus.setItem(rows,2,QtWidgets.QTableWidgetItem(statusRobot))
        else:
            statusRobot='Failed'
            self.tableWidgetPayloadStatus.setItem(rows,2,QtWidgets.QTableWidgetItem(statusRobot)) 
        rows=rows+1


    def retranslateUi(self, RemoteUI):
        _translate = QtCore.QCoreApplication.translate
        RemoteUI.setWindowTitle(_translate("RemoteUI", "RemoteUI"))
        self.tabWidget.setToolTip(_translate("RemoteUI", "<html><head/><body><p><br/></p></body></html>"))
        self.refreshButton.setToolTip(_translate("RemoteUI", "<html><head/><body><p>Update current changes</p></body></html>"))
        self.refreshButton.setText(_translate("RemoteUI", "Refresh"))
        item = self.tableWidgetRobotStatus.verticalHeaderItem(0)
        item.setText(_translate("RemoteUI", "Power"))
        item = self.tableWidgetRobotStatus.verticalHeaderItem(1)
        item.setText(_translate("RemoteUI", "Position"))
        item = self.tableWidgetRobotStatus.verticalHeaderItem(2)
        item.setText(_translate("RemoteUI", "Payload Type"))
        item = self.tableWidgetRobotStatus.horizontalHeaderItem(0)
        item.setText(_translate("RemoteUI", "Value"))
        item = self.tableWidgetPayloadStatus.horizontalHeaderItem(0)
        item.setText(_translate("RemoteUI", "No.Laci"))
        item = self.tableWidgetPayloadStatus.horizontalHeaderItem(1)
        item.setText(_translate("RemoteUI", "Tujuan"))
        item = self.tableWidgetPayloadStatus.horizontalHeaderItem(2)
        item.setText(_translate("RemoteUI", "Status"))
        item = self.tableWidgetPayloadStatus.horizontalHeaderItem(3)
        item.setText(_translate("RemoteUI", "Timestamp"))
        self.label_8.setText(_translate("RemoteUI", "Robot Status"))
        self.label_9.setText(_translate("RemoteUI", "Payload Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("RemoteUI", "Status Monitor"))
        self.label_3.setText(_translate("RemoteUI", "Remote Mode :"))
        self.navButton.setToolTip(_translate("RemoteUI", "<html><head/><body><p>Mode Navigasi</p><p><br/></p></body></html>"))
        self.navButton.setText(_translate("RemoteUI", "Navigation Mode"))
        self.teleopButton.setToolTip(_translate("RemoteUI", "<html><head/><body><p>Mode Teleoperasi Manual</p></body></html>"))
        self.teleopButton.setText(_translate("RemoteUI", "Teleoperation Mode"))
        self.changeButton.setToolTip(_translate("RemoteUI", "<html><head/><body><p>Stop mode robot yang sedang berjalan</p><p><br/></p></body></html>"))
        self.changeButton.setText(_translate("RemoteUI", "Stop Current Mode"))
        item = self.tableWidgetCekMode.verticalHeaderItem(0)
        item.setText(_translate("RemoteUI", "Current Mode"))
        item = self.tableWidgetCekMode.horizontalHeaderItem(0)
        item.setText(_translate("RemoteUI", "Robot Action"))
        self.refreshModeButton.setText(_translate("RemoteUI", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("RemoteUI", "Remote Action"))
        #lock table widget
        self.tableWidgetPayloadStatus.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetRobotStatus.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetCekMode.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #INCASE MAU RUN
        os.system('killall roscore &')
        os.system('roscore &')
        #INISIALISASI NODE REMOTE GUI
        rospy.init_node('remoteui',anonymous=False)
#MAIN PROGRAM
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RemoteUI = QtWidgets.QWidget()
    ui = Ui_RemoteUI()
    ui.setupUi(RemoteUI)
    RemoteUI.show()
    sys.exit(app.exec_())

