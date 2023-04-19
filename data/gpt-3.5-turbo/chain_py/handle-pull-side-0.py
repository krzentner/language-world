# Steps:
    #  1. Put the gripper to the side of the handle
    #  2. Grab the handle with the gripper
    #  3. Pull up on the handle
    # First, put the gripper to the side of the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper to side of handle")
    # Once the gripper is near the handle, grab the handle with the gripper.
    if check("the robot's gripper is near the handle and the gripper is not closed around the handle"):
        robot.grab("handle")
    # With the handle now grabbed, pull up on it to open or lift the object it's attached to.
    if check("the robot's gripper is closed around the handle"):
        robot.pull("handle upwards")