#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
# Author: Muhamad Alfarisy (Selasa, 3 November 2020)
#multi thread ref: https://www.learnpyqt.com/tutorials/multithreading-pyqt-applications-qthreadpool/
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import socket
import json
import os
import rospy
from std_msgs.msg import Int32, Float32, String, Bool,UInt8
from rospkg import RosPack
from std_srvs.srv import Trigger
from geometry_msgs.msg import Pose
from service_robot_msgs.msg import Command #Pose (coordinate) dan Uint8 (data.num)
import time

#Global variable
listTostr1=''
listTostr2=''
status1=False
count=1
status_finish=False
statusRobot=''
remote_nav=1
stopMode=False
kelar=0
saveTujuan=False
changedata=4
#hehe

#CLASS GUI
class Ui_RobotGUI(object):
    def setupUi(self, RobotGUI):
        RobotGUI.setObjectName("RobotGUI")
        RobotGUI.resize(596, 452)
        self.tabWidget = QtWidgets.QTabWidget(RobotGUI)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.saveButton = QtWidgets.QPushButton(self.tab)
        self.saveButton.setGeometry(QtCore.QRect(370, 340, 121, 31))
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 80, 191, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.comboBoxPayload = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBoxPayload.setObjectName("comboBoxPayload")
        self.horizontalLayout_3.addWidget(self.comboBoxPayload)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 150, 191, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.spinBoxNumItems = QtWidgets.QSpinBox(self.horizontalLayoutWidget_4)
        self.spinBoxNumItems.setObjectName("spinBoxNumItems")
        self.horizontalLayout_4.addWidget(self.spinBoxNumItems)
        self.addButton = QtWidgets.QPushButton(self.tab)
        self.addButton.setGeometry(QtCore.QRect(80, 200, 89, 25))
        self.addButton.setObjectName("addButton")
        self.tableWidgetTujuan = QtWidgets.QTableWidget(self.tab)
        self.tableWidgetTujuan.setGeometry(QtCore.QRect(270, 80, 311, 251))
        self.tableWidgetTujuan.setObjectName("tableWidgetTujuan")
        self.tableWidgetTujuan.setColumnCount(2)
        self.tableWidgetTujuan.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetTujuan.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetTujuan.setHorizontalHeaderItem(1, item)
        self.tableWidgetTujuan.horizontalHeader().setDefaultSectionSize(150)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 36, 251, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(280, 40, 281, 17))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.refreshButton = QtWidgets.QPushButton(self.tab_2)
        self.refreshButton.setGeometry(QtCore.QRect(210, 330, 141, 41))
        self.refreshButton.setObjectName("refreshButton")
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
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.initButton = QtWidgets.QPushButton(self.tab_3)
        self.initButton.setGeometry(QtCore.QRect(190, 60, 191, 61))
        self.initButton.setObjectName("initButton")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(150, 250, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 280, 381, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(220, 30, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_3, "")

        #comboBox list
        payLoadListType=["Drugs","Foods","Sprayer"]
        for i in payLoadListType:
            self.comboBoxPayload.addItem(i)

        #WidgetConnection
        self.startButton.clicked.connect(self.startAction)
        self.refreshButton.clicked.connect(self.refreshAction)
        self.addButton.clicked.connect(self.addAction)
        self.saveButton.clicked.connect(self.saveAction)
        self.stopButton.clicked.connect(self.stopAction)
        self.initButton.clicked.connect(self.initAction)

        #Main loop atau diluar class self window
        self.retranslateUi(RobotGUI)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(RobotGUI)

     #############################fungsi push button################
    def initAction(self):
        """INISIASI NODE ROBOT BRINGUP DAN NODE CMD"""
        os.system('roslaunch turtlebot3_bringup covid_robot.launch &')
        print('node bringup sudah terpanggil')
        os.system('roslaunch covid_commander covid_commander.launch &')
        print('node covid_commander sudah terpanggil')

    def startAction(self):
        global count
        global status_finish
        global statusRobot
        global kelar
        global stopMode
        stopMode=False
        sp_box_int=int(self.spinBoxNumItems.text())
        """masuk ke eksekusi"""
        self.pubFlag.publish(1) # indikasi navigasi
        #mengirim ke node commander awal (trigger point)
        # self.initKirim()
        if count==1:
            self.initKirim()
            print('sekuens 1 selesai dikirim')
        elif count!=1:
            #harusnya kalau ditekan start lagi sudah otomatis nilai count nya tersimpan dari nilai counter yang sebelumnya
            print('sekuens '+str(count)+ ' selesai dikirim')
       
        while count<sp_box_int and stopMode==False :
            QApplication.processEvents()  
            #cek flag dari callback
            Time=QTime.currentTime()
            Timestr=Time.toString(Qt.DefaultLocaleShortDate)
            if (status_finish==False):
                continue
            elif (status_finish==True):
                #update di table widget statusnya
                print('sekuens '+ str(count) +' selesai dieksekusi')
                #assign udpate nilai ke tabel
                # Time=QTime.currentTime()
                # Timestr=Time.toString(Qt.DefaultLocaleShortDate)
                """update tabel"""
                self.tableWidgetPayloadStatus.setItem(count-1,2,QtWidgets.QTableWidgetItem(statusRobot)) 
                self.tableWidgetPayloadStatus.setItem(count-1,3,QtWidgets.QTableWidgetItem(Timestr)) 
                #PARSING
                posisi=self.tableWidgetPayloadStatus.item(count,1).text()
                laci=int(self.tableWidgetPayloadStatus.item(count,0).text())
                #PARSING POSISI TO COORDINATE HARDCODE-static
                if  posisi == 'LSKK':
                    kordinat=[1.0,2.0,3.0, 0.0,0.3,0.5,1.0]
                elif posisi == 'Mekanikal':
                    kordinat=[1.0,2.0,3.0, 0.0,0.1,0.7,1.5]
                elif posisi == 'TA':
                    kordinat=[1.0,6.0,2.0, 0.0,0.3,0.5,1.0]
                else:#kalau input dari user ngawur
                    kordinat=[2.0,3.0,5.0, 0.1,0.3,0.5,1.0]
                p=Pose()
                p.position.x=kordinat[0]
                p.position.y=kordinat[1]
                p.position.z=kordinat[2]
                p.orientation.x=kordinat[3]
                p.orientation.y=kordinat[4]
                p.orientation.z=kordinat[5]
                p.orientation.w=kordinat[6]
                #PUBLISH NODE COMMANDER
                custom=Command()
                custom.coordinate=p
                custom.num.data=laci
                self.pubCommander.publish(custom)  
                print('sekuens '+ str(count+1) +' selesai dikirim')
                count+=1
            time.sleep(0.1)
            status_finish=False
            print(count)
        while (count==sp_box_int):    
            if (status_finish==True): 
                print('selesai dikerjakan')
                self.tableWidgetPayloadStatus.setItem(count-1,2,QtWidgets.QTableWidgetItem(statusRobot)) 
                self.tableWidgetPayloadStatus.setItem(count-1,3,QtWidgets.QTableWidgetItem(Timestr)) 
                kelar=1
                break

    def stopAction(self):
        global stopMode
        stopMode=True
        print("Stop action")     
        self.pubFlag.publish(0)
        """NIATNYA NANTI DIA PUBLISH STATUS STOP DAN TERMINATE"""
        #eksperimen service
        # rospy.wait_for_service('cancel_task')
        # try:
        #     xyz=rospy.ServiceProxy('cancel_task', Trigger)
        #     final_val=xyz()
        #     print(final_val.success)
        # except rospy.ServiceException as e:
        #     print(e)

    def refreshAction(self):
        global kelar
        global saveTujuan
        #----IP Address handling
        a=[l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        astr=str(a)
        self.tableWidgetRobotStatus.setItem(1,0,QtWidgets.QTableWidgetItem(astr))

        #----PayLoad Type handling
        payLoadReturn=self.comboBoxPayload.currentText()
        self.tableWidgetRobotStatus.setItem(3,0,QtWidgets.QTableWidgetItem(payLoadReturn))
        """PUBLISH HARUSNYA tipe payload dan number items"""

        #----Power batre handling
        #subscribe nilai power
        powerValue=str(80)
        self.tableWidgetRobotStatus.setItem(0,0,QtWidgets.QTableWidgetItem(powerValue+"%"))

        #----Position Handling
        #subscribe current position
        positionValue=str('LSKK')
        self.tableWidgetRobotStatus.setItem(2,0,QtWidgets.QTableWidgetItem(positionValue))

        """PAYLOAD STATUS"""
        sp_box_int=int(self.spinBoxNumItems.text())

        """WAKTU PARSING"""
        #membuat banyak dimensiinya si diwgetTabel
        self.tableWidgetPayloadStatus.setRowCount(sp_box_int)

        print(kelar)
        if saveTujuan==False:
            if kelar==1:

                print(kelar)
                jsonfile_PayloadParam='payload_finish.json'
                filename_PayloadParam=os.path.join('./',jsonfile_PayloadParam) # bisa diubah menjadi '/'
                PayloadParam={}
                PayloadParam['kirim']=[]
                my_list=[]

                num_rows = self.tableWidgetTujuan.rowCount()
                for row in range(num_rows):
                    my_dict={}
                    my_dict['No_laci']=self.tableWidgetPayloadStatus.item(row, 0).text()
                    my_dict['Tujuan']=self.tableWidgetPayloadStatus.item(row, 1).text()
                    my_dict['Status']=self.tableWidgetPayloadStatus.item(row,2).text()
                    my_dict['Timestamp']=self.tableWidgetPayloadStatus.item(row,3).text()
                    my_list.append(my_dict)
                    print(my_list)
                PayloadParam['kirim']=my_list
                
                """pengisian input"""
                with open (filename_PayloadParam,'w') as f:
                    json.dump(PayloadParam,f)

                with open(filename_PayloadParam,'r') as f:
                    PayloadParam=json.load(f)
                        #make sure json file benar
                baris=0
                for p in PayloadParam['kirim']:
                    self.tableWidgetPayloadStatus.setItem(baris,0,QtWidgets.QTableWidgetItem(p['No_laci']))
                    self.tableWidgetPayloadStatus.setItem(baris,1,QtWidgets.QTableWidgetItem(p['Tujuan']))
                    self.tableWidgetPayloadStatus.setItem(baris,2,QtWidgets.QTableWidgetItem(p['Status']))
                    self.tableWidgetPayloadStatus.setItem(baris,3,QtWidgets.QTableWidgetItem(p['Timestamp']))
                    baris=baris+1
                """PARSING DATA KE REMOTE GUI"""
                my_list1=[]
                my_list2=[]
                my_list3=[]
                my_list4=[]
                for p in PayloadParam['kirim']:
                    print('No Laci',p['No_laci'])
                    print('Tujuan',p['Tujuan'])
                    my_list1.append(p['No_laci'])
                    my_list2.append(p['Tujuan'])
                    my_list3.append(p['Status'])
                    my_list4.append(p['Timestamp'])
                for elemen in my_list2:
                    my_list1.append(elemen)
                for elemen in my_list3:
                    my_list1.append(elemen)
                for elemen in my_list4:
                    my_list1.append(elemen)
                print(my_list1)
                
                # konversi list to string buat di kirim ke ros param
                global listTostr1,listTostr2
                listTostr1= ' '.join([str(elem) for elem in my_list1]) 
                print(listTostr1)

                self.pubJsonTopic.publish(listTostr1)

            elif kelar==0:
                print(kelar)
                #---- status handling
                """
                    status nya ada = {Done, ongoing,pending}
                    nanti subscire dari status tanda MCU
                    inisialisasi semuanya berupa pending
                """
                status_str=str("Pending")
                jsonfile_PayloadParam='payload.json'
                filename_PayloadParam=os.path.join('./',jsonfile_PayloadParam) # bisa diubah menjadi '/'
                for row in range(sp_box_int):
                    self.tableWidgetPayloadStatus.setItem(row,2,QtWidgets.QTableWidgetItem(status_str))
                #Baca File JSON untuk parsing
                with open(filename_PayloadParam,'r') as f:
                    PayloadParam=json.load(f)
                        #make sure json file benar
                baris=0
                for p in PayloadParam['kirim']:
                    self.tableWidgetPayloadStatus.setItem(baris,0,QtWidgets.QTableWidgetItem(p['No_laci']))
                    self.tableWidgetPayloadStatus.setItem(baris,1,QtWidgets.QTableWidgetItem(p['Tujuan']))
                    baris=baris+1
        if saveTujuan==True:
            kelar=0
            if kelar==0:
                print(kelar)
                #---- status handling
                """
                    status nya ada = {Done, ongoing,pending}
                    nanti subscire dari status tanda MCU
                    inisialisasi semuanya berupa pending
                """
                status_str=str("Pending")
                jsonfile_PayloadParam='payload.json'
                filename_PayloadParam=os.path.join('./',jsonfile_PayloadParam) # bisa diubah menjadi '/'
                for row in range(sp_box_int):
                    self.tableWidgetPayloadStatus.setItem(row,2,QtWidgets.QTableWidgetItem(status_str))
                #Baca File JSON untuk parsing
                with open(filename_PayloadParam,'r') as f:
                    PayloadParam=json.load(f)
                        #make sure json file benar
                baris=0
                for p in PayloadParam['kirim']:
                    self.tableWidgetPayloadStatus.setItem(baris,0,QtWidgets.QTableWidgetItem(p['No_laci']))
                    self.tableWidgetPayloadStatus.setItem(baris,1,QtWidgets.QTableWidgetItem(p['Tujuan']))
                    baris=baris+1
        saveTujuan=False


    """CALL-BACK FUNCTION"""
    def callbackStatus(self,data):   
        global status1 #Bool 1,0
        global status_finish #flag callback
        global statusRobot
        status1=data.data
        if status1== True:
            statusRobot='Done'
        else:
            statusRobot='Failed'
        status_finish=True

    def callbackPower(self,data):
        global powerValue  
        powerValue=data.data
        self.tableWidgetRobotStatus.setItem(0,0,QtWidgets.QTableWidgetItem(powerValue+"%"))

    def callbackChangeAction(self,data):
        global changedata
        changedata=data.data 
        print(changedata)
        # global stopMode
        """GUARDING CHANGE DATA VALUE"""

        if changedata==1:
            print('exe 1')
            self.startAction()

        elif changedata==0:
            print('exe 0')
            self.stopAction()
    """CALL-BACK FUNCTION"""    

    def addAction(self):
        #SpinBox
        sp_box=self.spinBoxNumItems.text()
        print(sp_box) #ntar bakal dipakai buat max index rows
        self.tableWidgetTujuan.setRowCount(int(sp_box))
                ########################################
        cb_payload=self.comboBoxPayload.currentText()
        print(cb_payload)

        ###############################ROS PARAM KE REMOTE GUI
        my_items=[]
        my_items.append(sp_box)
        my_items.append(cb_payload)
        listTostr3= ' '.join([str(elem) for elem in my_items]) 
        print('isi list 3', listTostr3)
        self.pubItems.publish(listTostr3)
        ###############################ROS PARAM KE REMOTE GUI
     

    def saveAction(self):
        #Membaca input dari TableWidgetTujuan
        global saveTujuan
        saveTujuan=True
        jsonfile_PayloadParam='payload.json'
        filename_PayloadParam=os.path.join('./',jsonfile_PayloadParam)
        
        PayloadParam={}
        PayloadParam['kirim']=[]
        my_list=[]

        num_rows = self.tableWidgetTujuan.rowCount()
        for row in range(num_rows):
            my_dict={}
            my_dict['No_laci']=self.tableWidgetTujuan.item(row, 0).text()
            my_dict['Tujuan']=self.tableWidgetTujuan.item(row, 1).text()
            my_list.append(my_dict)
            print(my_list)
        PayloadParam['kirim']=my_list
        
        """pengisian input"""
        with open (filename_PayloadParam,'w') as f:
            json.dump(PayloadParam,f)
        
        ############################################################
        with open(filename_PayloadParam,'r') as f:
            PayloadParam=json.load(f)
                #make sure json file benar
        """LIST TO STRING CONVERSION untuk parsing ke remote gui"""
        my_list1=[]
        my_list2=[]
        for p in PayloadParam['kirim']:
            print('No Laci',p['No_laci'])
            print('Tujuan',p['Tujuan'])
            my_list1.append(p['No_laci'])
            my_list2.append(p['Tujuan'])
        for elemen in my_list2:
            my_list1.append(elemen)
        print(my_list1)
        
        # konversi list to string buat di kirim ke ros param
        global listTostr1,listTostr2
        listTostr1= ' '.join([str(elem) for elem in my_list1]) 
        print(listTostr1)

        self.pubJsonTopic.publish(listTostr1)

    def initKirim(self):
        # kordinat=[]
        """ROS PARAMETER PENGIRIMAN STATUS DAN LOKASI ATAUPUN KOORDINAT"""
        posisi=self.tableWidgetPayloadStatus.item(0,1).text()
        laci=int(self.tableWidgetPayloadStatus.item(0,0).text())
        #PARSING POSISI TO COORDINATE HARDCODE-static
        if  posisi == 'LSKK':
            kordinat=[1.0,2.0,3.0, 0.0,0.3,0.5,1.0]
        elif posisi == 'Mekanikal':
            kordinat=[1.0,2.0,3.0, 0.0,0.1,0.7,1.5]
        elif posisi == 'TA':
            kordinat=[1.0,6.0,2.0, 0.0,0.3,0.5,1.0]
        else:
            kordinat=[1.0,6.0,2.0, 0.0,0.3,0.5,1.0]
        p=Pose()
        p.position.x=kordinat[0]
        p.position.y=kordinat[1]
        p.position.z=kordinat[2]
        p.orientation.x=kordinat[3]
        p.orientation.y=kordinat[4]
        p.orientation.z=kordinat[5]
        p.orientation.w=kordinat[6]
        #PUBLISH NODE COMMANDER
        custom=Command()
        custom.coordinate=p
        custom.num.data=laci
        self.pubCommander.publish(custom)

    def retranslateUi(self, RobotGUI):
        _translate = QtCore.QCoreApplication.translate
        RobotGUI.setWindowTitle(_translate("RobotGUI", "RobotGUI"))
        self.tabWidget.setToolTip(_translate("RobotGUI", "<html><head/><body><p><br/></p></body></html>"))
        self.saveButton.setToolTip(_translate("RobotGUI", "<html><head/><body><p>Save Input</p></body></html>"))
        self.saveButton.setText(_translate("RobotGUI", "Save"))
        self.label_10.setText(_translate("RobotGUI", "Payload Type:"))
        self.label_11.setText(_translate("RobotGUI", "Number of items:"))
        self.addButton.setToolTip(_translate("RobotGUI", "<html><head/><body><p>Add to file</p></body></html>"))
        self.addButton.setText(_translate("RobotGUI", "Add"))
        item = self.tableWidgetTujuan.horizontalHeaderItem(0)
        item.setText(_translate("RobotGUI", "No. Laci"))
        item = self.tableWidgetTujuan.horizontalHeaderItem(1)
        item.setText(_translate("RobotGUI", "Tujuan"))
        self.label.setText(_translate("RobotGUI", "1. Masukkan jenis dan jumlah barang"))
        self.label_2.setText(_translate("RobotGUI", "2. Masukkan Tujuan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("RobotGUI", "Payload Robot"))
        self.refreshButton.setToolTip(_translate("RobotGUI", "<html><head/><body><p>Update current changes</p></body></html>"))
        self.refreshButton.setText(_translate("RobotGUI", "Refresh"))
        item = self.tableWidgetRobotStatus.verticalHeaderItem(0)
        item.setText(_translate("RobotGUI", "Power"))
        item = self.tableWidgetRobotStatus.verticalHeaderItem(1)
        item.setText(_translate("RobotGUI", "IP Address"))
        item = self.tableWidgetRobotStatus.verticalHeaderItem(2)
        item.setText(_translate("RobotGUI", "Position"))
        item = self.tableWidgetRobotStatus.verticalHeaderItem(3)
        item.setText(_translate("RobotGUI", "Payload Type"))
        item = self.tableWidgetRobotStatus.horizontalHeaderItem(0)
        item.setText(_translate("RobotGUI", "Value"))
        item = self.tableWidgetPayloadStatus.horizontalHeaderItem(0)
        item.setText(_translate("RobotGUI", "No.Laci"))
        item = self.tableWidgetPayloadStatus.horizontalHeaderItem(1)
        item.setText(_translate("RobotGUI", "Tujuan"))
        item = self.tableWidgetPayloadStatus.horizontalHeaderItem(2)
        item.setText(_translate("RobotGUI", "Status"))
        item = self.tableWidgetPayloadStatus.horizontalHeaderItem(3)
        item.setText(_translate("RobotGUI", "Timestamp"))
        self.label_8.setText(_translate("RobotGUI", "Robot Status"))
        self.label_9.setText(_translate("RobotGUI", "Payload Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("RobotGUI", "Status Monitor"))
        self.initButton.setToolTip(_translate("RobotGUI", "<html><head/><body><p>Inisialisasi Robot </p></body></html>"))
        self.initButton.setText(_translate("RobotGUI", "Init Robot"))
        self.label_3.setText(_translate("RobotGUI", "2. Autonomous Navigation Mode"))
        self.startButton.setToolTip(_translate("RobotGUI", "<html><head/><body><p>Menyalakan fungsi autonomous navigasi robot</p><p><br/></p></body></html>"))
        self.startButton.setText(_translate("RobotGUI", "Start"))
        self.stopButton.setToolTip(_translate("RobotGUI", "<html><head/><body><p>Mematikan fungsi autonomous navigasi robot</p><p><br/></p></body></html>"))
        self.stopButton.setText(_translate("RobotGUI", "Stop"))
        self.label_4.setText(_translate("RobotGUI", "1. Init Robot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("RobotGUI", "Robot Action"))
        #locking widget Tabel
        self.tableWidgetPayloadStatus.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetRobotStatus.setEditTriggers(QAbstractItemView.NoEditTriggers)
    
        #inisialisasi roscore dan clean up pre process
        os.system('killall roscore &')
        time.sleep(2)
        os.system('roscore &')
        """init node rospy GUI robot"""
        #AWALAN
        rospy.init_node('robot_ui',anonymous=False)
        print('masuk init node')
        rospy.Subscriber('status_topic',Bool,self.callbackStatus)
        rospy.Subscriber('voltage_bat',Float32,self.callbackPower)
        rospy.Subscriber('change_action',Int32,self.callbackChangeAction)
        
        print('topik subcriber sudah siap')
        self.pubCommander=rospy.Publisher('command_topic',Command,queue_size=10)
        self.pubFlag=rospy.Publisher('flag_action',Int32,queue_size=10)
        self.pubJsonTopic=rospy.Publisher('Json_Topic',String,queue_size=10)
        self.pubItems=rospy.Publisher('items_topic',String,queue_size=10)
        print('topik publish sudah siap')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RobotGUI = QtWidgets.QWidget()
    ui = Ui_RobotGUI()    
    ui.setupUi(RobotGUI)
    RobotGUI.show()
    sys.exit(app.exec_())

