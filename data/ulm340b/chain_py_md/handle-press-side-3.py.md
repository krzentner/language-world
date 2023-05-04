

Write a program to tell the robot how to press down the handle.
You can assume that the robot starts with its gripper near the handle.

```
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Push the handle down
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above the handle")
    if check("the handle is not vertically aligned with the robot's gripper"):
        robot.grab("handle")
    if check("the handle is vertically aligned with the robot's gripper"):
        robot.push("handle down")
```

`handle-press-side` is complete.`

class TestRobot:
    def __init__(self):
        self.handle = True
        self.button = True
        self.gripper = False

    def handle_closed(self):
        self.handle = True

    def handle_open(self):
        self.handle = False

    def button_up(self):
        self.button = True

    def button_down(self):
        self.button = False

    def gripper_open(self):
        self.gripper = True

    def gripper_closed(self):
        self.gripper = False


test_robot = TestRobot()
robot_state = test_robot

def check(str):
    test_robot.gripper = robot_state.gripper
    test_robot.button = robot_state.button
    test_robot.handle = robot_state.handle
    if str == "the handle is open":
        return test_robot.handle_open() == True
    elif str == "the button is up":
        return test_robot.button_up() == True
    elif str == "the robot's gripper is open":
        return test_robot.gripper_open() == True
    elif str == "the handle is vertically aligned with the robot's gripper":
        return test_robot.handle_closed() == True and test_robot.gripper_closed() == True
    elif str == "the handle is above the robot's gripper":
        return test_robot.handle_closed() == True
    elif str == "the handle is closed":
        return test_robot.handle_closed