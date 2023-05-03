# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Pull the door handle towards the robot to open the door
    # First, put the gripper roughly around the door handle.
    if check("the robot's gripper is not around door handle"):
        robot.move_gripper("near the door handle", close_gripper=True)
    # Then, pull the door handle towards the robot to open the door.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("horizontally aligned with the door handle")