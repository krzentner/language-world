
    # Steps:
    #  1. Place gripper above the puck
    #  2. Drop gripper around the puck
    #  3. Close gripper on the puck
    #  4. Move puck to goal
    # We need to line up the gripper with the puck, while being careful not to
    # bump the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # Once the gripper is lined up above the puck, we should be able to grab it
    # by closing the gripper.
    if check("the robot's gripper is above the puck and the robot's gripper is not closed"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is closed around the puck, we've probably grabbed the puck
    # so we can move it to the goal.
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        robot.move_gripper("at the target location")