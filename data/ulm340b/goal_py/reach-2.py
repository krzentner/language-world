
    # Steps:
    #  1. Move gripper above the target location
    #  2. Move gripper to the target location
    # If the robot's gripper is above the target location, move it near the
    # target location.
    if check("the robot's gripper is vertically aligned with the target location and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # If the robot's gripper is not vertically aligned with the target location,
    # move it to be aligned from above.
    if check("the robot's gripper is not vertically aligned with the target location"):
        robot.move_gripper("vertically aligned with the target location", close_gripper=True)

# turn-dial: turn the dial clockwise
def turn_dial(robot):
    # Steps:
    #  1. Move gripper close to dial
    #  2. Turn dial
    # If the robot's gripper is not around the dial, move it around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial")
    # If the robot's gripper is around the dial, turn the dial.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("right of the dial")

# turn-switch-left: turn the switch left
def turn_switch_left(robot):
    # Steps:
    #  1. Move gripper close to dial
    #  2. Turn dial
    # If the robot's gripper is not around the switch, move it around the switch.
    if check("the robot's gripper is not around the switch"):
        robot.move_gripper("around the switch")
    # If the robot's gripper is around the switch, turn the switch.
    if check("the robot's gripper is around the switch"):
        robot.move_gripper("right of the switch")

# turn-switch-right: turn the switch right
def turn_switch_right(robot):
    # Steps:
    #  1. Move gripper close to dial
    #  2. Turn dial
    # If the robot's gripper is not around