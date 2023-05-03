# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper around the door handle
    #  2. Pull the door open
    # If the the door handle is not yet within the gripper, we should move the gripper
    # near the door handle to start pulling
    if check("the door handle is not within the robot's gripper"):
        robot.move("gripper around door handle")
    # If the robot's gripper is around the door handle, we can pull the
    # door open.
    if check("the robot's gripper is around the door handle"):
        robot.pull("the door open")