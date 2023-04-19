# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper onto dial
    #  3. Turn dial to unlock the door
    # First, move the gripper above the dial.
    if check("the robot's gripper is not above dial"):
        robot.put("gripper above dial")
    # Then, drop the gripper onto the dial.
    if check("the robot's gripper is above dial and the robot's gripper is open"):
        robot.drop("gripper onto dial")
    # Finally, turn the dial to unlock the door.
    if check("the robot's gripper is around dial"):
        robot.turn("dial to unlock door")