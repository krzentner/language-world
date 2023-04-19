# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper around dial handle
    #  2. Turn the handle clockwise to unlock the door
    # First, put the gripper roughly around the dial handle.
    if check("the robot's gripper is not around the dial handle"):
        robot.move_gripper("near the dial handle", close_gripper=True)
    # If the gripper is around the dial handle, turn it clockwise to unlock the
    # door.
    if check("the robot's gripper is around the dial handle"):
        robot.turn_gripper("clockwise", revolutions=1.5) # The number of revolutions may need to be adjusted to match the specific lock.