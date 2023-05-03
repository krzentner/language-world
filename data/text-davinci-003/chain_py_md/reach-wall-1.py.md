

Followed by the code to make it happen:

```
    # Steps:
    #  1. Reach past the wall 
    #  2. Readjust to the target 
    # First, reach past the wall so that the robot's gripper can travel around it.
    if check("the robot's gripper is not on the other side of the wall"):
        robot.reach("past wall")
    # Once the robot's gripper is on the other side of the wall, readjust to the 
    # target location.
    if check("the robot's gripper is on the other side of the wall and the robot's gripper is not near reach target"):
        robot.reach("to goal")
```