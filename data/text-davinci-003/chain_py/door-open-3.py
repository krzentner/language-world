
    # Steps:
    #  1. Put the gripper left of the door handle
    #  2. Grab the door handle
    #  3. Pull the door open
    # To open the door we need to grab the door handle.
    #
    # To do this, first put the gripper around the left of the door handle
    if check("the robot's gripper is not left of door handle"):
        robot.move("gripper to left of door handle")
    # If the gripper is lined up with the door handle but not near it, move the
    # gripper down to the door handle.
    if check("the robot's gripper is left of door handle and the robot's gripper is not near door handle"):
        robot.drop("gripper to door handle")
    # If the gripper is near the door handle, grab it and pull the door open.
    if check("the robot's gripper is near door handle and the robot's gripper is closed"):
        robot.pull("away from door")