# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper around door knob
    #  2. Turn the dial to the right until the lock clicks open
    # First, put the gripper around the door knob.
    if check("the robot's gripper is not around door knob and the robot's gripper is open"):
        robot.drop("gripper around door knob")
    # Turn the dial to the right until the lock clicks open.
    # Check if the door is locked, if it is then start turning, else move on.
    if check("the door is locked"):
        while check("the lock is not open"):
            robot.turn("dial to the right")