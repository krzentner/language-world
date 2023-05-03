
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Place puck in box
    # If the gripper isn't near the puck, move it there.
    if check("the robot's gripper is not above the puck and the robot's gripper is not around the puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # Once the gripper is close to the puck, place it in the box by moving the
    # gripper away from the puck.
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("left of the puck", close_gripper=False)