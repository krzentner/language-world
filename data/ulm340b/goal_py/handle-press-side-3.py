
    # Steps:
    #  1. Put gripper to the side of the handle
    #  2. Push down on the handle
    # As long as the gripper isn't lined up with the handle from the side, line
    # it up.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Once the gripper is lined up with the handle from the side, push down on
    # the handle.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("below the handle", close_gripper=True)

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper to the side of the button
    #  2. Push the button from the side
    # As long as the gripper isn't lined up with the button from the side, line
    # it up.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with the button")
    # Once the gripper is lined up with the button from the side, push the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.move_gripper("vertically aligned with the button")

# door-close: close the door
def door_close(robot):
    # Steps:
    #  1. Put gripper to the side of the door handle
    #  2. Push closed the door
    # As long as the gripper isn't lined up with the door handle from the side,
    # line it up.
    if check("the robot's gripper is not horizontally aligned with the door handle"):
        robot.move_gripper("horizontally aligned with the door handle")
    # Once the gripper is lined up with the door handle, push it closed.
    if check("the robot's gripper is horizontally aligned with the door handle"):
        robot.move_gripper("below the door handle", close_gripper=True)

# handle-press-topdown: push down the handle from the top
def handle_press_topdown(robot):
    #