# ais_turtlebot3burger_obstacle_avoidance

this project is developed in Ubuntu 18.04 LTS with ROS melodic, Gazebo11
for installation put the following commands in the terminal:

1. Install gazebo (if not yet installed | http://gazebosim.org/tutorials?tut=install_ubuntu): <br>
    $ curl -sSL http://get.gazebosim.org | sh
2. Instal gazebo_ros: <br>
    $ sudo apt-get install ros-melodic-gazebo-ros
3. Install turtlebot3 packages(https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup): <br>
    $ sudo apt-get install ros-melodic-turtlebot3-msgs <br>
    $ sudo apt-get install ros-melodic-turtlebot3
4. Install teb_local_planner package (http://wiki.ros.org/teb_local_planner): <br>
    $ sudo apt-get install ros-melodic-teb-local-planner
5. Clone this repository in your catkin workspace and build it.
6.	Run the package .launch files.

