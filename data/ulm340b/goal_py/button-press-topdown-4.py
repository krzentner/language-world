
    # Steps:
    #  1. Put gripper vertically aligned with the button
    #  2. Drop gripper to the button to push it down
    #  3. Drop the gripper again
    if check("the robot's gripper is not above button"):
        robot.move_gripper("above the button", close_gripper=True)
    if check("the robot's gripper is around button"):
        robot.move_gripper("horizontally aligned with button")

# drawer-close: push the drawer closed
def drawer_close(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Grab drawer handle with the gripper
    #  3. Push the drawer closed
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    # Once the gripper is around the drawer handle, we can just pull the drawer
    # open.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("almost forward aligned with the drawer handle")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper vertically aligned with the button
    #  2. Drop gripper to the button to push it down
    #  3. Drop the gripper again
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("above the button", close_gripper=True)
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("forward aligned with button")

# door-close: pull the door closed
def door_