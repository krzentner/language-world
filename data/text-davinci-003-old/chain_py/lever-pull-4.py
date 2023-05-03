
    # Steps:
    #  1. Put gripper above lever
    #  2. Push gripper against one side of lever
    #  3. Pull lever up
    # First, we need to get the gripper in a good position to start pushing.
    # Move the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    # Move the gripper so that it's in contact with the side of the lever.
    if check("the robot's gripper is vertically aligned with lever and the robot's gripper is not in contact with lever"):
        robot.push("gripper against one side of lever")
    # If the gripper is pressed against one side of the lever, just pull it
    # until it's in the desired position.
    if check("the robot's gripper is in contact with lever"):
        robot.pull("lever up")