# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    # 1. Move the gripper behind the lever
    # 2. Grip the lever handle
    # 3. Rotate the gripper upwards to pull the lever
    # First, move the gripper behind the lever.
    if check("the robot's gripper is not behind the lever"):
        robot.move("gripper behind lever")
    # Once the gripper is behind the lever, grab the handle.
    if check("the robot's gripper is behind the lever and the robot's gripper is not gripping lever handle"):
        robot.grip("lever handle")
    # Rotate the gripper up to pull the lever.
    if check("the robot's gripper is gripping the handle"):
        robot.rotate("gripper upwards to pull the lever")