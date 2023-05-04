
    # Steps:
    #  1. Put the gripper near the handle's right side
    #  2. Move the gripper down to grab the handle
    #  3. Pull up on the handle
    # Put the gripper above the handle before we can grab it, because of the
    # angle of the robot's gripper.
    if check("the robot's gripper is not above handle"):
        robot.grab("handle")
    # If the gripper is still near the handle but not around it, drop it down
    # around the handle.
    if check("the robot's gripper is near handle and the robot's gripper is not around handle"):
        robot.grab("handle")
    # As long as the gripper is around the handle, it's being opened, so keep
    # pulling.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")

# handle-pull-up: pull up the handle from above
def handle_pull_up(robot):
    # Steps:
    #  1. Put the gripper above the handle
    #  2. Move the gripper down to grab the handle
    #  3. Pull up on the handle
    # Put the gripper above the handle before we can grab it, because of the
    # angle of the robot's gripper.
    if check("the robot's gripper is not above handle"):
        robot.grab("handle")
    # If the gripper is still above the handle but not around it, drop it down
    # around the handle.
    if check("the robot's gripper is above handle and the robot's gripper is not around handle"):
        robot.grab("handle")
    # As long as the gripper is around the handle, it's being opened, so keep
    # pulling.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")

# drawer-close-side: push the drawer closed from the side
def drawer_close_side(robot):
    # Steps:
    #  1. Put gripper on the side of the drawer handle
    #  2. Move gripper around drawer handle
    #  3. Push the drawer closed
    #