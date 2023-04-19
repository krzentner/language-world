# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    # 1. Put gripper above the lever
    # 2. Grab the lever with the gripper
    # 3. Rotate the gripper to pull the lever up
    
    # Put the gripper above the lever
    if check("the robot's gripper is not above the lever"):
        robot.move_gripper("above the lever")
    # If the gripper is above the lever, grab the lever
    if check("the robot's gripper is above the lever and open"):
        robot.move_gripper("around the lever", close_gripper=True)
    # If the gripper is holding the lever, rotate the gripper up
    if check("the robot's gripper is holding the lever"):
        robot.move_gripper("lever pulled up")