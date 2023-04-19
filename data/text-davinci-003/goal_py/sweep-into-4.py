
    # Steps:
    #  1. Put the gripper above the cube
    #  2. Drop the gripper around the cube and close it
    #  3. Sweep the cube into the target location
    # We need to put the gripper in the same plane as the cube, so start by
    # putting the gripper above the cube from the top.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # Once the gripper is above the cube, we can just drop it around the cube
    # and close it, trapping the cube in the gripper.
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is closed, we can move the cube to the target location by
    # sweeping it sideways.
    if check("the robot's gripper is around the cube and the robot's gripper, cube and target are not horizontally aligned"):
        robot.move_gripper("near the target location")