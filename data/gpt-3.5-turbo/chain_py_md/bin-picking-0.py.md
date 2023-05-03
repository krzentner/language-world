# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Check for a cube in the bin. If there is none, return.
    #  2. Move gripper above the cube.
    #  3. Move gripper around the cube.
    #  4. Close gripper around the cube.
    #  5. Move the gripper to the target bin.
    #  6. Put the cube in the target bin.
    #  7. Open the gripper.

    # Check for a cube in the bin. If there is none, return.
    if check("no cube in the bin"):
        return

    # Move the gripper above the cube.
    if check("the gripper is not above the cube"):
        robot.move("gripper above the cube")

    # Move the gripper around the cube.
    if check("the gripper is not around the cube"):
        robot.move("gripper around the cube")

    # Close the gripper around the cube.
    if check("the gripper is not closed around the cube"):
        robot.close("gripper around the cube")

    # Move the gripper to the target bin.
    if check("the gripper is not above the target bin"):
        robot.move("gripper above the target bin")
    if check("the gripper is not around the target bin"):
        robot.move("gripper around the target bin")

    # Put the cube in the target bin.
    if check("the gripper is not directly over the target bin"):
        robot.move("gripper directly over the target bin")
    if check("the gripper is not open above the target bin"):
        robot.move("gripper open above the target bin")
    if check("the gripper is not closed around the target bin"):
        robot.move("gripper closed around the target bin")
    if check("the gripper is not directly over the target bin"):
        robot.move("gripper directly over the target bin")
    if check("the gripper is not open above the target bin"):
        robot.move("gripper open above the target bin")

    # Open the gripper.
    if check("the gripper is not open"):
        robot.open("gripper")