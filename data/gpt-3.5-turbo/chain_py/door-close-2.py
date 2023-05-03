# Steps:
    #  1. Put gripper near door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it so that it is.
    # We don't have to be too exact about the direction, since we're just pushing
    # the door closed.
    if check("the robot's gripper is not near the door handle"):
        robot.move("the gripper near the door handle")
    # Once the gripper is near the door handle, we can push the door closed.
    if check("the robot's gripper is near the door handle"):
        robot.push("the door closed to the goal")