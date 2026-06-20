import numpy as np
import matplotlib.pyplot as plt
import rclpy
from rclpy.node import Node
from matplotlib.animation import FuncAnimation

from sensor_msgs.msg import LaserScan


fig, ax = plt.subplots()

class MazeNode(Node):
    def __init__(self):
        super().__init__("maze_node")
        self.subscription = self.create_subscription(LaserScan, '/scan', self.callback, 
         10)
    def callback(self, msg):
        self.parse_lidar_data_2d()  
        self.get_logger().info(f'Got it')
    def parse_lidar_data_2d(self):
        
        #clean the array
        self.lidar_data = np.array(msg.ranges)
        self.lidar_data = self.lidar_data[np.isfinite(self.lidar_data)]
        degree = np.linspace(0, 2*np.pi, len(self.lidar_data))
        #change form polar coordinates to cartesian coordinates for visualization
        x_cartesian = self.lidar_data * np.cos(degree)
        y_cartesian = self.lidar_data * np.sin(degree)
        # self.get_logger().info(f'Got {x_cartesian[:10]} and {y_cartesian[:10]}')





def main(args=None):
    rclpy.init(args=args)
    suscriber = MazeNode()
    rclpy.spin(suscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()