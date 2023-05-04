
    # Steps:
    #  1. Put gripper left of the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial counterclockwise
    # We need to put the gripper left of the dial before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not left of the dial"):
        robot.place("gripper left of dial")
    # Once the gripper is lined up with the dial, we should be able to grab the
    # dial by closing the gripper around it.
    if check("the robot's gripper is left of dial and the robot's gripper is open"):
        robot.grab("dial")
    # If the dial is still left of the robot's gripper, the robot probably didn't
    # grab it, so go back to trying to grab it.
    if check("the robot's gripper is closed and the dial is left of the robot's gripper"):
        robot.grab("dial")
    # We probably grabbed the dial, so go ahead and start turning it.
    if check("the robot's gripper is closed and the dial is not left of the robot's gripper"):
        robot.turn("dial counterclockwise")

# knob-turn: turn the knob clockwise
def knob_turn(robot):
    # Steps:
    #  1. Put gripper left of the knob
    #  2. Grab the knob with the gripper
    #  3. Turn the knob clockwise
    # We need to put the gripper left of the knob before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not left of the knob"):
        robot.place("gripper left of knob")
    # Once the gripper is lined up with the knob, we should be able to grab the
    # knob by closing the gripper around it.
    if check("the robot's gripper is left of knob and the robot's gripper is open"):
        robot.grab("knob")
    # If the knob is still left of the robot's gripper, the robot probably didn't
    # grab it, so go back to trying to grab it.
    if check