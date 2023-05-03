

```
# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper in front of puck
    #  2. Push the puck forward
    # To start off, we can move the robot's gripper in front of the puck.
    if check("the robot's gripper is not horizontally aligned with puck"):
        robot.move_gripper("horizontally aligned with puck")
    # If the gripper is still in front of the puck and the puck is not near the
    # target location, start pushing.
    if check("the robot's gripper is forward aligned with puck and the puck is not near the target location"):
        robot.move_gripper("horizontally aligned with the target location")
```