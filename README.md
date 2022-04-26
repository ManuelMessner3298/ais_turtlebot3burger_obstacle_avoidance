# ais_turtlebot3burger_obstacle_avoidance

## Installation

The ROS package was developed in Ubuntu 18.04 LTS with ROS melodic and gazebo11. The ROS package has only been tested with this setup, but normally it should also run on other Linux distributions. To install it via the terminal step by step, you have two different options for step 3 (Installing all required dependencies):

Option A: 

&emsp;**1.** Change directory to the src folder of your catkin workspace: <br>
&emsp;&emsp;$ cd ~/path_to_catkin_ws/src <br><br>
&emsp;**2.** Clone this repository in your catkin workspace. <br>
&emsp;&emsp;$ git clone ... # or "gh repo clone ..." #use one of the links of this git repos  <br><br>
&emsp;**3.** Installing all required dependencies: <br><br>
&emsp;&emsp;**OPTION A** (Install all required dependencies via ROS Dependencies): <br><br>
&emsp;&emsp;**3.1** Install all required dependencies via ROS Dependencies (http://wiki.ros.org/rosdep): <br>
&emsp;&emsp;&emsp;$ rosdep install --from-paths src --ignore-src --rosdistro=melodic -y -r <br><br>
&emsp;&emsp;**OPTION B** (Install all required dependencies manually): <br><br>
&emsp;&emsp;**3.1** Install gazebo (if not yet installed | http://gazebosim.org/tutorials?tut=install_ubuntu): <br> 
&emsp;&emsp;&emsp;$ curl -sSL http://get.gazebosim.org | sh <br><br>
&emsp;&emsp;**3.2** Instal gazebo_ros: <br>
&emsp;&emsp;&emsp;$ sudo apt-get install ros-melodic-gazebo11-ros <br>
&emsp;&emsp;&emsp;(in case of gazebo 9: $ sudo apt-get install ros-melodic-gazebo-ros) <br><br>
&emsp;&emsp;**3.3** Install turtlebot3 packages(https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup): <br>
&emsp;&emsp;&emsp;$ sudo apt-get install ros-melodic-turtlebot3-msgs <br>
&emsp;&emsp;&emsp;$ sudo apt-get install ros-melodic-turtlebot3 <br><br>
&emsp;&emsp;**3.4** Install teb_local_planner package (http://wiki.ros.org/teb_local_planner): <br>
&emsp;&emsp;&emsp;$ sudo apt-get install ros-melodic-teb-local-planner <br><br>
&emsp;**4.** Make all python scripts in folder scripts executable (Change permission via chmod): <br>
&emsp;&emsp;$ find ./ais_turtlebot3burger_obstacle_avoidance/scripts -type f -iname "*.py" -exec chmod +x {} \;   <br><br>
&emsp;**5.** Build the catkin workspace. <br><br>
&emsp;**6.** Set the default TURTLEBOT3_MODEL name to burger. <br>
&emsp;&emsp;$ echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc <br><br>
&emsp;**7.** Reopen Terminal or Source ~/.bashrc: <br>
&emsp;&emsp;$ source ~/.bashrc <br><br>
&emsp;**8.** Run the package .launch files. <br><br>
