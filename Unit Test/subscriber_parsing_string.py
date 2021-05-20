import json
import os
import rospy
from std_msgs.msg import Int32, Float32, String, Bool

stringFile=''

def callbackJson(data):
    global stringFile
    stringFile=data.data


def main():
    rospy.Subscriber('Json_publisher',String,callbackJson)
    #string to list
    my_new_list1=stringFile.split()
    print(my_new_list1)
    
if __name__ == "__main__":
    rospy.init_node('subscribe_json',anonymous=False)
    print('masukkan x')
    x=input()
    main()
    while (x==2):
        main()
        print('masukkan x')
        x=input()
    