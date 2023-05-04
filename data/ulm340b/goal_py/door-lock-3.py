
    # Steps:
    #  1. Put gripper around door dial
    #  2. Move the door dial to the right
    #  3. Move the door dial to the left
    # First, put the gripper around the door dial, roughly in the direction
    # where the robot's gripper can turn it.
    if check("the robot's gripper is not around the door dial"):
        robot.move_gripper("around the door dial")
    # As long as the gripper is already around the door dial, we should be able
    # to turn it by moving the gripper.
    if check("the robot's gripper is left of the door dial"):
        robot.move_gripper("right of the door dial")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Push the door closed
    # We don't need to be careful about the direction here, because the door
    # handle is large.
    if check("the robot's gripper is not near door handle"):
        robot.move_gripper("around door handle")
    # If the robot's gripper is around the door handle, push the door closed.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("vertically aligned with door handle")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Put gripper in front of the button
    #  3. Push the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button", close_gripper=True)
    # Then, put the gripper in front of the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with the button and the robot