
    # Steps:
    #  1. Position the hammer above the nail
    #  2. Move the hammer down onto the nail
    #  3. Swing the hammer downward
    # Put the hammer roughly above the nail.
    if check("the hammer is not above the nail and the robot's gripper is not above the hammer"):
        robot.put("hammer above nail")
    # Rotate the gripper around the hammer, so that it will move in a straight
    # line.
    if check("the robot's gripper is not above the hammer and the robot's gripper is not around the hammer"):
        robot.drop("gripper around hammer")
    # Strike the nail with the hammer, angled such that it will stick into the
    # nail.
    if check("the robot's gripper is above the hammer"):
        robot.strike("hammer downward")