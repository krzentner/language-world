

When you run the following command:

```
python3 -m cs188.run_robot hammer
```

Your program should use the robot to hammer the nail at least once.
"""

import numpy as np
import robot_fingers

class Robot:
    def __init__(self, object_info):
        self.pos = object_info['robot_position']
        self.gripper_angle = object_info['gripper_angle']
        self.gripper_width = object_info['gripper_width']
        self.gripper_height = object_info['gripper_height']
        self.gripper_state = self.gripper_width == object_info['gripper_close_width']
        self.robot_pos = self.pos[0, :]
        self.obj_pos = self.pos[1:, :]
        self.obj_id = object_info['object_id']
        self.target_pos = object_info['target_position']

    def move_grip(self, dist):
        """ Move the gripper by a distance (in meters). """
        self.gripper_angle += dist

    def move_to(self, pos):
        """ Move the gripper to a (x,y) position (in meters). """
        self.robot_pos = pos

    def open_grip(self):
        """ Open the gripper. """
        self.gripper_width += 0.01
        self.gripper_state = False

    def close_grip(self):
        """ Close the gripper. """
        self.gripper_width = object_info['gripper_close_width']
        self.gripper_state = True

    def place(self, text):
        """ Some function. """
        return

    def put(self, text):
        """ Some function. """
        return

    def reach(self, text):
        """ Some function. """
        return

    def grab(self, text):
        """ Some function. """
        return

    def put(self, text):
        """ Some function. """
        return

    def align(self, text):
        """ Some function. """
        return

    def insert(self, text):
        """ Some function. """
        return

    def pick(self, text):
        """ Some function. """
        return

    def close(self, text):
        """ Some function. """
        return

    def place(self, text):
        """ Some function. """