
"""

################################################################################################


class Robot:
    def __init__(self, world):
        self.world = world
        self.gripper_x = world.gripper_x
        self.gripper_y = world.gripper_y
        self.gripper_open = world.gripper_open

    def move_gripper(self, to_where, close_gripper=False):
        if to_where == "near the robot's gripper":
            self.world.gripper_x = self.gripper_x
            self.world.gripper_y = self.gripper_y

        if to_where == "above the robot's gripper":
            self.world.gripper_y = self.gripper_y - 50

        if to_where == "below the robot's gripper":
            self.world.gripper_y = self.gripper_y + 50

        if to_where == "left of the robot's gripper":
            self.world.gripper_x = self.gripper_x - 50

        if to_where == "right of the robot's gripper":
            self.world.gripper_x = self.gripper_x + 50

        if to_where == "vertically aligned with the robot's gripper":
            self.world.gripper_x = self.gripper_x
            self.world.gripper_y = self.gripper_y + 50

        if to_where == "vertically aligned with the robot's gripper":
            self.world.gripper_y = self.gripper_y + 50

        if to_where == "forward aligned with the robot's gripper":
            self.world.gripper_y = self.gripper_y
            self.world.gripper_x = self.gripper_x + 50

        if to_where == "backward aligned with the robot's gripper":
            self.world.gripper_x = self.gripper_x + 50

        if close_gripper:
            self.world.gripper_open = False

        else:
            self.world.gripper_open = True


world = World()
world.initialize()
world.reset()
robot = Robot(world)
robot.move_gripper("above the robot's gripper")
robot.move_gripper("above the robot's gripper")
robot.move_g