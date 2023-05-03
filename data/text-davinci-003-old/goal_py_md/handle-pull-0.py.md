

Steps:
  1. Put gripper roughly above handle
  2. Drop gripper around handle
  3. Pull the handle up

# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper roughly above handle
    #  2. Drop gripper around handle
    #  3. Pull the handle up
    # We need to put the gripper roughly above the handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Once the gripper is lined up above the handle, we should be able to grab 
    # the handle by moving the gripper down and around it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, we can just pull it up.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("above the handle")