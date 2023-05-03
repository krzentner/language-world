# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper above the lever
    #  2. Grab the lever
    #  3. Rotate the lever up
    # First, put the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.move_gripper("vertically aligned with the lever")
    # If the gripper isn't around the lever, put it around the lever.
    if check("the robot's gripper is not around lever and the robot's gripper is open"):
        robot.move_gripper("around the lever", close_gripper=True)
    # Once the gripper is around the lever, we can rotate the lever up.
    if check("the robot's gripper is around lever"):
        robot.move_gripper("lever rotated up")