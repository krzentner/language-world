# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door knob
    #  2. Push the door closed
    # If the gripper is not near the door knob, move it towards the door knob.
    if check("the robot's gripper is not near the door knob"):
        robot.move("gripper to door knob")
    # If the gripper is near the door knob but not around it, put it around the
    # door knob.
    if check("the robot's gripper is not around door knob"):
        robot.drop("gripper around door knob")
    # If the gripper is around the door knob, push the door closed.
    if check("the robot's gripper is around door knob"):
        robot.push("door closed to the target location")