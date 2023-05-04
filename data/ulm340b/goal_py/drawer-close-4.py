
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Push the drawer closed
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    # Once the gripper is around the drawer handle, we can just push the drawer
    # closed.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle", close_gripper=True)

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push the door closed
    # We need to put the gripper above the door handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # Once the gripper is lined up above the door handle, we should be able to
    # grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.move_gripper("around the door handle")
    # Once the gripper is around the door handle, we can just push the door
    # closed.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)

# pick-place-wall: