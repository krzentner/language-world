
    # Steps:
    #  1. Put gripper above the door lock
    #  2. Move gripper around the lock
    #  3. Twist the knob to the desired number
    # First, put the robot's gripper above the door lock.
    if check("the robot's gripper is not above the door lock"):
        robot.move_gripper("above the door lock")
    # Once the gripper is above the lock, move it around the lock.
    if check("the robot's gripper is not around the door lock"):
        robot.move_gripper("around the door lock", close_gripper=True)
    # Once the gripper is around the lock, twist the knob to the desired number.
    if check("the robot's gripper is around the door lock"):
        robot.move_gripper("counterclockwise around the door lock")