# Steps:
    #  1. Put gripper above the puck
    #  2. Drop gripper around the puck
    #  3. Push the puck to the target location
    # First, put the gripper roughly above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # Once the gripper is around the puck, push it to the target location.
    if check("the robot's gripper is around puck and the robot's gripper is not near target location"):
        robot.move_gripper("near the target location")