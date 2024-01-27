# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPubSub(Node):

    def __init__(self):
        super().__init__('minimal_pubsub')
        self.last_message = "--"
        timer_period_seconds = 0.5
        self.i = 0
        self.subscription = self.create_subscription(
            String,
            '/update',
            self.update_last_message,
            10
        )
        self.publisher_ = self.create_publisher(String, '/hey', 10)
        self.timer = self.create_timer(
            timer_period_seconds, self.timer_callback)

    def update_last_message(self, new_message: String):
        self.get_logger().info(f"Updating the last message to: {new_message}")
        self.last_message = new_message.data

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello World: {self.i}. Last message is: {self.last_message}'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPubSub()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
