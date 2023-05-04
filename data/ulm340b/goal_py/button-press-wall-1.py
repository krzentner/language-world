
    # Steps:
    #  1. Line up the gripper as viewed from above, above the wall
    #  2. Move the gripper past the wall into the button
    # First, we need to line up the gripper from above the wall.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push past the wall down on the
    # button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above, above the wall
    #  2. Move the gripper past the wall into the button
    # First, we need to line up the gripper from above the wall.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push past the wall down on the
    # button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

# dial-turn: turn the dial clockwise 180 degrees
def dial_turn(robot):
    # Steps:
    #  1. Put the robot's gripper around the dial
    #  2. Turn the dial 180 degrees
    #  3. Move the gripper to the target location
    # If the robot's gripper isn't around the dial, put the gripper around the
    # dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # If the robot's gripper is around the dial and the dial is upright, start
    # to turn the dial clockwise.
    if check("the dial is vertically aligned with the robot's gripper"):
        robot