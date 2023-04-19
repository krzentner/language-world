
    # Steps:
    #  1. Put gripper above lever
    #  2. Grab the lever
    #  3. Rotate the lever up
    # First, put the gripper above the lever.
    if check("the robot's gripper is not above the lever"):
        robot.put("gripper above lever")
    # If the lever is left of the gripper, go back to putting the gripper
    # above the lever.
    # Because the lever is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("lever is not left of the robot's gripper and lever is not forward aligned with the robot's gripper"):
        robot.grab("lever")
    # As long the gripper is still mostly around the lever and the lever isn't
    # rotated up, rotate the lever up.
    if check("the robot's gripper is forward aligned with the lever and the lever is not up"):
        robot.rotate("lever up")