
    # Steps:
    #  1. Put gripper above the button
    #  2. Put gripper around the button
    #  3. Push the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # Now put the gripper around the button.
    if check("the robot's gripper is not around the button"):
        robot.grab("the button")
    # Because we don't need to press the button very hard or for very long,
    # pushing the gripper forward should be enough.
    if check("the robot's gripper is around the button"):
        robot.push("the button")

# bottle-insert: put the bottle into the bottle opener
def bottle_insert(robot):
    # Steps:
    #  1. Put gripper above bottle
    #  2. Grab bottle with gripper
    #  3. Line up the bottle
    #  4. Push the bottle down into the bottle opener
    # First, put the gripper above the bottle.
    if check("the robot's gripper is not vertically aligned with bottle"):
        robot.put("gripper above bottle")
    # Now grab the bottle with the gripper.
    # Because the bottle is long and thin, check if the gripper is aligned with
    # it from the front instead of around it.
    if check("the robot's gripper is vertically aligned with bottle and bottle is not forward aligned with the robot's gripper"):
        robot.grab("bottle")
    # Once the gripper is around the bottle, line up the bottle.
    if check("the robot's gripper is forward aligned with bottle and bottle is not aligned with bottle opener"):
        robot.align("bottle with bottle opener")
    # Once the bottle is aligned, push the bottle down into the bottle opener.
    if check("bottle is aligned with bottle opener"):
        robot.push("bottle into bottle opener")

# peg-unstack: remove the top peg from the stack
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper above peg stack
    #  2. Grab the top peg
    #  3. Pull up