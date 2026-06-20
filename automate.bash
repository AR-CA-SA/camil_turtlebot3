#!/bin/bash


colcon build --symlink-install
source install/local_setup.bash
ros2 run control maze