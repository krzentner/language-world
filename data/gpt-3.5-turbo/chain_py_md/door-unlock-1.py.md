# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Line up gripper above dial
    #  2. Turn the dial
    # We need to make sure the gripper is lined up directly above the dial to be
    # able to grasp it.
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    # Once the gripper is lined up above the dial, we can grab it by closing the
    # gripper around it.
    if check("the robot's gripper is above the dial and the gripper is open"):
        robot.grab("dial")
    # Now that we have a good grip on the dial, we can turn it to unlock the
    # door.
    if check("the gripper is around the dial"):
        robot.turn("dial to unlock the door")