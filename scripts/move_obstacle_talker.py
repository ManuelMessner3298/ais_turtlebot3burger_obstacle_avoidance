#!/usr/bin/env python

import rospy
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import *

pub_state = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=3)

def set_move_turtlebot3_burger():
    state_turtlebot3_burger = ModelState()
    state_turtlebot3_burger.model_name = 'turtlebot3_burger'
    #pose
    state_turtlebot3_burger.pose.position.x = 0
    state_turtlebot3_burger.pose.position.y = 0
    state_turtlebot3_burger.pose.position.z = 0
    dummy = tf.transformations.quaternion_from_euler(0, 0, -1.5708)
    state_turtlebot3_burger.pose.orientation.x = dummy[0]
    state_turtlebot3_burger.pose.orientation.y = dummy[1]
    state_turtlebot3_burger.pose.orientation.z = dummy[2]
    state_turtlebot3_burger.pose.orientation.w = dummy[3]
    # twist
    state_turtlebot3_burger.twist.linear.x = 0
    state_turtlebot3_burger.twist.linear.y = 0
    state_turtlebot3_burger.twist.linear.z = 0
    state_turtlebot3_burger.twist.angular.x = 0
    state_turtlebot3_burger.twist.angular.y = 0
    state_turtlebot3_burger.twist.angular.z = 0
    pub_state.publish(state_turtlebot3_burger)

def set_move_obstacle(velocity):
    state_obstacle = ModelState()
    state_obstacle.model_name = 'obstacle'
    #pose
    state_obstacle.pose.orientation.x = 0
    state_obstacle.pose.orientation.y = 0
    state_obstacle.pose.orientation.z = 0
    state_obstacle.pose.orientation.w = 1
    state_obstacle.pose.position.x = 0
    state_obstacle.pose.position.y = -35
    state_obstacle.pose.position.z = 0.2
    # twist
    state_obstacle.twist.linear.x = 0
    state_obstacle.twist.linear.y = velocity
    state_obstacle.twist.linear.z = 0
    state_obstacle.twist.angular.x = 0
    state_obstacle.twist.angular.y = 0
    state_obstacle.twist.angular.z = 0
    pub_state.publish(state_obstacle)

def move_obstacle_talker():
    rospy.init_node('move_obstacle_talker', anonymous=True)
    rate = rospy.Rate(0.1) # 0.5hz
    while not rospy.is_shutdown():
        set_move_obstacle(0.2)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_obstacle_talker()
    except rospy.ROSInterruptException:
        pass


