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
from service_robot_msgs.msg import Command

#variable global
rows=0
stringFile1=''
stringFile2=''
num=0
flag=0
flag_tele=1 #default state
kelar=0

class Ui_RemoteUI(object):
    def setupUi(self, RemoteUI):
        RemoteUI.setObjectName("RemoteUI")
        RemoteUI.resize(596, 452)
        self.tabWidget = QtWidgets.QTabWidget(RemoteUI)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
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
        self.refreshRobotButton.setGeometry(QtCore.QRect(210, 310, 181, 41))
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
        self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('Idle Mode'))
        #Widget connection
        self.refreshModeButton.clicked.connect(self.refreshModeAction)
        self.changeButton.clicked.connect(self.changeAction)
        self.navButton.clicked.connect(self.navAction)
        self.teleopButton.clicked.connect(self.teleopAction)
        self.refreshRobotButton.clicked.connect(self.refreshActionRobot)
        #MAIN WINDOW CMD
        self.retranslateUi(RemoteUI)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(RemoteUI)
    """PUSHBUTTON ACTION"""
    def teleopAction(self):
        global flag
        global flag_tele
        print('flag_tele_val',flag_tele)
        if flag==0 and flag_tele==1: #guarding
            self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('Teleoperation Mode'))
            os.system('roslaunch turtlebot3_teleop joystick_control.launch &')
            #time.sleep(0.25)
            #ganti ke packagenya turtleboit twist joy
            print('mode teleop')
            flag=2
        else:
            print('harus kembali ke idle dahulu')
            print('flag ',flag)
            #kasih popup message
            w=str(self.tableWidgetCekMode.item(0,0).text())
            QtWidgets.QMessageBox.critical(None,'Fail',w+' is still running')

    def navAction(self):
        global flag
        global kelar
        stop_nav=str(self.tableWidgetCekMode.item(0,0).text())

        if flag==0 and stop_nav=='Idle Mode' and kelar==0 : #guarding
            self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('Navigation Mode'))
            self.pubChangeAction.publish(1)
            print('mode navigasi')
            flag=1
            #ngirim topic ke robot gui bahwa node navigasi ingin dilakukan pengiriman
        elif flag==0 and stop_nav=='Idle Mode' and kelar==1:
            QtWidgets.QMessageBox.critical(None,'Fail','Harap mengisi kembali item tujuan payload')
        else:
            print('harus kembali ke idle dahulu')
            print('flag ',flag)
            w=str(self.tableWidgetCekMode.item(0,0).text())
            #kasih popup message
            QtWidgets.QMessageBox.critical(None,'Fail',w+' is still running')

    def changeAction(self):
        #Terminate aksi yang sedang berjalan
        global flag
        global flag_tele
        stop_nav=str(self.tableWidgetCekMode.item(0,0).text()) #ngambil kondisi sekarang ditabel sedang apa
        if (stop_nav=='Teleoperation Mode'):
            os.system('rosnode kill teleop_twist_joy &')
            self.pubChangeAction.publish(0)
            self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('Idle Mode'))
            flag_tele=1
            print(stop_nav+' Dimatikan')

        elif (stop_nav=='Navigation Mode'):
        #   mengirim topik ke robot gui bahwa node navigasi ingin dimatikan
            self.pubChangeAction.publish(0)
            self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('Idle Mode'))
            print(stop_nav+' Dimatikan')
        else:
            flag_tele=1
            print('Masih berada di Idle mode')
        #re-state idle mode
        flag=0
    """NOT REALLY NECESSARY BUT CAN BE USED TO REFRESH WINDOW A BIT"""
    def refreshModeAction(self):
        """Mengambil info atau subscribe topik dari action yang sedang berjalan"""
        pesan="""
        Mode Robot:
            0: Idle action
            1: Navigation action
            2: Teleoperation action
            """
        global flag
        print(pesan)
        print(flag)
        stop_nav=str(self.tableWidgetCekMode.item(0,0).text())
        if flag==0 and stop_nav=='Idle Mode':
            self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('Idle Mode'))
        a=str(self.tableWidgetCekMode.item(0,0).text())
        self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem(a))
        print('On going action : '+a)

    def callbackFlagAction(self,data):
        global flag
        global flag_tele
        flag=data.data
        navmode=str(self.tableWidgetCekMode.item(0,0).text())
        if flag==1:
            print('menjalankan navigasi mode')
            self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('Navigation Mode'))
        elif flag==0: #Nilai flag ini hanya mematikan mode navigasi saja tidak teleoperasi
            if navmode=='Navigation Mode':
                print('stop Navigation mode')
                self.tableWidgetCekMode.setItem(0,0,QtWidgets.QTableWidgetItem('Idle Mode'))
            else:
                print('masuk callbackFlagAction')
                flag_tele=0
            #stop dari robot tidak bisa mematikan fungsi node teleop

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
        time.sleep(0.1)


    """CALL-BACK FUNCTION"""
    def callbackKelarKirim(self,data):
        global kelar
        kelar=data.data
        print('subscriber kelar',kelar)

    def callbackStringRT(self,data):
        global string_RT
        z=str(self.tableWidgetRobotStatus.item(3,0).text())
        z_int=int(z)
        list_rt=[]
        string_RT=data.data
        list_rt=string_RT.split()
        print('list parsing ',list_rt)
        indeks=int(list_rt[0])
        print('status:',list_rt[1])
        print('status type:',type(list_rt[1]))
        print('parsing jam:',list_rt[2])
        print('indeks',indeks)
        self.tableWidgetPayloadStatus.setItem(indeks-1,2,QtWidgets.QTableWidgetItem(str(list_rt[1])  ) )
        self.tableWidgetPayloadStatus.setItem(indeks-1,3,QtWidgets.QTableWidgetItem(str(list_rt[2]) ) )
        if indeks<z_int:
            self.tableWidgetPayloadStatus.setItem(indeks,2,QtWidgets.QTableWidgetItem('Ongoing' ) )
        print('parsing realtime data berhasil')

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
        panjang_list=len(my_new_list1)
        print('panjang list update ', panjang_list)
        if (panjang_list/z_int)==2:
            while iter<z_int*2 :
                self.tableWidgetPayloadStatus.setItem(iter,2,QtWidgets.QTableWidgetItem(str('Pending')))
                self.tableWidgetPayloadStatus.setItem(iter,3,QtWidgets.QTableWidgetItem(''))
                if iter<z_int:
                    self.tableWidgetPayloadStatus.setItem(iter,0,QtWidgets.QTableWidgetItem(str(my_new_list1[iter])))
                    print(my_new_list1[iter])
                    iter+=1
                    continue
                self.tableWidgetPayloadStatus.setItem(iter-z_int,1,QtWidgets.QTableWidgetItem(str(my_new_list1[iter])))
                print(my_new_list1[iter])
                iter+=1
            print('selesai parsing data inisial')
        elif (panjang_list/z_int)==4: #kalau udpatean dah kelar
            while iter<z_int*4:
                print('mulai parsing data')
                if iter<z_int:
                    self.tableWidgetPayloadStatus.setItem(iter,0,QtWidgets.QTableWidgetItem(str(my_new_list1[iter])))
                    print(my_new_list1[iter])
                    iter+=1
                    continue
                elif iter<z_int*2 and iter>=z_int:
                    self.tableWidgetPayloadStatus.setItem(iter-z_int,1,QtWidgets.QTableWidgetItem(str(my_new_list1[iter])))
                    print(my_new_list1[iter])
                    iter+=1
                    continue
                elif iter<z_int*3 and iter>=z_int*2:
                    self.tableWidgetPayloadStatus.setItem(iter-z_int*2,2,QtWidgets.QTableWidgetItem(str(my_new_list1[iter])))
                    print(my_new_list1[iter])
                    iter+=1
                    continue
                elif iter>=z_int*3:
                    self.tableWidgetPayloadStatus.setItem(iter-z_int*3,3,QtWidgets.QTableWidgetItem(str(my_new_list1[iter])))
                    print(my_new_list1[iter])
                    iter+=1
            print('selesai parsing data')

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


    def retranslateUi(self, RemoteUI):
        _translate = QtCore.QCoreApplication.translate
        RemoteUI.setWindowTitle(_translate("RemoteUI", "RemoteUI"))
        self.tabWidget.setToolTip(_translate("RemoteUI", "<html><head/><body><p><br/></p></body></html>"))
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
        self.refreshRobotButton.setText(_translate("RemoteUI", "Refresh"))
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
        os.system('roslaunch turtlebot3_bringup gui_monitor.launch &')
        #Init ros subscriber
        rospy.Subscriber('items_topic',String,self.callbackPayloadtype)
        rospy.Subscriber('Json_Topic',String,self.callbackJsonTopic)
        rospy.Subscriber('flag_action',Int32,self.callbackFlagAction)
        rospy.Subscriber('string_RT',String,self.callbackStringRT)
        rospy.Subscriber('kelar_kirim',Int32,self.callbackKelarKirim)
        #init ros publisher
        self.pubChangeAction=rospy.Publisher('change_action',Int32,queue_size=10)
        #if 1 maka navigasi diaktifkan, 0 maka navigasi ingin dihentikan

#MAIN PROGRAM
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RemoteUI = QtWidgets.QWidget()
    ui = Ui_RemoteUI()
    ui.setupUi(RemoteUI)
    RemoteUI.show()
    sys.exit(app.exec_())
