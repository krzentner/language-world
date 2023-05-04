
    # Steps:
    #  1. Reach towards the target
    #  2. Go above the wall
    # We want to reach to the target, but there's a wall in the way.
    # We should put the gripper above the wall to make sure it clears.
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal and go above the wall")

# turn-switch-left: turn the switch left to the goal angle
def turn_switch_left(robot):
    # Steps:
    #  1. Put gripper above knob
    #  2. Close gripper around knob
    #  3. Turn switch to goal angle
    #  4. Open gripper around knob
    # First, line up the robot's gripper with the knob as seen from above.
    if check("the robot's gripper is not vertically aligned with knob and the robot's gripper is not above knob"):
        robot.put("gripper above knob")
    # If the gripper is lined up with the knob from above, it might be able to
    # grab the knob by closing.
    if check("the robot's gripper is vertically aligned with knob and the robot's gripper is open"):
        robot.close("gripper around knob")
    # The gripper is grabbing the knob and we haven't reached the goal, so try
    # turning.
    if check("the robot's gripper is grabbing knob and the angle is not at goal angle"):
        robot.turn("knob left")
    # Now that the knob is turned as far as it needs to be, let go.
    if check("the robot's gripper is grabbing knob and the angle is at goal angle"):
        robot.open("gripper around knob")

# turn-switch-right: turn the switch right to the goal angle
def turn_switch_right(robot):
    # Steps:
    #  1. Put gripper above knob
    #  2. Close gripper around knob
    #  3. Turn switch to goal angle
    #  4. Open gripper around knob
    # First, line up the robot's gripper with the knob as seen from above.
    if check("the robot's gripper is not vertically aligned with knob and the robot's