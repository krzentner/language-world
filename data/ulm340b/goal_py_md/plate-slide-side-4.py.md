

and replace the line containing `# <your program here>` with your code.

Once you're done, click "Submit" and we'll simulate the robot following your
code!

"""


# import the function `move_gripper` for controlling the robot's gripper
from robot import Robot

# define the function to run on the robot, which should be called `plate_slide_side`

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Move gripper next to the plate
    #  2. Slide the plate into the target location
    # We can just slide the plate by aligning the gripper with it.
    if check("the robot's gripper is not horizontally aligned with plate"):
        robot.move_gripper("horizontally aligned with plate")
    if check("the robot's gripper is almost vertically aligned with plate"):
        robot.move_gripper("near plate", close_gripper=True)
    if check("the robot's gripper is near plate and the robot's gripper is not near the target location"):
        robot.move_gripper("horizontally aligned with the target location")


if __name__ == "__main__":
    print("Entering main...")

    # create a robot
    robot = Robot()

    # run `plate_slide_side` on the robot
    robot.plate_slide_side()

    # wait for the user to hit any key before exiting
    input("Press any key to finish...")
    print("Leaving main...")
[eod] [code]import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from src.ui.mainwindow import Ui_MainWindow
from src.game_controller import GameController


class MyApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.controller = GameController()
        self.controller.init(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
[eod] [code]# Generated by Django 2.2 on 2019-06-19 20:13

from django.db import migrations