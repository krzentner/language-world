
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull door open
    # We need to put the gripper above the door handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # Once the gripper is lined up above the door handle, we should be able to
    # grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.move_gripper("around the door handle")
    # Once the gripper is around the door handle, we can just pull the door
    # open.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("horizontally aligned with the door handle")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Push door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.move_gripper("vertically aligned with the door handle")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper from the side
    #  2. Push the button from the side
    # Because this is "side", we just need to line up the gripper from the side.
    # Line up the robot's grip