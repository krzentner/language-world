
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Slide the handle up
    # Put the gripper mostly above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle is forward aligned with the gripper, grab it by closing the
    # gripper.
    if check("the robot's gripper is forward aligned with the handle and the robot's gripper is open"):
        robot.move_gripper("around the handle")
    # Once we have the handle, slide it up.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("horizontally aligned with the handle")

# handle-pull-topdown: pull up the handle from the top
def handle_pull_topdown(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Slide the handle up
    # First, put the gripper mostly above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle is forward aligned with the gripper, grab it by closing the
    # gripper.
    if check("the robot's gripper is forward aligned with the handle and the robot's gripper is open"):
        robot.move_gripper("around the handle")
    # Once we have the handle, slide it up.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("horizontally aligned with the handle")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Drop the gripper around the button
    #  3. Push down on the button
    # First, put the gripper mostly above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_