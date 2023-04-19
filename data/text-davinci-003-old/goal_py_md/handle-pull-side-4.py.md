

Steps:
1. Put gripper left of the handle
2. Pull the handle up from the side

    if check("the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle")
    # Pull the handle up from the side.
    if check("the robot's gripper is left of the handle"):
        robot.move_gripper("vertically aligned with the handle")