
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # First, line up the robot's gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is near the button"):
        robot.move_gripper("around the button")

# button-press-side: push the button down from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper with the button from the side
    #  2. Push the button down from the side
    # We're pushing the button from the side, so we need to line the gripper up
    # with the button from the side.
    if check("the robot's gripper is not horizontally aligned with the button"):
        robot.move_gripper("above the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is horizontally aligned with the button"):
        robot.move_gripper("near the button")

# button-press-wall: push the button down from the side with a tall wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Line up the gripper with the button from the side
    #  2. Push the button down from the side
    # We're pushing the button from the side, so we need to line the gripper up
    # with the button from the side.
    if check("the robot's gripper is not horizontally aligned with the button"):
        robot.move_gripper("above the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is horizontally aligned with the button"):
        robot.move_gripper("near the button")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around