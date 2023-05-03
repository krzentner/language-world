
    # Steps:
    #  1. Put gripper at start location
    #  2. Move gripper to target
    # We just need to move the gripper to the target location.
    # Ideally, the gripper should be lined up with the target location and the
    # robot's body before moving.
    if check("the robot's gripper is not near the target location and the robot's gripper is not forward aligned with the target location"):
        robot.put("gripper near and aligned with target location")
    # Now that the gripper is lined up, just move the gripper.
    if check("the robot's gripper is near the target location and the robot's gripper is forward aligned with the target location"):
        robot.move("gripper to the target location")