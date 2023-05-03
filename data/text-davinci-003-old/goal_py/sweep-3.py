
    # Steps:
    #  1. Move gripper above the cube
    #  2. Grab the cube
    #  3. Move the cube sideways to the target location
    # First, move the gripper above the cube, if it isn't already.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube", close_gripper=True)
    # If the cube is still above the gripper but the gripper is open, maybe
    # we can grab it by closing the gripper.
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.move_gripper("above the cube", close_gripper=True)
    # Now that the cube is in the gripper, we can move the cube sideways to
    # the target position.
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.move_gripper("above the target location")