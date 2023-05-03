
    # Steps:
    #  1. Put gripper near end of stick
    #  2. Grab the end of the stick with the gripper
    #  3. Pull the stick towards the robot
    #  4. Pull the thermos behind the stick
    # Since the stick is a long object and the gripper can't grab it around, try
    # to get the gripper close to the end of it, so we can grab it.
    if check("the robot's gripper is not near end of stick"):
        robot.put("gripper near end of stick")
    # With the gripper near the end of the stick, close the gripper so it can
    # grab it.
    if check("the robot's gripper is near end of stick and the gripper is open"):
        robot.grab("end of the stick")
    # Try to pull the stick towards the robot, which should also move the
    # thermos.
    if check("the robot's gripper is holding the end of the stick"):
        robot.pull("stick towards the robot")
    # Pull the thermos behind the stick
    if check("the robot's gripper is still holding the end of the stick"):
        robot.pull("thermos behind the stick")