
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with coffee button"):
        robot.move_gripper("vertically aligned with the coffee button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with coffee button"):
        robot.move_gripper("near the coffee button")

# turn-switch: flip the switch into the correct position
def turn_switch(robot):
    # Steps:
    #  1. Put gripper above the switch
    #  2. Drop gripper around switch
    #  3. Flip switch
    # First, put the gripper above the switch.
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.move_gripper("vertically aligned with the switch")
    # As long the gripper is lined up above the switch, closing it should line it
    # up all the way.
    if check("the robot's gripper is above switch"):
        robot.move_gripper("near the switch")

# peg-unstack: unstack the bottom peg and place it at the target location
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Move the peg to the target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with top peg"):
        robot.move_gripper("vertically aligned with the top peg")
    # If the gripper is lined up above the peg, close the gripper around the peg.
    if check("the robot's gripper is vertically aligned with top peg and the robot's gripper is not below top peg"):
        robot.move_gripper("near the top peg")
    # If the gripper is around the peg, move the peg to the target location.
 