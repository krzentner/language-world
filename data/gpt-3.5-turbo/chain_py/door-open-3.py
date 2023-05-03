# Steps:
    #  1. Put gripper around the door knob
    #  2. Pull the door open
    # If the gripper is not around the door knob, move it to the door knob.
    if check("the robot's gripper is not around the door knob"):
        robot.grab("door knob")
    # Once the gripper is around the door knob, we can pull the door open.
    if check("the robot's gripper is around door knob"):
        robot.pull("away from door")