import rclpy
from rclpy.node import Node


from sensor_msgs.msg import LaserScan


class MazeNode(Node):
    def __init__(self):
        super().__init__("maze_node")
        self.lidar_data = self.create_subscription(LaserScan, '/scan', self.callback, 
         10)
    def callback(self, msg):
        self.get_logger().info(f'Got {msg.ranges}')

def main(args=None):
    rclpy.init(args=args)
    suscriber = MazeNode()
    rclpy.spin(suscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()