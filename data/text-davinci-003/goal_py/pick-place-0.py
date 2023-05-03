
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab puck with gripper
    #  3. Lift puck
    #  4. Move puck to target location
    # If the puck isn't aligned with the gripper from above, line them up before
    # trying to grab the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck", close_gripper=True)
    # If the puck is aligned with the gripper, grab it.
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.move_gripper("above the puck")
    # Once the gripper is around the puck, we can lift it.
    if check("gripper is around the puck"):
        robot.move_gripper("above the target location")