
    # Steps:
    #  1. Align the gripper as seen from the front
    #  2. Press down on the handle from the side
    # First, line up the gripper as seen from the front.
    if check("the robot's gripper is not forward aligned with handle"):
        robot.move_gripper("forward aligned with the handle", close_gripper=True)
    # If the handle is in front of the gripper now, push it down from the side.
    if check("the robot's gripper is forward aligned with handle"):
        robot.move_gripper("near the handle")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Align the gripper as seen from the front
    #  2. Push the door closed
    # First, line up the gripper as seen from the front.
    if check("the robot's gripper is not forward aligned with door handle"):
        robot.move_gripper("forward aligned with the door handle")
    # If the door handle is in front of the gripper now, push it closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.move_gripper("near the door handle")

# light-switch-side: turn on the light switch
def light_switch_side(robot):
    # Steps:
    #  1. Align the gripper with the light switch
    #  2. Push the light switch sideways
    # First, align the gripper with the light switch.
    # We use forward aligned, because it's more likely to end up aligned this
    # way.
    if check("the robot's gripper is not forward aligned with the light switch"):
        robot.move_gripper("forward aligned with the light switch", close_gripper=True)
    # If the light switch is in front of the gripper, push it sideways.
    if check("the robot's gripper is forward aligned with the light switch"):
        robot.move_gripper("near the light switch")

# handle-press: press the handle down from above
def handle_press(robot):
    # Steps:
    #  1. Align the gripper as seen from above
    #  2. Press down on