
    # Steps:
    #  1. Put gripper left of the dial handle
    #  2. Grab the dial handle with the gripper
    #  3. Turn the dial handle right
    # If the gripper is left of the dial handle, move the gripper next to the
    # dial handle.
    if check("the robot's gripper is left of the dial handle"):
        robot.place("gripper next to dial handle")
    # Once the gripper is roughly in the same position as the dial handle, move
    # it up or down a bit to grab the dial handle.
    # We don't have to worry about aligning the gripper to be on top of the dial
    # handle, because the robot's gripper is at an angle.
    if check("the robot's gripper is in front of the dial handle"):
        robot.grab("dial handle")
    # Once we're grabbing the dial handle, move the gripper right to turn the
    # dial.
    if check("the robot's gripper is near the dial handle"):
        robot.rotate("dial handle right")

# knob-turn-left: turn the knob clockwise
def knob_turn_left(robot):
    # Steps:
    #  1. Put gripper left of the knob
    #  2. Grab the knob with the gripper
    #  3. Turn the knob clockwise
    # If the gripper is left of the knob, move the gripper next to the knob.
    if check("the robot's gripper is left of the knob"):
        robot.place("gripper next to knob")
    # Once the gripper is roughly in the same position as the knob, move it up
    # or down a bit to grab the knob.
    # We don't have to worry about aligning the gripper to be on top of the knob,
    # because the robot's gripper is at an angle.
    if check("the robot's gripper is in front of the knob"):
        robot.grab("knob")
    # Once we're grabbing the knob, rotate the gripper clockwise to turn the
    # knob.
    if check("the robot's gripper is around the knob"):
        robot.rotate("knob clockwise")

# knob-turn-right: turn the knob counter-clockwise