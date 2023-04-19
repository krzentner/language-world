# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put gripper around the bottom of the lever
    #  2. Pull the lever upwards
    # First, put the gripper around the bottom of the lever.
    if check("the robot's gripper is not around the bottom of the lever and the robot's gripper is open"):
        robot.move_gripper("near the bottom of the lever", close_gripper=True)
    # If the gripper is around the bottom of the lever, we can pull it upwards.
    if check("the robot's gripper is around the bottom of the lever"):
        robot.move_gripper("above the lever")