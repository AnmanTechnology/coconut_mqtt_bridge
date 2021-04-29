#!/usr/bin/env python3
import rospy
from std_msgs.msg import UInt8


battey_percent = 100
emergency_state = 0
emergency_pub = rospy.Publisher("emergency_status", UInt8, queue_size=1)


def actuatorStatusCB(msg: UInt8):
    global emergency_state
    emergency_state = (msg.data & 0x08) != 0
    emergency_pub.publish(emergency_state)


if __name__ == "__main__":
    rospy.init_node("coconut_bridge_node")
    rospy.loginfo("Starting coconut_bridge_node.")
    rospy.Subscriber("actuator_status", UInt8, actuatorStatusCB)

    # while not rospy.is_shutdown():
    #     pass
    rospy.spin()
