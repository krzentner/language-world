# Steps:
    #  1. Move gripper to target location
    #  2. Open gripper
    #  3. Move gripper away from target location
    # This task doesn't involve grabbing anything, so we just need to move the
    # gripper to the target location.
    if check("the robot's gripper is not at the target location"):
        robot.move("the gripper to the target location")
    # Once the gripper is at the target location, open it.
    if check("the robot's gripper is at the target location and closed"):
        robot.open("the gripper")
    # Finally, once the gripper is open, we can move it away from the target
    # location.
    if check("the robot's gripper is open and at the target location"):
        robot.move("the gripper away from the target location")