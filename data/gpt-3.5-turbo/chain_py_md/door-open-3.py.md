# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper around door knob
    #  2. Pull door open
    # To open the door, we need to grab onto the door knob and pull it towards
    # us.
    # If the gripper is not near the door knob, move it there.
    if check("the robot's gripper is not near door knob"):
        robot.put("the gripper around the door knob")
    # Once the gripper is around the door knob, we can just pull the door open.
    if check("the robot's gripper is around door knob"):
        robot.pull("door towards robot")