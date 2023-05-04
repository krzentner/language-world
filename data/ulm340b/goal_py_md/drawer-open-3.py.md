

For each line of code that you would like to execute, type `print(line_of_code)`.
(In other words, execute your code by printing out each line that you want to
execute.)

We have provided code to call your function with a simulated robot.
After submitting your code, click "Submit & Test" to see the output of your
program.
"""

def drawer_open(robot):
    if check("the robot's gripper is near the drawer handle"):
        print("robot.move_gripper(\"in front of the drawer handle\", close_gripper=True)")

    if check("the robot's gripper is in front of the drawer handle"):
        print("robot.move_gripper(\"below the drawer handle\")")


# Provided by assessor. Do not modify.
if __name__ == "__main__":
    from robot import Robot, check
    ROBOT_START = (200, 150, 20)
    ROBOT_GOAL = (20, 150, 20)
    ROBOT_LEFT = (20, 150, 80)

    ROBOT_RIGHT = (200, 150, 80)
    ROBOT_START_HANDLE = (150, 150, 20)
    ROBOT_GOAL_HANDLE = (150, 150, 80)

    robot = Robot(ROBOT_START)
    drawer_open(robot)
    robot.move_gripper("in front of the drawer handle")
    assert check("the robot's gripper is near the drawer handle")
    robot.move_gripper("below the drawer handle")
    assert check("the robot's gripper is in front of the drawer handle")
[eod] [code]from .base_options import BaseOptions


class TrainOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        self.parser.add_argument('--save_latest_freq', type=int, default=5000, help='frequency of saving the latest results')
        self.parser.add_argument('--display_freq', type=int, default=1000, help='frequency of showing training results on screen')
        self.parser.add_argument('--update_html_freq', type=int, default=10000, help='frequency of saving training results to html')
