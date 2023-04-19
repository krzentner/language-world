

# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper above door dial
    #  2. Drop gripper around door dial
    #  3. Turn dial to lock the door
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the door dial"):
        robot.move_gripper("vertically aligned with the door dial")
    # If the gripper isn't around the dial, we can drop it around the dial.
    if check("the robot's gripper is not around door dial and the robot's gripper is open"):
        robot.move_gripper("around the door dial", close_gripper=True)
    # Now that the gripper is around the dial, we can turn the dial to lock the
    # door.
    if check("the robot's gripper is around door dial"):
        robot.move_gripper("counterclockwise")