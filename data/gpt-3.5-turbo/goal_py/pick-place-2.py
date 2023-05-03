# Steps:
    #  1. Put gripper above puck
    #  2. Grab puck with gripper
    #  3. Move gripper to target location
    #  4. Release puck
    # We need to pick up the puck first by aligning the gripper above it and
    # closing the gripper.
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.move_gripper("vertically aligned with the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Once we've grabbed the puck, we can now move it to the target location by
    # moving the gripper there.
    if check("the robot's gripper is around the puck and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # Finally, release the puck by opening the gripper.
    if check("the robot's gripper is near the target location and the robot's gripper is around the puck"):
        robot.move_gripper("vertically aligned with the target location", close_gripper=False)