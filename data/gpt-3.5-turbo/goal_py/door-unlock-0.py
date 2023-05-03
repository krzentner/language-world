# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial")
    # Once the gripper is around the dial, turn the dial to unlock the door.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("turn the dial")