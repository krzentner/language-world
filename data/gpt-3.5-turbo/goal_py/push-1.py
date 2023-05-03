# Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Push the puck to the target location
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and closed around it, we can push the puck
    # to the target location (in this case, to the right).
    if check("the robot's gripper is around puck and the robot's gripper is almost vertically aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")