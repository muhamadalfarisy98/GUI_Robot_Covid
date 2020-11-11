# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime, QDate,QTime,Qt
import socket
import rospy
from std_msgs.msg import Int32, Float32, String
from rospkg import RosPack
import json
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
        self.startButton = QtWidgets.QPushButton(self.tab_3)
        self.startButton.setGeometry(QtCore.QRect(190, 160, 201, 101))
        self.startButton.setObjectName("startButton")
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

        #main loop atau diluar class self window
        self.retranslateUi(RobotGUI)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(RobotGUI)

    ##############################fungsi push button##############
    
    def startAction(self):
        os.system('roslaunch turtlebot3_teleop turtlebot3_teleop_key.launchh')
    
    def refreshAction(self):
  
        #----IP Address handling
        a=[l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        astr=str(a)
        self.tableWidgetRobotStatus.setItem(1,0,QtWidgets.QTableWidgetItem(astr))

        #----PayLoad Type handling
        payLoadReturn=self.comboBoxPayload.currentText()
        self.tableWidgetRobotStatus.setItem(3,0,QtWidgets.QTableWidgetItem(payLoadReturn))

        #----Power batre handling
        #subscribe nilai power
        powerValue=str(80)
        self.tableWidgetRobotStatus.setItem(0,0,QtWidgets.QTableWidgetItem(powerValue+"%"))

        #----Position Handling
        #subscribe current position
        positionValue=str('LSKK')
        self.tableWidgetRobotStatus.setItem(2,0,QtWidgets.QTableWidgetItem(positionValue))

        """PAYLOAD STATUS"""
        self.tableWidgetPayloadStatus.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetRobotStatus.setEditTriggers(QAbstractItemView.NoEditTriggers)
        sp_box_int=int(self.spinBoxNumItems.text())
        #---- time handling
        Time=QTime.currentTime()
        Timestr=Time.toString(Qt.DefaultLocaleShortDate)
        
        self.tableWidgetPayloadStatus.setRowCount(sp_box_int)
        #waktu nya kudu diparsing dulu  pokoknya
        for row in range(sp_box_int) :
            self.tableWidgetPayloadStatus.setItem(row,3,QtWidgets.QTableWidgetItem(Timestr))

        #---- status handling
        """
            status nya ada = {Done, ongoing,pending}
            nanti subscire dari status tanda MCU
        """
        status_str=str("Done")
        for row in range(sp_box_int):
            self.tableWidgetPayloadStatus.setItem(row,2,QtWidgets.QTableWidgetItem(status_str))

        #---- No.laci handling
        # nolaci_str=str('1')
        # for row in range(sp_box_int):
        #     self.tableWidgetPayloadStatus.setItem(row,0,QtWidgets.QTableWidgetItem(nolaci_str))

        #---- Tujuan handling
        # tujuan_str=str('lskk')
        # for row in range(sp_box_int):
        #     self.tableWidgetPayloadStatus.setItem(row,1,QtWidgets.QTableWidgetItem(tujuan_str))
        
        # jsonfile_PayloadParam='PayloadSetting.json'
       
        jsonfile_PayloadParam='payload.json'
        filename_PayloadParam=os.path.join('/home/faris/Desktop/pyQt/Main_UI',jsonfile_PayloadParam)
        with open(filename_PayloadParam,'r') as f:
            PayloadParam=json.load(f)
                #make sure json file benar
        baris=0
        for p in PayloadParam['kirim']:
            self.tableWidgetPayloadStatus.setItem(baris,0,QtWidgets.QTableWidgetItem(p['No_laci']))
            self.tableWidgetPayloadStatus.setItem(baris,1,QtWidgets.QTableWidgetItem(p['Tujuan']))
            # print('Name: ' + p['No_laci'])
            # print('Tujuan: ' + p['Tujuan'])
            baris=baris+1

        # print(PayloadParam)
        # self.tableWidgetPayloadStatus.setItem(0,0,QtWidgets.QTableWidgetItem(PayloadParam["No laci"]))
        # self.tableWidgetPayloadStatus.setItem(0,1,QtWidgets.QTableWidgetItem(PayloadParam["Tujuan"]))
        

    def addAction(self):
        #comboBox Read
        cb_payload=self.comboBoxPayload.currentText()
        print(cb_payload)

        #SpinBox
        sp_box=self.spinBoxNumItems.text()
        print(sp_box) #ntar bakal dipakai buat max index rows
        self.tableWidgetTujuan.setRowCount(int(sp_box))
    
    def saveAction(self):
        #Membaca input dari TableWidgetTujuan
        jsonfile_PayloadParam='payload.json'
        filename_PayloadParam=os.path.join('/home/faris/Desktop/pyQt/Main_UI',jsonfile_PayloadParam)
        
        PayloadParam={}
        PayloadParam['kirim']=[]
        my_dict={}
        my_list=[]

        num_rows, num_cols = self.tableWidgetTujuan.rowCount(), self.tableWidgetTujuan.columnCount()
        for row in range(num_rows):
            # gas=self.tableWidgetTujuan.item(row, 0).text()
            # print(gas)
            my_dict['No_laci']=self.tableWidgetTujuan.item(row, 0).text()
            my_dict['Tujuan']=self.tableWidgetTujuan.item(row, 1).text()
            my_list.append(my_dict)
            print(my_list, row)
        PayloadParam['kirim']=my_list
        
        """pengisian input"""
        with open (filename_PayloadParam,'w') as f:
            json.dump(PayloadParam,f)

      
         

        # for row in range (num_rows):
        #     PayloadParam["No laci"].append(self.tableWidgetTujuan.item(row,0).text)


        # assign=[{'hehe':'asda'},{'asd':'91'}]
        # #print(type(assign))
        # for i in assign:
        #     print(assign[i])
    def retranslateUi(self, RobotGUI):
        _translate = QtCore.QCoreApplication.translate
        RobotGUI.setWindowTitle(_translate("RobotGUI", "RobotGUI"))
        self.tabWidget.setToolTip(_translate("RobotGUI", "<html><head/><body><p>Start your robot!</p></body></html>"))
        self.saveButton.setToolTip(_translate("RobotGUI", "<html><head/><body><p>Save Input</p></body></html>"))
        self.saveButton.setText(_translate("RobotGUI", "Save"))
        self.label_10.setText(_translate("RobotGUI", "Payload Type:"))
        self.label_11.setText(_translate("RobotGUI", "Number of items:"))
        self.addButton.setToolTip(_translate("RobotGUI", "<html><head/><body><p>It will add your init value</p></body></html>"))
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
        self.startButton.setText(_translate("RobotGUI", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("RobotGUI", "Startup"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RobotGUI = QtWidgets.QWidget()
    ui = Ui_RobotGUI()
    ui.setupUi(RobotGUI)
    RobotGUI.show()
    sys.exit(app.exec_())

