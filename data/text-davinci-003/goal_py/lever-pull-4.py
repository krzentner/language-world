
    # Steps:
    #  1. Put the gripper so that it is aligned with the lever
    #  2. Close the gripper around the lever
    #  3. Rotate the lever up
    # Move the gripper to the front of the lever.
    if check("the robot's gripper is not horizontally aligned with lever"):
        robot.move_gripper("horizontally aligned with the lever", close_gripper=True)
    # Close the gripper around the lever.
    if check("the robot's gripper is forward aligned with lever and the robot's gripper is open"):
        robot.move_gripper("vertically aligned with the lever")
    # Rotate the lever up.
    if check("the robot's gripper is vertically aligned with lever and the robot's gripper is closed"):
        robot.move_gripper("above the lever")