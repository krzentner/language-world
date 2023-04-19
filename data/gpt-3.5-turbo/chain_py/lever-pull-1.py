# Steps:
    #  1. Put gripper roughly around lever
    #  2. Grab the lever with the gripper
    #  3. Rotate the gripper upwards to pull the lever
    # First, put the gripper roughly around the lever.
    if check("the robot's gripper is not around lever"):
        robot.put("gripper around lever")
    # Once the gripper is around the lever, grab it.
    if check("the robot's gripper is around lever and the robot's gripper is open"):
        robot.close("gripper around lever")
    # Once the gripper is around the lever and closed, rotate the gripper upwards
    # to pull the lever.
    if check("the robot's gripper is around lever and the robot's gripper is closed"):
        robot.rotate("lever upwards")