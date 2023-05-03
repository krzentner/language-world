
    # Steps:
    #  1. Hold hammer in robot's gripper
    #  2. Move the robot's gripper to the nail
    #  3. Hit the nail with the hammer
    # Once the robot has the hammer, it needs to move its gripper to the nail.
    if check("the robot's gripper is not near the nail"):
        robot.move("gripper to nail")
    # When the robot's gripper is near the nail, hit the nail with the hammer.
    if check("the robot's gripper is near the nail and the hammer is in the robot's gripper"):
        robot.hit("nail with hammer")