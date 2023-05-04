
    # Steps:
    #  1. Put gripper above the coffee machine button
    #  2. Push down on the button
    # First, we need to put the gripper above the button.
    # The button is really small, so don't try to do it without good alignment.
    # If the robot's gripper is not vertically lined up with button, we should
    # move the gripper near button to start pushing.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # If the robot's gripper is near button, we can push the button.
    if check("the robot's gripper is near button"):
        robot.move_gripper("above the button", close_gripper=True)

# peg-unstack-side: grab the peg and lift it off of the block
def peg_unstack_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Lift the peg off the block
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg isn't lifted
    # up, lift up the peg.
    if check("the robot's gripper is forward aligned with the peg and the peg is not above the block"):
        robot.move_gripper("above the peg")

# pick-wall-place-side: pick up the puck and place it down on the side
def pick_wall_place_side(robot):
    # Steps:
    #  1. Put