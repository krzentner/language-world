

The program should include steps for the robot to put its gripper around the dial on the door, rotate the dial with the gripper, and then move the gripper away from the dial once the door is locked.

# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper above door dial
    #  2. Drop gripper around door dial
    #  3. Rotate the dial with the gripper
    #  4. Move gripper away from the dial
    # First, put the gripper (roughly) above the door dial.
    if check("the robot's gripper is not above door dial"):
        robot.move_gripper("above the door dial")
    # Once the gripper is above the door dial, we need to put it around the dial
    # so we can rotate it.
    if check("the robot's gripper is not around door dial"):
        robot.move_gripper("around the door dial", close_gripper=True)
    # If the gripper is around the dial, we can rotate it to turn the dial.
    if check("the robot's gripper is around door dial"):
        robot.move_gripper("clockwise or counterclockwise", close_gripper=True)
    # Once the dial is in the correct place, we can move the gripper away from
    # the dial.
    if check("the door is locked"):
        robot.move_gripper("above the door dial")