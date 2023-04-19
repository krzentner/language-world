# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Move gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move gripper above the target bin
    #  4. Drop the cube in the bin
    # First, move the gripper above the cube
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and closed, move the gripper above the target bin.
    if check("the robot's gripper is near the cube and the gripper has a cube and the robot's gripper is not above the target bin"):
        robot.move_gripper("above the target bin")
    # If the gripper is above the target bin, drop the cube in the bin.
    if check("the robot's gripper is above the target bin and the gripper has a cube"):
        robot.move_gripper("opened above the target bin")