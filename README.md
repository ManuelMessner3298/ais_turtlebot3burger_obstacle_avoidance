# ais_turtlebot3burger_obstacle_avoidance

The ROS package was developed in Ubuntu 18.04 LTS with ROS melodic and gazebo11. The ROS package has only been tested with this setup, but normally it should also run on other Linux distributions. To install it via the terminal, you have two different options:

Option A: 

1. Change directory to the src folder of your catkin workspace:
    $ cd ~/path_to_catkin_ws/src
2. Clone this repository in your catkin workspace.
    $ git clone ... # or "gh repo clone ..." #use one of the links of this git repos 
3. Install all required dependencies via ROS Dependencies (http://wiki.ros.org/rosdep):
    $ rosdep install --from-paths src --ignore-src --rosdistro=melodic -y -r
4. Make all python scripts in folder scripts executable (Change permission via chmod):
    $ find ./ais_turtlebot3burger_obstacle_avoidance/scripts -type f -iname "*.py" -exec chmod +x {} \;  
5. Build the catkin workspace.
6. Set the default TURTLEBOT3_MODEL name to burger.
    $ echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
7. Reopen Terminal or Source ~/.bashrc:
    $ source ~/.bashrc
8. Run the package .launch files.   


Option B (manually install required dependencies): 
1. Install gazebo (if not yet installed | http://gazebosim.org/tutorials?tut=install_ubuntu): <br>
    $ curl -sSL http://get.gazebosim.org | sh
2. Instal gazebo_ros: <br>
    $ sudo apt-get install ros-melodic-gazebo-ros
3. Install turtlebot3 packages(https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup): <br>
    $ sudo apt-get install ros-melodic-turtlebot3-msgs <br>
    $ sudo apt-get install ros-melodic-turtlebot3
4. Install teb_local_planner package (http://wiki.ros.org/teb_local_planner): <br>
    $ sudo apt-get install ros-melodic-teb-local-planner
5. Change directory to the src folder of your catkin workspace:
    $ cd ~/path_to_catkin_ws/src
6. Clone this repository in your catkin workspace.
    $ git clone ... # or "gh repo clone ..." #use one of the links of this git repos 
7. Make all python scripts in folder scripts executable (Change permission via chmod):
    $ find ./ais_turtlebot3burger_obstacle_avoidance/scripts -type f -iname "*.py" -exec chmod +x {} \;  
8. Build the catkin workspace.
9. Set the default TURTLEBOT3_MODEL name to burger.
    $ echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
10. Reopen Terminal or Source ~/.bashrc:
    $ source ~/.bashrc
11. Run the package .launch files.
