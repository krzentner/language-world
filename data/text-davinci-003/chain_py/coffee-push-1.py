
    # Steps:
    #  1. Put gripper near mug handle
    #  2. Grab mug with gripper
    #  3. Move mug to goal
    # First, put the gripper near the mug handle.
    if check("the robot's gripper is not near mug handle"):
        robot.put("gripper near mug handle")
    # As long as the gripper is near the mug handle but not grabbing it, try
    # grabbing the mug handle.
    if check("the robot's gripper is near mug handle and the robot's gripper is open"):
        robot.grab("mug handle")
    # If the mug is grabbed and the gripper is still near the mug handle, try
    # to move the mug to the goal.
    if check("the robot's gripper is near mug handle and the robot's gripper is closed"):
        robot.move("mug to goal")