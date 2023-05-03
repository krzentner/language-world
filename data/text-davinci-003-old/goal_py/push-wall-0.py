
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Roll puck towards goal, pushing the wall
    # First, put the gripper roughly above the puck so we don't accidentally
    # bump it.
    if check("the robot's gripper is not above puck"):
        robot.move_gripper("above the puck")
    # If the puck isn't below the gripper, move the gripper so it is in front of
    # the puck. This should keep it above the wall.
    if check("the puck is below the robot's gripper and the robot's gripper is not forward aligned with the puck"):
        robot.move_gripper("forward aligned with the puck", close_gripper=True)
    # If the gripper is near the puck and open, close the gripper to trap the
    # puck and slide it towards the goal.
    if check("the robot's gripper is near the puck and the robot's gripper is closed"):
        robot.move_gripper("above the target location")