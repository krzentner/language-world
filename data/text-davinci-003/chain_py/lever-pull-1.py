
    # Steps:
    #  1. Put gripper above the lever
    #  2. Grab the lever with the gripper
    #  3. Pull the lever up
    #  Put the gripper near the lever so we can grab it.
    if check("the robot's gripper is not vertically aligned with the lever and the robot's gripper is not near lever"):
        robot.put("gripper near lever")
    # If the gripper is around the lever, grab it. Otherwise, try to get closer
    # to the lever.
    if check("the robot's gripper is vertically aligned with the lever and the robot's gripper is not grabbing lever"):
        robot.grab("lever")
    # Once the gripper is grabbing the lever, we can pull it upwards
    if check("the robot's gripper is grabbing lever"):
        robot.pull("lever up")