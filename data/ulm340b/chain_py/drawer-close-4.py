
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Push closed the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    # Once the gripper is around the drawer handle, we can just push the drawer
    # closed.
    if check("the robot's gripper is around drawer handle"):
        robot.push("towards drawer")

# button-press-side: push the button sideways from the front
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Drop gripper around the button
    #  3. Push the button in sideways
    # Because the robot's gripper is at an angle, it's harder to grab the button
    # if the gripper is not above it.
    # This is also the best position to make sure that the gripper is lined up
    # with the button before trying to grab it.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Once the gripper is aligned above the button, we should be able to grab
    # the button easily.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not around button"):
        robot.put("gripper around button")
    # As long as the gripper is still vertically aligned with the button, it's
    # probably pushing it sideways, so we can keep pushing.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is around button"):
        robot.push("button in sideways")

