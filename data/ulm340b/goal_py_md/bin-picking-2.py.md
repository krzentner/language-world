

and continue from there, using the robot's `move_gripper` and `move_gripper_to` methods.
"""

class Robot(object):
    def __init__(self):
        self.gripper_x = 0
        self.gripper_y = 0
        self.gripper_z = 0
        self.gripper_theta = 0
        self.gripper_width = 0
        self.last_move = None

    def move_gripper(self, goal, close_gripper=False):
        """
        Move the robot's gripper using a description that can be understood by a
        human being, like "above", "left of", etc. This is useful when you need
        to know where the robot needs to move but you don't know (or want to know)
        what the robot's joint angles need to be in order to reach that location.
        """
        rel_x, rel_y, rel_z, rel_theta, width = {
            "above": (0, 0, -1, 0, 0),
            "left of": (-1, 0, 0, 0, 0),
            "right of": (1, 0, 0, 0, 0),
            "behind": (0, -1, 0, 0, 0),
            "in front of": (0, 1, 0, 0, 0),
            "near": (0, 0, 0, 0, 0),
            "vertically aligned with": (0, 0, 0, 0, 0),
            "forward aligned with": (0, 0, 0, 0, 0),
            "almost vertically aligned with": (0, 0, 0, 0, 0),
            "horizontally aligned with": (0, 0, 0, 0, 0),
        }.get(goal, (0, 0, 0, 0, 0))
        self.last_move = {
            "x": self.gripper_x + rel_x,
            "y": self.gripper_y + rel_y,
            "z": self.gripper_z + rel_z,
            "theta": self.gripper_theta + rel_theta,
            "width": self.gripper_width + rel_width,
            "close": close_gripper,
        }

    def move_gripper_to(self, x, y, z, theta,