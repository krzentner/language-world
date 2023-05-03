# Steps:
    #  1. Locate the lever grip
    #  2. Grab the lever grip with the gripper
    #  3. Rotate the lever up
    # If the gripper is not already above the lever grip, move it there.
    if check("the robot's gripper is not above the lever grip"):
        robot.move_gripper("above the lever grip")
    # If the gripper is not already gripping the lever grip, close the gripper
    # around it.
    if check("the robot's gripper is above the lever grip and the robot's gripper is not holding the lever grip"):
        robot.move_gripper("around the lever grip", close_gripper=True)
    # Once the gripper is holding the lever grip, rotate the lever up.
    if check("the robot's gripper is holding the lever grip"):
        robot.move_gripper("upwards aligned with the lever")