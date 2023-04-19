
    # Steps:
    #  1. Put gripper near door handle
    #  2. Push the door closed
    # We need to put the gripper near the door handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not near door handle"):
        robot.put("gripper near door handle")
    # Once the gripper is near the door handle, we should be able to just push
    # the door closed.
    if check("the robot's gripper is near door handle"):
        robot.push("door closed")