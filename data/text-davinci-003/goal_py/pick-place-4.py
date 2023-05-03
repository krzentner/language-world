
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab puck with gripper
    #  3. Move gripper to target location
    # If the gripper is not vertically aligned with the puck,we should align it.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # As long as the puck isn't below the gripper, drop the gripper to the puck.
    # Once the gripper is around the puck, close the gripper to grab it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Once the robot has grabbed the puck, we can just move the gripper to the
    # target location and drop the puck.
    if check("the robot is carrying the puck"):
        robot.move_gripper("above the target location", open_gripper=True)