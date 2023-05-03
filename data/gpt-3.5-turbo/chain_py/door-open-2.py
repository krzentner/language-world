# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper around door knob
    #  2. Pull the door open
    # If the gripper is not around the door knob, we need to move it there.
    if check("the robot's gripper is not around door knob"):
        robot.grab("door knob")
    # Once the gripper is around the door knob, we can pull the door open.
    if check("the robot's gripper is around door knob"):
        robot.pull("door open")