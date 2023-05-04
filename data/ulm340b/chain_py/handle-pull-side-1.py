
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab handle with gripper
    #  3. Pull handle up
    # First, put the gripper above the handle.
    # If the handle is left of the gripper, put the gripper above the handle.
    if check("handle is not left of the robot's gripper and the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # If the gripper is right above the handle and not around it, grab the
    # handle.
    if check("the robot's gripper is forward aligned with handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    # As long as the gripper is still around the handle, keep pulling upwards.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push door closed
    # First, put the gripper above the door handle.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # Once the gripper is around the door handle, we can just push the door
    # closed.
    if check("the robot's gripper is around door handle"):
        robot.push("door closed")

# button-press-side: press the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push down on the button from the side
    # Because this is "side", we just need to line up the gripper from the side.
    # Line up the robot's gripper from