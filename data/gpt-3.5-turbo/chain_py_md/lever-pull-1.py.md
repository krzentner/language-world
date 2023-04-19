# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put the gripper around the lever
    #  2. Rotate the gripper up
    #  3. Release the lever
    # First, put the gripper roughly around the lever.
    if check("the robot's gripper is not roughly around the lever"):
        robot.place("gripper around lever")
    # If the gripper is around the lever, rotate it up to pull the lever.
    if check("the robot's gripper is around the lever"):
        robot.rotate("gripper up")
    # If the gripper is above the lever, release the lever to complete the task.
    if check("the robot's gripper is above the lever"):
        robot.release("lever")