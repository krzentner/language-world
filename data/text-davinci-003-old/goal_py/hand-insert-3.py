
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, move the gripper above the puck. This helps us to avoid bumping it
    # while trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper is still very far away from the puck, move the gripper
    # directly towards the puck until it is in front of the gripper.
    if check("the robot's gripper is not near the puck and the robot's gripper is not forward aligned with puck"):
        robot.move_gripper("forward aligned with the puck", close_gripper=True)
    # Now, close the gripper to trap the puck.
    if check("the robot's gripper is forward aligned with puck and the robot's gripper is open"):
        robot.move_gripper("to the target location")