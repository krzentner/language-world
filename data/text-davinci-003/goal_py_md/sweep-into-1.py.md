 

```
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper near the cube
    #  2. Grab the cube with the gripper
    #  3. Sweep the cube towards the target location
    # First, move the gripper near the cube.
    if check("the robot's gripper is not near cube"):
        robot.move_gripper("near cube", close_gripper=True)
    # As long as the gripper is near the cube and the cube is not below the
    # gripper, close the gripper around the cube.
    if check("the robot's gripper is near cube and cube is not below the robot's gripper"):
        robot.move_gripper("above the cube")
    # If the gripper is above the cube and the cube is below the gripper, sweep
    # the cube towards the target location.
    if check("the cube is below the robot's gripper"):
        robot.move_gripper("near the target location")
```