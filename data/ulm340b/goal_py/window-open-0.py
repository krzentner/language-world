
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the the window handle is left of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the robot's gripper is left of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper right.
    if check("the robot's gripper is not near the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is starting to be left of the window handle, push
    # harder.
    if check("the window handle is left of the robot's gripper"):
        robot.move_gripper("left of the window handle")

# button-press-side: push the button down from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Push down on the button from the side
    # Because this is "side", we just need to line up the gripper from the side.
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not sideways aligned with button"):
        robot.move_gripper("sideways aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is sideways aligned with button"):
        robot.move_gripper("near the button")

# button-press-topdown-side: push the button down from the front, but first line up
#  the gripper from the side
def button_press_topdown_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Turn the gripper to face the button
    #  3. Push down on the button from the top
    # We can use a lot of button_press_side