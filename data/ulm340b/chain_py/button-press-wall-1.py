
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push the button sideways
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Because the button has a wall in front of it, we can't just push down.
    # So, as long as the button is in front of the gripper, move the gripper
    # into the button sideways.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("the button sideways")

# button-press-side: push the button in from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push the button sideways
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Because the button doesn't have anything in front of it, we can just move
    # the gripper into the button sideways.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("the button sideways")

# button-press-corner: push the button in from a corner
def button_press_corner(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push the button sideways
    # First, put the gripper above the button.
    # This also puts the gripper near the button, so we don't have to check for
    # that later.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Line up the robot's gripper above the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("the button sideways")

# peg-insert-tip: grab the peg and insert it into the hole from the tip
def peg_insert_tip(robot):
    # Steps:
    #  1. Put gripper above the peg
    # 