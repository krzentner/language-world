
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # Pick up the puck by dropping the gripper down around it and then closing
    # the gripper.
    if check("the robot's gripper is not vertically aligned with the puck and the robot's gripper is open"):
        robot.move_gripper("vertically aligned with the puck", close_gripper=True)
    # If the gripper is around the puck and it's closed, move the puck to the
    # target location.
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")