

Then, complete the program with the following code:
```
    # Steps:
    #  1. Put gripper above the wall
    #  2. Reach around the wall to the target location
    # First, put the gripper above the wall blocking the target location.
    if check("the robot's gripper is not above the wall"):
        robot.move_gripper("above the wall")
    # Now that the gripper is above the wall, reach around the wall to the target location.
    if check("the robot's gripper is above the wall"):
        robot.move_gripper("near the reach target")
```