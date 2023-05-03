# Steps:
    #  1. Move gripper above target location
    #  2. Move gripper down to target location
    # When reaching to a target location, the robot just needs to move the
    # gripper to the correct position and orientation.
    # First, move the gripper above the target location.
    if check("the robot's gripper is not above the target location"):
        robot.move("gripper above target location")
    # Once the gripper is above the target location, move it down to the target
    # location.
    if check("the robot's gripper is above the target location"):
        robot.move("gripper to target location")