import rospy
from std_msgs.msg import *

def main():
    #pubNumItems=rospy.Publisher('payloadtype',String,queue_size=10)
    pubNumItems.publish('3')
    pubtype.publish('Drugs')
    pubPower.publish(60.00)
    pubStatus.publish(True)
if __name__ == "__main__":
    rospy.init_node('publisher_node',anonymous=False)
    pubNumItems=rospy.Publisher('numitems',String,queue_size=10)
    pubtype=rospy.Publisher('payloadtype',String,queue_size=10)
    pubPower=rospy.Publisher('voltage_bat',Float32,queue_size=10)
    pubStatus=rospy.Publisher('status_topic',Bool,queue_size=10)
    #main()
    i=0
    print('masukkan input')
    x=input()

    while x==2 :
    
        main()
        print('masukkan input')
        x=input()
        