

Steps: 
1. Put the gripper near the cube
2. Grab the cube with the gripper
3. Align the cube with the target bin opening
4. Push the cube into the target bin

```
# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Put gripper near cube
    #  2. Grab cube with gripper
    #  3. Align cube with target bin opening
    #  4. Push cube into target bin
    # First, move the robot's gripper to the cube.
    if check("the robot's gripper is not near cube"):
        robot.move("gripper to cube")
    # Once the robot's gripper is close to the cube, try to grab it.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.grab("cube")
    # As long as the cube is not lined up with the target bin opening and the
    # gripper is still around the cube, try to line them up.
    if check("cube is not aligned with target bin opening and the robot's gripper is closed around cube"):
        robot.align("cube to target bin opening")
    # If the cube is lined up, we should be able to push it into the target bin.
    if check("cube is aligned with target bin opening and the robot's gripper is closed around cube"):
        robot.push("cube into target bin")