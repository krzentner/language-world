

Then, write code that describes what the robot should do in comments. Then, write the code that makes the robot perform these steps. For example:

```
# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put the robot's gripper above the stick
    #  2. Move the gripper down around the stick
    #  3. Grab the stick with the gripper
    #  4. Reach towards the thermos
    #  5. Push the thermos
    #  6. Slide the thermos to the target location
    # First, move the robot's gripper to be above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # If the gripper is above the stick, try to grab the stick.
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around the stick"):
        robot.move_gripper("around the stick", close_gripper=True)
    # If we're holding the stick, reach towards the thermos.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("near the thermos", close_gripper=True)
    # If we're holding the stick and near the thermos, start trying to push the thermos.
    if check("the robot's gripper is near the thermos and the thermos is not below the robot's gripper"):
        robot.move_gripper("near the thermos", close_gripper=True)
    # If we've started moving the thermos, just slide it all the way to the target.
    if check("the thermos is below the robot's gripper and the thermos is not vertically aligned with the target"):
        robot.move_gripper("vertically aligned with the target", close_gripper=True)
```

Please complete the code for `stick-push`.
"""
from lab_5_2_01_robot_code import *


def stick_push(robot):
    """
    Grab the stick and use it to push the thermos to the target location
    
    :param robot: a robot with its gripper at the ready
    