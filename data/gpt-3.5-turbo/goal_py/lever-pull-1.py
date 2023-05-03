# Steps:
    #  1. Put gripper above the lever
    #  2. Grab the lever with the gripper
    #  3. Rotate the gripper up to pull the lever
    # First, put the gripper above the lever
    if check("the robot's gripper is not above the lever"):
        robot.move_gripper("above the lever")
    # If the gripper is above the lever, grab the lever with the gripper
    if check("the robot's gripper is above the lever and the robot's gripper is not around the lever"):
        robot.move_gripper("around the lever", close_gripper=True)
    # Once the gripper is around the lever, we can rotate it up to pull the lever
    if check("the robot's gripper is around the lever and the lever is not rotated up"):
        robot.move_gripper("vertically aligned with the lever")