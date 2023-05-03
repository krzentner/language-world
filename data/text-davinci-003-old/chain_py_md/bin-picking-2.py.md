

Steps:
1. Move the gripper above the cube.
2. Drop the gripper around the cube.
3. Close the gripper around the cube.
4. Move the cube above the target bin.
5. Release the cube from the gripper at the top of the bin.

```
# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    # Steps:
    #  1. Move the gripper above the cube
    #  2. Drop the gripper around the cube
    #  3. Close the gripper around the cube
    #  4. Move the cube above the target bin
    #  5. Release the cube from the gripper at the top of the bin
    if check("the robot's gripper is not above the cube"):
        robot.put("the gripper above the cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("the gripper around the cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("the gripper around the cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube above the target bin.
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.carry("the cube above the target bin")
    # With the cube at the top of the bin, release the cube from the gripper.
    if check("the cube is above the target bin"):
        robot.release("the cube from the gripper")