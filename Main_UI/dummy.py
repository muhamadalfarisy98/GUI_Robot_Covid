import rospy
from std_msgs.msg import Int32, Float32, String

i=0

def main():
    # rospy.init_node('pubCMD',anonymous=False)
    # pubPayloadType=rospy.Publisher('publishCMD',String,queue_size=10)
    # pubPayloadType.publish('hehe')
    global i
    i=i-1
    print(i)
if __name__ == "__main__":
    while True:
        main()