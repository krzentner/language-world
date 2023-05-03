
    # Steps:
    #  1. Put gripper below door handle
    #  2. Push the door closed
    # Put the gripper vertically aligned with the door handle to start pushing.
    # This is easier than approaching the door handle from above, since the robot
    # is closer to the door handle at this angle.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("right of the door handle")
    # As long as the gripper is aligned with the handle and still left of it, push
    # the door closed by moving the gripper right.
    if check("the robot's gripper is in front of the door handle"):
        robot.move_gripper("around the door handle")