# Steps:
    #  1. Put gripper beside the handle
    #  2. Slide the gripper down to the handle
    #  3. Push down on the handle from the side
    # First, put the gripper beside the handle.
    if check("the robot's gripper is not beside the handle"):
        robot.move("gripper beside handle")
    # Move the gripper down to the handle.
    if check("the robot's gripper is beside handle but not near handle"):
        robot.move("gripper down to handle")
    # Push down on the handle from the side.
    if check("the robot's gripper is near handle"):
        robot.push("down on handle from the side")