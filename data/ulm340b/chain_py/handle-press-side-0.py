
    # Steps:
    #  1. Put gripper above the handle
    #  2. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above the handle")
    # Once the gripper is above the handle, we can just push down on it.
    if check("the robot's gripper is above the handle"):
        robot.push("handle down")

# handle-press: push the handle from the front
def handle_press(robot):
    # Steps:
    #  1. Put gripper forward of the handle
    #  2. Push the handle
    # First, put the gripper roughly forward of the handle.
    if check("the robot's gripper is not forward of the handle"):
        robot.put("gripper forward of the handle")
    # If the gripper is close to aligned with the handle from the front, we can
    # start pushing.
    if check("the robot's gripper is almost forward aligned with handle"):
        robot.move("gripper forward")
    # Now that the gripper is aligned with the handle from the front, we can
    # push the handle.
    if check("the robot's gripper is forward aligned with handle"):
        robot.push("handle forward")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper near door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near door handle"):
        robot.grab("door handle")
    # If the gripper is aligned with the door as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# handle-pull-side: pull the handle towards you from the side
def handle_pull_side(robot):
   