
    # Steps:
    #  1. Put gripper near the lever
    #  2. Push down the lever
    # First, move the gripper to near the lever.
    if check("the robot's gripper is not near lever"):
        robot.put("gripper near lever")
    # Once the gripper is near the lever, we can just push it up.
    if check("the robot's gripper is near lever"):
        robot.push("lever up")