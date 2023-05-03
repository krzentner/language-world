# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    # Steps:
    #  1. Move gripper to the cube
    #  2. Grab the cube with the gripper
    #  3. Move the gripper to the target bin
    #  4. Place the cube in the target bin
    # First, move the gripper close to the cube without hitting it or anything else around it.
    if check("the robot's gripper is not near the cube"):
        robot.move("gripper to cube")
    # Once the gripper is near the cube, open the gripper and grab the cube.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
        robot.close("gripper around cube")
    # Now that we have the cube, we should move it to the target bin.
    # Make sure the gripper is above the bin without hitting it or anything else.
    if check("the robot's gripper is not above the target bin"):
        robot.move("gripper above target bin")
    # Once the gripper is above the bin, lower it into the bin and open the gripper to let go of the cube.
    if check("the robot's gripper is above the target bin and the robot's gripper is closed"):
        robot.put("gripper inside bin")
        robot.open("gripper around cube")