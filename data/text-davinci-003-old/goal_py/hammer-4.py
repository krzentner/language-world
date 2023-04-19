
    # Steps:
    #  1. Put gripper above the nail
    #  2. Move the hammer head onto the nail
    #  3. Hit the nail with the hammer
    # First, move the gripper above the nail.
    if check("the robot's gripper is not near the nail"):
        robot.move_gripper("above the nail", close_gripper=True)
    # Once the gripper is above the nail, move the hammer head onto the nail.
    if check("the robot's gripper is above the nail and the hammer head is not on the nail"):
        robot.move_gripper("on the nail")
    # Once the hammer head is on the nail, hit the nail with the hammer.
    if check("the robot's gripper is on the nail"):
        robot.move_gripper("above the nail")