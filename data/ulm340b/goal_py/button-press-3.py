
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Line up the gripper as viewed from in front
    #  3. Push the button from in front
    # We need to line up the gripper as viewed from above and as viewed from
    # in front so that we can press the button accurately.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Now that the gripper is aligned, push the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("around the button")

# door-close: close the door
def door_close(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Close the door by moving gripper right
    # First, put the gripper around the door handle.
    if check("the robot's gripper is not around door handle and the robot's gripper is open"):
        robot.move_gripper("around the door handle", close_gripper=True)
    # Once the gripper is around the door handle, we can close the door.
    # We do this by moving the robot's gripper right.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.move_gripper("around the door handle")

# slider-move-right: slide the object to the right
def slider_move_right(robot):
    # Steps:
    #  1. Put gripper above the slider
    #  2. Close gripper around slider
    #  3. Move slider to the right
    # If the slider is not below the robot's gripper, move the gripper
    # vertically above it.
    if check("the robot's gripper is not vertically aligned with the slider and the robot's gripper is not around the slider"):
        robot.move_gripper("vertically aligned with the slider", close_gripper=True)
    # If the