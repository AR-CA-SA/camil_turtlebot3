run 
$ colcon build --symlink-install 
every time you build a new package 

then run 


$ source install/local_setup.bash

all of this must be done on the root ("camil_turtlebot3")

when opening vsCode for the first time, run the following command 
$ source /opt/ros/jazzy/setup.bash
on the terminal where vsCode will be open


-----------

colcon build --symlink-install
source install/local_setup.ba
ros2 run control maze

------