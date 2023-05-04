
    # Steps:
    #  1. Line up gripper with dial as seen from front
    #  2. Grasp the dial from the top
    #  3. Turn the dial clockwise
    # If the robot's gripper is not lined up from the front, line it up from the
    # front.
    if check("the robot's gripper is not forward aligned with dial"):
        robot.put("gripper above dial")
    # If the gripper is aligned from the front, grasp it from the top.
    if check("the robot's gripper is forward aligned with dial and the robot's gripper is open"):
        robot.grab("dial")
    # If the gripper is grasping the dial, turn it clockwise.
    if check("the robot's gripper is forward aligned with dial"):
        robot.turn("the dial clockwise")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push door closed
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # As long as the gripper is still vertically aligned with the door handle,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.push("door closed")

# knob-turn-right: turn the knob clockwise
def knob_turn_right(robot):
    # Steps:
    #  1. Put gripper in front of the knob
    #  2. Grasp the knob
    #  3. Turn the knob clockwise
    # We need to put the gripper in front of the knob so that we can grab it
    # without knocking it away.
    if check("the