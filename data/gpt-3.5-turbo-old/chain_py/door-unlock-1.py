# Steps:
    #  1. Put gripper around door handle
    #  2. Turn the dial to unlock the door
    # We need to put the gripper around the door handle first in order to turn
    # the dial.
    if check("the robot's gripper is not around the door handle"):
        robot.drop("gripper around door handle")
    # Once the gripper is around the door handle, we can turn the dial to unlock
    # the door.
    if check("the robot's gripper is around the door handle"):
        robot.turn("dial to unlock the door")