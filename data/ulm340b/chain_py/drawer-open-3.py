
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull drawer open
    # First, put the gripper mostly above the drawer handle.
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    # As long as the gripper is still vertically aligned with the drawer handle,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.pull("drawer open")

# light-switch-press: press the button from above
def light_switch_press(robot):
    # Steps:
    #  1. Line up the gripper above the button
    #  2. Push down on the button from the top
    # Because this is "press", we just need to line up the gripper.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near door handle"):
        robot.grab("door handle")
    # If the door is aligned with the gripper as seen from in front, we can push
