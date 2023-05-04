
    # Steps:
    #  1. Put gripper above button
    #  2. Push gripper into button
    #  3. Continue pushing gripper
    # The robot can push the button by pushing it from above.
    # If the button is not below the gripper as seen from above, move the gripper
    # above the button.
    if check("the robot's gripper is not above the button and the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    # If the gripper is aligned with the button but not near it, move the gripper
    # down to the button to push it.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button"):
        robot.push("gripper into button")
    # If the gripper is near the button, we probably pushed the button.
    # As long as we are still vertically aligned with the button, it should still
    # be pressed, so keep pushing it.
    if check("the robot's gripper is near the button and the robot's gripper is vertically aligned with the button"):
        robot.push("gripper into button")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    # If the door is aligned with the gripper as seen from in front, we can push
    # the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# button-press-side: push the button sideways from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper next to the button
    #  2. Push button
    # If the button is not