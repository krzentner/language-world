
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Drop gripper around the door handle
    #  3. Pull open the door
    # We need to put the gripper above the door handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # Once the gripper is lined up above the door handle, we should be able to
    # grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    # Once the gripper is around the door handle, we can just pull the door
    # open.
    if check("the robot's gripper is around door handle"):
        robot.pull("away from door")

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
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# button-press-side: grab the button and push it to the left
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Grab the button
    #  3. Push the button to the left
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above