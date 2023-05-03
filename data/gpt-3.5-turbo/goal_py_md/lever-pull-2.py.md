# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper around the lever
    #  2. Rotate the gripper up to pull the lever
    # To begin, position the gripper around the lever. 
    if check("the robot's gripper is not around the lever and the robot's gripper is open"):
        robot.move_gripper("around the lever", close_gripper=True)
    # If the gripper is around the lever, rotate the gripper up to pull the lever.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("above the lever, rotated up")