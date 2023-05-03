

Then your program should look like this:

```
# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube above target bin
    #  5. Drop cube into target bin
        
    # First, put the gripper above the cube.
    if check("the robot's gripper is not near the cube and the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # Then, drop the gripper around the cube.
    if check("the robot's gripper is not near the cube and the robot's gripper is above the cube and the robot's gripper is not closed"):
        robot.drop("gripper around cube")
    # Then, close the gripper around the cube.
    if check("the robot's gripper is near the cube and the robot's gripper is not closed"):
        robot.close("gripper around cube")
    # Then, move the cube above the target bin.
    if check("the robot's gripper is above the cube and the target bin is not below the cube"):
        robot.lift("cube to target bin")
    # Finally, drop the cube into the target bin.
    if check("the target bin is below the cube"):
        robot.drop("cube into target bin")
```