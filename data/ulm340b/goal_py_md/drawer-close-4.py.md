

<div class="well well-green">
The above is an example from [Instructions with Natural Language Priors](https://arxiv.org/abs/2004.11763).
</div>

"""

# drawer-close: push the drawer close
def drawer_close(robot):
    pass

# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Move the gripper near the drawer handle
    #  2. Push the handle inside to close the drawer
    if check("the robot's gripper is not near drawer handle"):
        robot.move_gripper("near drawer handle")
    if check("the robot's gripper is near drawer handle"):
        robot.move_gripper("above drawer handle")

# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Move the gripper near the drawer handle
    #  2. Push the handle inside to close the drawer
    if check("the robot's gripper is not near drawer handle"):
        robot.move_gripper("near drawer handle")
    # Now that the robot's gripper is near drawer handle, we should be able to
    # close it by moving the gripper in front of drawer handle.
    if check("the robot's gripper is not in front of drawer handle"):
        robot.move_gripper("in front of drawer handle", close_gripper=True)

# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Move the gripper near the drawer handle
    #  2. Push the handle inside to close the drawer
    if check("the robot's gripper is not in front of drawer handle"):
        robot.move_gripper("in front of drawer handle")
    # Now that the robot's gripper is in front of drawer handle, we should be
    # able to close it by moving the gripper to the side of drawer handle.
    if check("the robot's gripper is not left of drawer handle"):
        robot.move_gripper("left of drawer handle")

# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Move the gripper near the drawer handle