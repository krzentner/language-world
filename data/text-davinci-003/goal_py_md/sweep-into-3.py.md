

The code should be:

```
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above the cube 
    #  2. Drop gripper around cube 
    #  3. Close gripper around the cube 
    #  4. Push against the cube to move the cube to the target location
    # Put the robot's gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.move_gripper("above the cube") 
    # If the gripper isn't around the cube, try to move it around it.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Once the gripper is around the cube, close the gripper to grab the cube.
    if check("the robot's gripper is around cube"):
        robot.move_gripper("close around cube")
    # If the gripper is closed around the cube, push on it to move it towards
    # the target location.
    if check("the robot's gripper is closed around cube"):
        robot.move_gripper("above the target location")
```