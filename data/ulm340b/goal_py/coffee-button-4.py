
    # Steps:
    #  1. Line up the gripper as viewed from in front
    #  2. Push the button straight in from in front
    # First, line up the gripper from in front.
    if check("the robot's gripper is not horizontally aligned with coffee button"):
        robot.move_gripper("horizontally aligned with coffee button")
    # If the gripper is lined up with the button, push the button in.
    if check("the robot's gripper is not forward aligned with coffee button"):
        robot.move_gripper("forward aligned with coffee button")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Push the button in from the side
    # First, line up the gripper from the side.
    if check("the robot's gripper is not around the button"):
        robot.move_gripper("around the button")
    # If the gripper is lined up with the button, push the button in.
    if check("the robot's gripper is around the button"):
        robot.move_gripper("almost vertically aligned with button")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.move_gripper("around the door handle")

# peg-unstack-side: slide the stacked pegs off sideways
def peg_unstack_side(robot):
    # Steps:
    #  1. Put the gripper to the side of