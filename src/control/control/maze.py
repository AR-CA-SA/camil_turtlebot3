import numpy as np
import matplotlib.pyplot as plt
import rclpy
from rclpy.node import Node
from matplotlib.animation import FuncAnimation
from sensor_msgs.msg import LaserScan


class MazeNode(Node):
    def __init__(self):
        super().__init__("maze_node")
        self.subscription = self.create_subscription(LaserScan, '/scan', self.callback, 
         10)
    def callback(self, msg):
        self.lidar_data = np.array(msg.ranges)
        self.lidar_data[np.isfinite(self.lidar_data)]  
        self.get_logger().info(f'Got {self.lidar_data}')
    def paser_lidar_data_2d(self):
        degree = np.arange(0, 2*np.pi, 360)
        x = self.lidar_data * np.cos(degree)
        y = self.lidar_data * np.sin(degree)





def main(args=None):
    rclpy.init(args=args)
    suscriber = MazeNode()
    rclpy.spin(suscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()