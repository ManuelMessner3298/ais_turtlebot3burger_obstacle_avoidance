#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import *
from gazebo_msgs.msg import ModelState
from nav_msgs.msg import OccupancyGrid
from time import sleep
import argparse 

width = 1056
height = 384

costmap_data = [0] * width * height

pub_global_costmap = rospy.Publisher('/move_base/global_costmap/costmap', OccupancyGrid , queue_size=3)

def reset_global_costmap():
    O_Grid_global_costmap = OccupancyGrid()
    O_Grid_global_costmap.header.stamp = rospy.Time.now()
    O_Grid_global_costmap.header.frame_id = "/map"
    O_Grid_global_costmap.info.resolution = 0.05
    O_Grid_global_costmap.info.width = 1056
    O_Grid_global_costmap.info.height = 384
    O_Grid_global_costmap.info.origin.position.x = -10.0
    O_Grid_global_costmap.info.origin.position.y = -10.0
    O_Grid_global_costmap.info.origin.position.z = 0.0
    O_Grid_global_costmap.info.origin.orientation.x = 0.0
    O_Grid_global_costmap.info.origin.orientation.y = 0.0
    O_Grid_global_costmap.info.origin.orientation.z = 0.0
    O_Grid_global_costmap.info.origin.orientation.w = 1.0
    O_Grid_global_costmap.data = costmap_data
    pub_global_costmap.publish(O_Grid_global_costmap)


pub_state = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=3)
pub_goal = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=3)

def set_move_obstacle(n, obstacle_speed):
    state_obstacle = ModelState()
    state_obstacle.model_name = 'obstacle'
    #pose
    state_obstacle.pose.orientation.x = 0
    state_obstacle.pose.orientation.y = 0
    state_obstacle.pose.orientation.z = 0
    state_obstacle.pose.orientation.w = 1
    state_obstacle.pose.position.x = 0
    state_obstacle.pose.position.y = -2 - (4*n)
    state_obstacle.pose.position.z = 0.2
    # twist
    state_obstacle.twist.linear.x = 0
    state_obstacle.twist.linear.y = obstacle_speed
    state_obstacle.twist.linear.z = 0
    state_obstacle.twist.angular.x = 0
    state_obstacle.twist.angular.y = 0
    state_obstacle.twist.angular.z = 0
    pub_state.publish(state_obstacle)

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

def collision_validation_movement_periodically_talker(obstacle_speed):
    rospy.init_node('collision_validation_movement_periodically', anonymous=True)
    sleep(5)
    n = 1
    rate = rospy.Rate(0.05) # 20s interval
    while not rospy.is_shutdown():
        send_move_base_goal(4*n, 0, 0)
        # set_move_turtlebot3_burger()
        # reset_global_costmap()
        set_move_obstacle(n, obstacle_speed)
        n = n+1
        rate.sleep()

if __name__ == '__main__':
    try:
        arg_fmt = argparse.ArgumentDefaultsHelpFormatter
        parser = argparse.ArgumentParser(formatter_class=arg_fmt)
        parser.add_argument("-os", "--obstacle_speed", dest="obstacle_speed", default=0.8, type=float, help="Obstacle speed in m/s")
        args = parser.parse_args(rospy.myargv()[1:])

        collision_validation_movement_periodically_talker(args.obstacle_speed)
    except rospy.ROSInterruptException:
        pass

