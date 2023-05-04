
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Drop gripper around the door handle
    #  3. Pull open the door
    # We need to put the gripper above the door handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # Once the gripper is lined up above the door handle, we should be able to
    # grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around the door handle"):
        robot.move_gripper("around the door handle")
    # Once the gripper is around the door handle, we can just pull the door
    # open.
    if check("the robot's gripper is around the door handle"):
        robot.move_gripper("horizontally aligned with the door handle")

# door-close: push the door close
def door_close(robot):
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Put the gripper forward aligned with the door handle
    #  3. Push the door closed
    # We need to put the gripper above the door handle before we can start
    # pushing it, because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # Once the gripper is lined up above the door handle, we should be able to
    # start pushing the door handle by lining up the gripper from in front.
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not forward aligned with the door handle"):
        robot.move_gripper("forward aligned with the door handle")
    # Once the gripper is lined up with the door handle, we can just push the
    # door close.
    if check("the robot's gripper is forward aligned with the door handle"):
        robot.move_gripper("below the door handle")