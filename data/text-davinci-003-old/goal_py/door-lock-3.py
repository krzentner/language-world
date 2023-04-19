
    # Steps:
    #  1. Put gripper above the door lock
    #  2. Drop gripper around the door lock
    #  3. Turn the door lock 90 degrees
    # First, put the gripper above the door lock.
    if check("the robot's gripper is not vertically aligned with the door lock"):
        robot.move_gripper("vertically aligned with the door lock")
    # If the gripper isn't around the door lock, put it around it.
    if check("the robot's gripper is not around door lock and the robot's gripper is open"):
        robot.move_gripper("near the door lock", close_gripper=True)
    # If the gripper is around the door lock, we can just turn the door lock 90
    # degrees.
    if check("the robot's gripper is around door lock"):
        robot.move_gripper("90 degrees")