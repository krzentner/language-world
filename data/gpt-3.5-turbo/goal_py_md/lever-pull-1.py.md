# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put the gripper around the lever
    #  2. Rotate the gripper to rotate the lever
    # If the gripper is not around the lever, move it to the lever.
    if check("the robot's gripper is not around the lever and the robot's gripper is not vertically aligned with the lever"):
        robot.move_gripper("almost vertically aligned with the lever", close_gripper=True)
    # Once the gripper is around the lever, we can rotate it to pull the lever up.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("horizontally aligned with the lever")