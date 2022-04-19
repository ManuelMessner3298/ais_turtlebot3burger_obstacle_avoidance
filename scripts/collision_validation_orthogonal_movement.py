#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import *
from gazebo_msgs.msg import ModelState
from time import sleep
import argparse 

pub_state = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=3)
pub_goal = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=3)

def set_move_obstacle(obstacle_speed):
    state_obstacle = ModelState()
    state_obstacle.model_name = 'obstacle'
    #pose
    state_obstacle.pose.orientation.x = 0
    state_obstacle.pose.orientation.y = 0
    state_obstacle.pose.orientation.z = 0
    state_obstacle.pose.orientation.w = 1
    state_obstacle.pose.position.x = 9 * obstacle_speed
    state_obstacle.pose.position.y = -2
    state_obstacle.pose.position.z = 0.2
    # twist
    state_obstacle.twist.linear.x = -obstacle_speed
    state_obstacle.twist.linear.y = 0
    state_obstacle.twist.linear.z = 0
    state_obstacle.twist.angular.x = 0
    state_obstacle.twist.angular.y = 0
    state_obstacle.twist.angular.z = 0
    pub_state.publish(state_obstacle)

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

def collision_validation_movement_talker(obstacle_speed):
    rospy.init_node('collision_validation_movement', anonymous=True)
    sleep(5)
    send_move_base_goal(35, 0, 0)
    set_move_obstacle(obstacle_speed)

if __name__ == '__main__':
    try:
        arg_fmt = argparse.ArgumentDefaultsHelpFormatter
        parser = argparse.ArgumentParser(formatter_class=arg_fmt)
        parser.add_argument("-os", "--obstacle_speed", dest="obstacle_speed", default=0.8, type=float, help="Obstacle speed in m/s")
        args = parser.parse_args(rospy.myargv()[1:])

        collision_validation_movement_talker(args.obstacle_speed)
    except rospy.ROSInterruptException:
        pass

