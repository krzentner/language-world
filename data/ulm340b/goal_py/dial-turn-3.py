
    # Steps:
    #  1. Put gripper above the dial
    #  2. Move the gripper around the dial to turn it
    # If the gripper is not above the dial as seen from above, move it above the
    # dial.
    if check("the robot's gripper is not above dial"):
        robot.move_gripper("above the dial")
    # If the gripper is near the dial and the dial is left of the gripper, move
    # the gripper left to turn the dial.
    if check("the robot's gripper is near dial and the dial is right of the robot's gripper"):
        robot.move_gripper("horizontally aligned with the dial")

# switch-flip-down: flip the switch down
def switch_flip_down(robot):
    # Steps:
    #  1. Put gripper above the switch
    #  2. Move the gripper around the switch to flip it
    # If the gripper is not above the switch as seen from above, move it above
    # the switch.
    if check("the robot's gripper is not above switch"):
        robot.move_gripper("above the switch", close_gripper=True)
    # If the switch is right of the gripper, we can flip the switch by moving
    # the gripper right.
    if check("the robot's gripper is near switch and the switch is left of the robot's gripper"):
        robot.move_gripper("horizontally aligned with the switch")

# switch-flip-up: flip the switch up
def switch_flip_up(robot):
    # Steps:
    #  1. Put gripper above the switch
    #  2. Move the gripper around the switch to flip it
    # If the gripper is not above the switch as seen from above, move it above
    # the switch.
    if check("the robot's gripper is not above switch"):
        robot.move_gripper("above the switch")
    # If the switch is left of the gripper, we can flip the switch by moving
    # the gripper left.
    if check("the robot's gripper is near switch and the switch is right of the robot's gripper"):
        robot.move_gripper("horizontally aligned with the