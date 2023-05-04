
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push the button from the front
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is forward aligned with button and button is vertically aligned with robot's gripper"):
        robot.move_gripper("above the button")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push the button from the side
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is forward aligned with button and button is vertically aligned with robot's gripper"):
        robot.move_gripper("horizontally aligned with the button")

# peg-unstack: pick up the bottom peg of a stack of pegs
def peg_unstack(robot):
    # Steps:
    #  1. Line up the robot's gripper above the peg
    #  2. Move the robot's gripper below the peg, close to the table
    #  3. Close the gripper on the peg
    #  4. Lift the robot's gripper above the table, pulling the peg with it
    # We need to put the gripper above the peg before we can grab it, because of
    # the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the robot's