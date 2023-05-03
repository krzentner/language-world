# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put gripper near the lever
    #  2. Grab lever with gripper
    #  3. Rotate the lever up
    # To start, move the gripper near the lever.
    if check("the robot's gripper is not near the lever"):
        robot.move("gripper to lever")
    # Once the gripper is near the lever, grab onto it.
    if check("the robot's gripper is near the lever and the robot's gripper is open"):
        robot.grab("lever")
    # Now that the gripper is around the lever, try to rotate the lever up.
    if check("the robot's gripper is around lever"):
        robot.rotate("lever up")