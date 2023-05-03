# Steps:
    #  1. Put gripper near the lever
    #  2. Move the gripper under the lever
    #  3. Rotate the gripper up to rotate the lever
    # To pull the lever, we need to move the gripper under it first. 
    if check("the robot's gripper is not near the lever"):
        robot.move_gripper("near the lever")
    # Once the gripper is near the lever, we can move it under the lever.
    if check("the robot's gripper is near the lever and the gripper is not under the lever"):
        robot.move_gripper("under the lever")
    # Once the gripper is under the lever, we can rotate it up to pull the lever.
    if check("the gripper is under the lever"):
        robot.move_gripper("turned up")