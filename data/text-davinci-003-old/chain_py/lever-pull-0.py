
    # Steps:
    #  1. Put gripper above the lever
    #  2. Grab the lever with the gripper
    #  3. Rotate the lever up
    # First, put the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper above lever")
    # If the gripper isn't around the lever, move it to the lever.
    if check("the robot's gripper is not around the lever and the robot's gripper is open"):
        robot.grab("lever")
    # If the gripper is around the lever, rotate the lever up.
    if check("the robot's gripper is around the lever and the robot's gripper is closed"):
        robot.rotate("lever up")