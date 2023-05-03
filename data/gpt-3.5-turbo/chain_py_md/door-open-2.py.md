# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Pull open the door
    # We need to put the gripper around the door handle before we can grab it.
    if check("the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    # Once the gripper is around the door handle, we can just pull the door open.
    if check("the robot's gripper is around door handle"):
        robot.pull("away from door")