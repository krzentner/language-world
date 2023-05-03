# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put the gripper around the door handle
    #  2. Pull the door open
    # First, the gripper needs to be positioned around the door handle, so the
    # robot can pull it open.
    if check("the robot's gripper is not around the door handle"):
        robot.move_gripper("around the door handle")
    # Pull the door open by moving the gripper away from the door handle.
    if check("the robot's gripper is around the door handle and is not horizontally aligned with the open position"):
        robot.move_gripper("horizontally aligned with the open position")