 
    # Steps:
    #  1. Put gripper almost vertically aligned with the door handle
    #  2. Push the door closed
    # The robot needs to put the gripper almost vertically aligned with the
    # door handle before trying to push the door closed.
    if check("the robot's gripper is almost vertically aligned with door handle"):
        robot.move_gripper("left of the door handle")
    # If the gripper is almost vertically aligned, push the door closed.
    if check("the robot's gripper is in front of the door handle"):
        robot.move_gripper("almost vertically aligned with the door handle")