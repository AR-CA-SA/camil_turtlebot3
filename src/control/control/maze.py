import numpy as np
import matplotlib.pyplot as plt
import rclpy
from rclpy.node import Node
from matplotlib.animation import FuncAnimation

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import TwistStamped


import threading 


fig, ax = plt.subplots()

class MazeNode(Node):
    def __init__(self):
        self.msgTwist = None
        self.msgLaser = None
        super().__init__("maze_node")
        self.subscription = self.create_subscription(LaserScan, '/scan', self.listener_callback, 
         10)
        self.publisher_ = self.create_publisher(TwistStamped, 'cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.publish_transformations)
        self.i = 0
    def publish_transformations(self):
        self.msgTwist = TwistStamped()
        self.msgTwist.twist.linear.x = 0.5
        self.msgTwist.twist.angular.z = 0.1
        self.publisher_.publish(self.msgTwist)
        self.get_logger().info('Publishing')
        self.i += 1
    def listener_callback(self, msg):
        self.msgLaser = msg
        self.parse_lidar_data_2d()
        self.get_logger().info(f'Got it')
    def parse_lidar_data_2d(self):
        
        #clean the array
        self.lidar_data = np.array(self.msgLaser.ranges)
        self.lidar_data = self.lidar_data[np.isfinite(self.lidar_data)]
        degree = np.linspace(0, 2*np.pi, len(self.lidar_data))
        #change form polar coordinates to cartesian coordinates for visualization
        x_cartesian = self.lidar_data * np.cos(degree)
        y_cartesian = self.lidar_data * np.sin(degree)
        self.get_logger().info(f'Got {x_cartesian[:10]} and {y_cartesian[:10]}')
        
    def maze_solver(self):
        None
        



def main(args=None):
    rclpy.init(args=args)
    mazeNode = MazeNode()
    rclpy.spin(mazeNode)
    rclpy.shutdown()

if __name__ == '__main__':
    main()