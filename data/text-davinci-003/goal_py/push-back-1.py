
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck backward to goal
    # We need to put the gripper roughly above the puck, so that we don't bump 
    # it while trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # Once the gripper is around the puck, we can pull the puck backward to the
    # target location.
    if check("robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("near the target location")