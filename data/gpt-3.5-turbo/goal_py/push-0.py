# Steps:
    #  1. Put gripper mostly above puck
    #  2. Drop gripper around puck
    #  3. Push puck towards target
    # First, put the gripper roughly above the puck, without getting too close to
    # it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is around the puck, we can push the puck towards the target.
    if check("the robot's gripper is around puck and the robot's gripper is near the puck"):
        robot.move_gripper("near the target location")