# Steps:
    #  1. Put gripper around the door handle
    #  2. Pull the door open
    # We don't need to be careful about the direction we approach the door handle,
    # since the door handle is easily accessible.
    if check("the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    # Once the gripper is around the door handle, we can pull the door open.
    if check("the robot's gripper is around door handle"):
        robot.pull("door open")