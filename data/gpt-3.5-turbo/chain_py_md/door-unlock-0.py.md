# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the correct combination
    # In order to turn the dial, the gripper needs to be able to rotate around
    # the handle. First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.drop("gripper around dial")
    # Once the gripper is around the dial, we need to turn it to the correct
    # combination to unlock the door.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial to correct combination")