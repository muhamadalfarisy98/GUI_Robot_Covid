import json
import os
import rospy
from std_msgs.msg import Int32, Float32, String, Bool

#global
listTostr1 = ''

def baca():
    jsonfile_PayloadParam = 'payload.json'
    filename_PayloadParam=os.path.join('/home/faris/Desktop/pyQt/Main_UI',jsonfile_PayloadParam)
    with open(filename_PayloadParam,'r') as f:
        PayloadParam=json.load(f)
                #make sure json file benar
    my_list1=[]
    my_list2=[]
    for p in PayloadParam['kirim']:
    #         #self.tableWidgetPayloadStatus.setItem(baris,0,QtWidgets.QTableWidgetItem(p['No_laci']))
    #         #self.tableWidgetPayloadStatus.setItem(baris,1,QtWidgets.QTableWidgetItem(p['Tujuan']))
        print('No Laci',p['No_laci'])
        print('Tujuan',p['Tujuan'])
        my_list1.append(p['No_laci'])
        my_list2.append(p['Tujuan'])

    print(my_list1)
    print(my_list2)

    # konversi list to string buat di kirim ke ros param

    global listTostr1
    listTostr1= ' '.join([str(elem) for elem in my_list1]) 
    listTostr2= ' '.join([str(elem) for elem in my_list2]) 

    print('String1', listTostr1)
    print('String2', listTostr2)

    my_new_list1=listTostr1.split()
    print('my new list', my_new_list1)
    print(my_new_list1[0])
    print(my_new_list1[1])
    # for i,j in PayloadParam.values():
    #     #self.tableWidgetPayloadStatus.setItem(baris,0,QtWidgets.QTableWidgetItem(p['No_laci']))
    #     #self.tableWidgetPayloadStatus.setItem(baris,1,QtWidgets.QTableWidgetItem(p['Tujuan']))
    #     print(i,j)

def pubString():
    
    pubJson.publish(listTostr1)

if  __name__ == "__main__":
    # os.system('killall roscore &')
    # os.system('roscore &')
    rospy.init_node('publish_json',anonymous=False)
    pubJson=rospy.Publisher('Json_publisher',String,queue_size=10)
    print('masukkan x')
    x=input()
    baca()
    while (x==2):
        pubString()
        print('masukkan x')
        x=input()
