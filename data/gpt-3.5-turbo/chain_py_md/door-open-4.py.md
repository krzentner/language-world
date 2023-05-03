# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Pull the door towards the robot
    # First, put the gripper roughly around the door handle.
    if check("the robot's gripper is not around door handle"):
        robot.place("gripper around door handle")
    # Once the gripper is around the door handle, we can pull the door towards
    # the robot to open it.
    if check("the robot's gripper is around door handle"):
        robot.pull("door towards robot")