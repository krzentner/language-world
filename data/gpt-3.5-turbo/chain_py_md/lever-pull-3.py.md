# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    # 1. Put gripper near the end of the lever
    # 2. Grab the end of the lever with the gripper
    # 3. Rotate the gripper up to pull the lever
    # 4. Release the lever
    # To begin, move the gripper near the end of the lever.
    if check("the robot's gripper is not near the end of the lever"):
        robot.move("gripper to end of lever")
    # Once the gripper is near the end of the lever, grab it.
    if check("the robot's gripper is near the end of the lever and the gripper is open"):
        robot.grab("end of the lever")
    # With the gripper around the lever, rotate the gripper up to pull the lever.
    if check("the gripper is around the lever"):
        robot.rotate("gripper up to pull the lever")
    # Finally, release the lever.
    if check("the gripper is rotated up and around the lever"):
        robot.release("the lever")