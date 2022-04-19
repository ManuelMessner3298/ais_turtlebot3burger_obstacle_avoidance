#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import *
from gazebo_msgs.msg import ModelState
from time import sleep
import argparse 

pub_goal = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=3)

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

def navigation_goal_talker(goal_X, goal_Y, rotation_Z):
    rospy.init_node('navigation_goal_talker', anonymous=True)
    send_move_base_goal(goal_X, goal_Y, rotation_Z)

    rate = rospy.Rate(1) # 0.1hz
    while not rospy.is_shutdown():
        send_move_base_goal(goal_X, goal_Y, rotation_Z)
        rate.sleep()

if __name__ == '__main__':
    try:
        arg_fmt = argparse.ArgumentDefaultsHelpFormatter
        parser = argparse.ArgumentParser(formatter_class=arg_fmt)
        parser.add_argument("-gx", "--goal_X", dest="goal_X", default=4.0, type=float, help="goal_X")
        parser.add_argument("-gy", "--goal_Y", dest="goal_Y", default=1.0, type=float, help="goal_Y")
        parser.add_argument("-rz", "--rotation_Z", dest="rotation_Z", default=0.0, type=float, help="rotation_Z")
        args = parser.parse_args(rospy.myargv()[1:])

        navigation_goal_talker(args.goal_X, args.goal_Y, args.rotation_Z)
    except rospy.ROSInterruptException:
        pass

