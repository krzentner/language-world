
    # Steps:
    #  1. Put gripper right of the faucet handle
    #  2. Turn the faucet handle left
    # First, put the robot's gripper right of the faucet handle.
    if check("the faucet handle is left of the robot's gripper"):
        robot.move("gripper to right of faucet handle")
    # Now that the faucet handle is right of the robot's gripper, we can just
    # turn it.
    if check("the faucet handle is right of the robot's gripper"):
        robot.turn("the faucet handle left")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg down into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long as the gripper is still mostly around the peg and the peg isn't
    # lined up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the front, insert it.
    if check("peg is vertically aligned with hole"):
        robot.insert("peg into hole")

# button-press-side: push the button left to right
def button_press_side(robot):
    # Steps:
    #  1. Put gripper left of the button
    #  2. Push