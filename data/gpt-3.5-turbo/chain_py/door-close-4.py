# Steps:
    #  1. Put gripper around door handle
    #  2. Push the door closed to the target location
    # We need to get the gripper around the door handle to push it closed.
    if check("the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    # Once the gripper is around the handle, push the door closed.
    if check("the robot's gripper is around door handle"):
        robot.push("door closed to goal")