
    # Steps:
    #  1. Put gripper above lever
    #  2. Drop gripper around lever
    #  3. Pull lever up
    # First, put the gripper above the lever as viewed from the side.
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    # If the gripper is above the lever and the gripper isn't around it yet,
    # close the gripper around it.
    if check("the robot's gripper is vertically aligned with lever and the robot's gripper is not around lever"):
        robot.grab("lever")
    # If the lever is now closer to the robot's gripper, we can pull it up.
    # Pull the lever up.
    if check("the robot's gripper is around lever"):
        robot.pull("lever up")