
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Pull the door open
    # If the robot's gripper is not above the door handle, move the robot's
    # gripper above the door handle.
    if check("the robot's gripper is not above the door handle"):
        robot.move_gripper("above the door handle")
    # Once the robot's gripper is above the door handle, pull the door open.
    if check("the robot's gripper is above the door handle"):
        robot.move_gripper("left of the door handle")