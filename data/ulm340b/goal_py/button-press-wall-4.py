
    # Steps:
    #  1. Line up the gripper with the button as viewed from in front
    #  2. Push the button from the side
    # First, line up the robot's gripper with the button from in front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with the button", close_gripper=True)
    # Now the gripper is lined up with the button, just push it.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.move_gripper("near the button")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper with the button as viewed from the side
    #  2. Push the button from the side
    # First, line up the robot's gripper with the button from the side.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with the button", close_gripper=True)
    # Now the gripper is lined up with the button, just push it.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.move_gripper("near the button")

# box-close-topdown: push the lid closed on the box from above
def box_close_topdown(robot):
    # Steps:
    #  1. Put the gripper above the lid
    #  2. Lower the gripper onto the lid
    #  3. Push the lid closed
    # Put the gripper above the lid.
    if check("the robot's gripper is not vertically aligned with box lid"):
        robot.move_gripper("vertically aligned with the box lid", close_gripper=True)
    # Put the gripper on top of the lid.
    if check("the robot's gripper is not above box lid"):
        robot.move_gripper("above the box lid")
    # Now, push the lid closed.
    if check("the robot's gripper is above box lid"):
        robot.move_gripper("horizontally aligned with the box lid")

# box-open-topdown: open