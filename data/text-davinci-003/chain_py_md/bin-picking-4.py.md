

Then add the following steps to the program: 

1. Put gripper above cube
2. Drop gripper around cube
3. Close gripper around cube
4. Move cube to target bin

```
# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to target bin
    # Put the gripper above the cube so it does not bump the cube when trying to
    # grab it.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so we have
    # successfully grabbed the cube.
    # Try to move the cube to the target bin.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.put("cube into bin")
```