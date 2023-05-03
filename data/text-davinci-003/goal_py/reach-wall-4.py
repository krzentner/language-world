
    # Steps:
    #  1. Move gripper to the side of the wall
    #  2. Reach towards the target
    # First, put the gripper near the side of the wall.
    # Check if the gripper is near the side of the wall, but not at the target.
    # To make sure the gripper doesn't hit the wall, check that the gripper is
    # also below the wall as seen from above.
    if check("the robot's gripper is not near the side of the wall and the robot's gripper below the wall"):
        robot.move_gripper("near the side of the wall")
    # If the gripper should be in front of the wall, reach towards the target
    if check("the robot's gripper is near the side of the wall and the robot's gripper not at the reach target"):
        robot.move_gripper("near the reach target")