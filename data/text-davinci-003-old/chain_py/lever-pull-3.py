
    # Steps:
    #  1. Put gripper above the lever
    #  2. Grab the lever with the gripper
    #  3. Rotate the lever up
    # First, put the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper above lever")
    # If the lever becomes left of the gripper, go back to putting the gripper
    # above the lever.
    # Because the lever is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("lever is not left of the robot's gripper and lever is not forward aligned with the robot's gripper"):
        robot.grab("lever")
    # Now that the gripper is around the lever, just rotate the lever up.
    if check("the robot's gripper is around the lever"):
        robot.rotate("lever up")