# Steps:
    #  1. Put the gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move gripper to target location
    #  4. Release the puck
    # First, move the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # Once the gripper is above the puck, we can grab it by moving the gripper
    # down around it.
    if check("the robot's gripper is above the puck and the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Now we can move the gripper to the target location.
    if check("the robot's gripper is holding the puck and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # Finally, release the puck.
    if check("the robot's gripper is near the target location and the gripper is holding the puck"):
        robot.move_gripper("near the target location", close_gripper=False)