

I will then ask you about the steps the robot should take.
"""


class Program(object):
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        if command in self.commands:
            raise ValueError("command `%s` has already been added")
        else:
            self.commands.append(command)

    def get_commands(self):
        return sorted(self.commands)


class Robot(object):
    def __init__(self):
        pass

    def place(self, args):
        pass

    def drop(self, args):
        pass

    def grab(self, args):
        pass

    def reach(self, args):
        pass

    def move(self, args):
        pass

    def align(self, args):
        pass

    def insert(self, args):
        pass

    def close(self, args):
        pass

    def put(self, args):
        pass

    def push(self, args):
        pass

    def slide(self, args):
        pass

    def pull(self, args):
        pass

    def check(self, state):
        pass


def plate_slide_side(robot):
    """slide the plate sideways into the target location

    If there is more than one plate in the scene, you can use the word `plate`
    in the code to refer to the closest plate to the robot's gripper.

    Arguments:
        robot

    Returns:
        None
    """
    """
    if check("plate is left of the robot's gripper"):
        robot.slide("plate to the left")
    if check("plate is not left of the robot's gripper and plate is not right of the robot's gripper and plate is not above the robot's gripper"):
        robot.move("gripper to left of plate")
    if check("plate is not left of the robot's gripper"):
        robot.slide("plate to the right")
    if check("plate is not left of the robot's gripper and plate is not right of the robot's gripper"):
        robot.move("gripper above plate")
    if check("plate is left of the robot's gripper"):
        robot.slide("plate to the left")
    if check("plate is right of the robot's gripper"):
       