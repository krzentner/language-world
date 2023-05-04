
    # Steps:
    #  1. Put gripper above button
    #  2. Push down on button from the top
    # First, put the gripper above the button, so that we don't accidentally
    # bump the coffee machine while reaching for the button.
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    # If the robot's gripper is above the button, we can just push it down.
    if check("the robot's gripper is above button"):
        robot.push("down on button")

# peg-unstack: grab and remove the top peg from the peg
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Pull up to remove the top peg
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg is to the left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # Once the gripper is around the peg, pull up to try to remove the peg from
    # the rest of the stack.
    if check("the robot's gripper is forward aligned with peg"):
        robot.unstack("peg")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push open the door
    # First, put the gripper above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
