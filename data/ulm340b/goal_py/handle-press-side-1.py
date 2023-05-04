
    # Steps:
    #  1. Move the gripper above the handle
    #  2. Put the gripper around the handle
    #  3. Close the gripper and push down on the handle
    # First, move the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the gripper is above the handle but not lined up from the front, move
    # the gripper around the handle.
    if check("the robot's gripper is not forward aligned with handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # If the gripper is around the handle, try to close it and push down.
    if check("the robot's gripper is forward aligned with handle and the robot's gripper is open"):
        robot.move_gripper("near the handle")

# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Move the gripper above the handle
    #  2. Put the gripper around the handle
    #  3. Close the gripper and push down on the handle
    # First, move the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the gripper is above the handle but not lined up from the front, move
    # the gripper around the handle.
    if check("the robot's gripper is not forward aligned with handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # If the gripper is around the handle, try to close it and push down.
    if check("the robot's gripper is forward aligned with handle and the robot's gripper is open"):
        robot.move_gripper("near the handle")

# button-press: push the button
def button_press(robot):
    # Steps:
    #  1. Put the gripper above the button
    #  2. Close the gripper, pushing down on the button
    # First, put the gripper above the button.
    if check("the