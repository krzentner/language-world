
    # Steps:
    #  1. Put the gripper above the plate
    #  2. Slide the plate to the goal
    # If the gripper isn't above the plate as seen from above, put it there.
    if check("the robot's gripper is not vertically aligned with plate"):
        robot.put("gripper above plate")
    # If the gripper is almost above the plate, slide the plate towards the
    # goal.
    if check("the robot's gripper is vertically aligned with plate"):
        robot.push("plate to goal")

# drawer-close: push the drawer closed
def drawer_close(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when opening the drawer).
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# switch-push: turn the switch on by pushing it forwards
def switch_push(robot):
    # Steps:
    #  1. Put gripper above switch
    #  2. Push switch forward
    # If the switch is behind the robot's gripper as seen from above, put the
    # gripper above the switch.
    if check("the robot's gripper is not vertically aligned with switch and switch is behind the robot's gripper"):
        robot.put("gripper above switch")
    # If the gripper is aligned with the switch, push the switch forward.
    if check("the robot's gripper is vertically aligned with switch"):
        robot.push("switch forward")

# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop