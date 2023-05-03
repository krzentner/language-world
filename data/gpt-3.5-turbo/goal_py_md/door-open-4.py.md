# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Drop gripper around the door handle
    #  3. Pull the door open
    # We need to put the gripper above the door handle before we can grab it, because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # Once the gripper is lined up above the door handle, we should be able to grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around the door handle"):
        robot.move_gripper("around the door handle")
    # Once the gripper is around the door handle, we can pull the handle towards the robot to open the door.
    if check("the robot's gripper is around the door handle"):
        robot.move_gripper("horizontally aligned with the door handle")