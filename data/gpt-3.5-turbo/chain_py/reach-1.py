# Steps:
    #  1. Move gripper close to the target location
    #  2. Extend robot arm to reach the target location
    # First, move the gripper close to the target location.
    if check("the gripper is not near the target location"):
        robot.move("the gripper near the target location")
    # Once the gripper is near the target location, extend the robot arm to reach
    # it.
    if check("the gripper is near the target location"):
        robot.extend("the robot arm to reach the target location")