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
from std_msgs.msg import Int32, Float32, String, Bool,UInt8
from rospkg import RosPack
import time
from std_srvs.srv import Trigger
from geometry_msgs.msg import Pose
from service_robot_msgs.msg import command

#variable global
rows=0
stringFile1=''
stringFile2=''
num=0
flag=9

class Ui_RemoteUI(object):
    def setupUi(self, RemoteUI):
        RemoteUI.setObjectName("RemoteUI")
        RemoteUI.resize(596, 452)
        self.tabWidget = QtWidgets.QTabWidget(RemoteUI)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.refreshPayloadButton = QtWidgets.QPushButton(self.tab_2)
        self.refreshPayloadButton.setGeometry(QtCore.QRect(350, 280, 181, 41))
        self.refreshPayloadButton.setObjectName("refreshPayloadButton")
        self.tableWidgetRobotStatus = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidgetRobotStatus.setGeometry(QtCore.QRect(0, 60, 260, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetRobotStatus.sizePolicy().hasHeightForWidth())
        self.tableWidgetRobotStatus.setSizePolicy(sizePolicy)
        self.tableWidgetRobotStatus.setMinimumSize(QtCore.QSize(260, 0))
        self.tableWidgetRobotStatus.setObjectName("tableWidgetRobotStatus")
        self.tableWidgetRobotStatus.setColumnCount(1)
        self.tableWidgetRobotStatus.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRobotStatus.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRobotStatus.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRobotStatus.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRobotStatus.setVerticalHeaderItem(3, item)
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
        """TAG"""
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
        self.refreshRobotButton = QtWidgets.QPushButton(self.tab_2)
        self.refreshRobotButton.setGeometry(QtCore.QRect(40, 280, 181, 41))
        self.refreshRobotButton.setObjectName("refreshRobotButton")
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
        self.refreshPayloadButton.clicked.connect(self.refreshActionPayload)
        self.refreshRobotButton.clicked.connect(self.refreshActionRobot)
        #MAIN WINDOW CMD
        self.retranslateUi(RemoteUI)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(RemoteUI)

    """PUSHBUTTON ACTION"""
    def teleopAction(self):
        self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('Teleoperation Mode'))
        os.system('roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch &')
    def navAction(self):
        self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('Navigation Mode'))
        #ngirim data sama Node commander
    def changeAction(self):
        #Terminate aksi yang sedang berjalan
        self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem(''))

    def refreshModeAction(self):
        #Mengambil info atau subscribe topik dari action yang sedang berjalan
        # rospy.Subscriber('flag_action',UInt8,self.callbackFlagAction)
        # print(flag)
        # if flag==0:
        #     aksi='Idle'
        # elif flag==1:
        #     aksi='Navigation Mode'
        # elif flag==2:
        #     aksi='Teleoperation Mode'
        pesan="""
        Mode Robot:
            0: Idle action
            1: Navigation action
            2: Teleoperation action
            """
        print(pesan)
        # print('aksi robot',aksi)
        # self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem(aksi))
        a=str(self.tableWidgetCekMode.item(0,0).text())
        self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem(a))
        if a=='':
            a='Idle'
        print('On going action : '+a)

    # def callbackFlagAction(self,data):
    #     global flag
    #     flag=data.data

    def refreshActionPayload(self):
        #rate=rospy.Rate(10)
        print('baca JSON ')
        # rospy.Subscriber('Json_Topic',String,self.callbackJsonTopic)
        #rate.sleep()
    def refreshActionRobot(self):
        #ngeload atau subscribe topic dari robot gui dan node commander
        #----Power batre handling
        #subscribe nilai power
        powerValue=str(80)
        self.tableWidgetRobotStatus.setItem(0,0,QtWidgets.QTableWidgetItem(powerValue+"%"))
         #----Position Handling
        #subscribe current position
        positionValue=str('LSKK')
        self.tableWidgetRobotStatus.setItem(1,0,QtWidgets.QTableWidgetItem(positionValue))
        #ROS PARAM SUBSCRIBER
        # rospy.Subscriber('voltage_bat',Float32,self.callbackPower)
        # rospy.Subscriber('status_topic',Bool,self.callbackStatus)

    """CALL-BACK FUNCTION"""
    def callbackJsonTopic(self,data):
        global stringFile1
        z=str(self.tableWidgetRobotStatus.item(3,0).text())
        z_int=int(z)
        print('num di json',z_int)
        stringFile1=data.data
        #parsing jadi list
        my_new_list1=stringFile1.split()
        print('my new list parsing',my_new_list1)
        iter=0
        while iter<z_int*2 :
            self.tableWidgetPayloadStatus.setItem(iter,2,QtWidgets.QTableWidgetItem(str('Pending')))
            if iter<z_int:
                self.tableWidgetPayloadStatus.setItem(iter,0,QtWidgets.QTableWidgetItem(str(my_new_list1[iter])))
                print(my_new_list1[iter])
                iter+=1
                continue
            self.tableWidgetPayloadStatus.setItem(iter-z_int,1,QtWidgets.QTableWidgetItem(str(my_new_list1[iter])))
            print(my_new_list1[iter])
            iter+=1

    # def callbackPower(self,data):
    #     global powerValue
    #     powerValue=data.data
    #     str_pow=str(powerValue)
    #     self.tableWidgetRobotStatus.setItem(0,0,QtWidgets.QTableWidgetItem(str_pow+"%"))

    def callbackPayloadtype(self,data):
        global stringFile2
        global num
        #array[0]: byk items, array[1]:Jenis payload
        stringFile2=data.data
        print('subscribe string',stringFile2)
        my_new_list2=stringFile2.split()
        print('subscribe list',my_new_list2)
        num=my_new_list2[0]
        self.tableWidgetRobotStatus.setItem(3,0,QtWidgets.QTableWidgetItem(str(num) ))
        print('num callbacknya ',num)
        self.tableWidgetRobotStatus.setItem(2,0,QtWidgets.QTableWidgetItem(str(my_new_list2[1])))
        print(my_new_list2)
        self.tableWidgetPayloadStatus.setRowCount(int(num))

    #
    # def callbackStatus(self,data):
    #     global statusRobot
    #     status1=data.data
    #     global rows
    #     #pending dan ongoing aku sendiri
    #     #setiap nerima ini aku konversiin sendiri waktu terima time stampnya
    #     Time=QTime.currentTime()
    #     Timestr=Time.toString(Qt.DefaultLocaleShortDate)
    #     self.tableWidgetPayloadStatus.setItem(rows,3,QtWidgets.QTableWidgetItem(Timestr))
    #     if status1== True:
    #         statusRobot='Done'
    #         self.tableWidgetPayloadStatus.setItem(rows,2,QtWidgets.QTableWidgetItem(statusRobot))
    #     else:
    #         statusRobot='Failed'
    #         self.tableWidgetPayloadStatus.setItem(rows,2,QtWidgets.QTableWidgetItem(statusRobot))
    #     rows=rows+1

    def retranslateUi(self, RemoteUI):
        _translate = QtCore.QCoreApplication.translate
        RemoteUI.setWindowTitle(_translate("RemoteUI", "RemoteUI"))
        self.tabWidget.setToolTip(_translate("RemoteUI", "<html><head/><body><p><br/></p></body></html>"))
        self.refreshPayloadButton.setToolTip(_translate("RemoteUI", "<html><head/><body><p>Update current changes</p></body></html>"))
        self.refreshPayloadButton.setText(_translate("RemoteUI", "Refresh Payload Status"))
        item = self.tableWidgetRobotStatus.verticalHeaderItem(0)
        item.setText(_translate("RemoteUI", "Power"))
        item = self.tableWidgetRobotStatus.verticalHeaderItem(1)
        item.setText(_translate("RemoteUI", "Position"))
        item = self.tableWidgetRobotStatus.verticalHeaderItem(2)
        item.setText(_translate("RemoteUI", "Payload Type"))
        item = self.tableWidgetRobotStatus.verticalHeaderItem(3)
        item.setText(_translate("RemoteUI", "Number of Items"))
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
        self.refreshRobotButton.setText(_translate("RemoteUI", "Refresh Robot Status"))
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
        #INCASE MAU RUN SELf
        # os.system('killall roscore &')
        # os.system('roscore &')
        """INISIALISASI NODE REMOTE GUI"""
        rospy.init_node('remote_ui',anonymous=False)
        rospy.Subscriber('items_topic',String,self.callbackPayloadtype)
        rospy.Subscriber('Json_Topic',String,self.callbackJsonTopic)

#MAIN PROGRAM
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RemoteUI = QtWidgets.QWidget()
    ui = Ui_RemoteUI()
    ui.setupUi(RemoteUI)
    RemoteUI.show()
    sys.exit(app.exec_())
