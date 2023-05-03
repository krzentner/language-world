
    # Steps:
    #  1. Reach towards the target
    # When the gripper is below the wall, move the gripper around the wall.
    if check("the gripper is below wall"):
        robot.move_gripper("above the wall")
    # Now that the gripper is above the wall, reach towards the target.
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")