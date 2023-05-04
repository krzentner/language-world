

Please write your code below.

```
# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above ball
    #  2. Grab ball
    #  3. Move the ball over the basket
    #  4. Drop ball in the basket
    # First, put the gripper above the ball so it doesn't bump the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("almost vertically aligned with the ball")
    # If the gripper is vertically aligned with the ball, close it to grab the
    # ball.
    if check("the robot's gripper is not almost vertically aligned with the ball"):
        robot.move_gripper("around the ball", close_gripper=True)
    # If the gripper is around the ball, move the ball above the basket.
    if check("the ball is left of the robot's gripper"):
        robot.move_gripper("almost vertically aligned with basket")
    # If the ball is above the basket, drop the ball in.
    if check("the robot's gripper is left of the basket"):
        robot.move_gripper("almost vertically aligned with the ball")
```

"""


class Robot:
    def __init__(self):
        self._gripper_location = np.array([0.0, 0.0, 0.0])
        self._gripper_orientation = np.array([1.0, 0.0, 0.0, 0.0])
        self._gripper_open = False

    def move_gripper(self, *args, **kwargs):
        self._gripper_location = np.array([0.0, 0.0, 0.0])
        self._gripper_orientation = np.array([1.0, 0.0, 0.0, 0.0])
        self._gripper_open = False

    def get_gripper_location(self):
        return self._gripper_location

    def get_gripper_orientation(self):
        return self._gripper_orientation

    def get_gripper_open(self):
        return self._gripper_open


robot = Robot()
robot.move_gripper("right of the door handle