#!/usr/bin/env python
import rospy
import tf

from geometry_msgs.msg import *

pub_goal = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=3)

def navigation_goal_talker():
    rospy.init_node('navigation_goal_talker', anonymous=True)
    rate = rospy.Rate(1) # 0.1hz
    while not rospy.is_shutdown():
        send_move_base_goal(35, 0, 0)
        rate.sleep()

def send_move_base_goal(posx, posy, rotationz):
    target_pose = PoseStamped()
    target_pose.header.frame_id = "map"
    target_pose.pose.position.x = posx
    target_pose.pose.position.y = posy
    dummy = tf.transformations.quaternion_from_euler(0, 0, rotationz)
    target_pose.pose.orientation.x = dummy[0]
    target_pose.pose.orientation.y = dummy[1]
    target_pose.pose.orientation.z = dummy[2]
    target_pose.pose.orientation.w = dummy[3]
    pub_goal.publish(target_pose)

if __name__ == '__main__':
    try:
        navigation_goal_talker()
    except rospy.ROSInterruptException:
        pass


