
    # Steps:
    #  1. Put gripper above wall
    #  2. Reach over the wall towards the target
    # First, move the gripper above the wall.
    if check("the robot's gripper is not above wall"):
        robot.move_gripper("above the wall")
    # Now that the gripper is above the wall, reach over the wall to the target.
    if check("the robot's gripper is above wall and the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")