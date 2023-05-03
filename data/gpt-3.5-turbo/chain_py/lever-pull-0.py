# Steps:
    #  1. Line up gripper beside the lever
    #  2. Hook the gripper under the lever
    #  3. Rotate the gripper up to pull the lever
    # First, we need to line up the gripper beside the lever.
    if check("the robot's gripper is not beside the lever"):
        robot.move("gripper beside lever")
    # Once the gripper is beside the lever, we need to hook it under the lever.
    if check("the gripper is beside the lever and the gripper is not hooked under lever"):
        robot.hook("gripper under lever")
    # Finally, we can rotate the gripper up to pull the lever.
    if check("the gripper is hooked under lever"):
        robot.rotate("gripper up to pull lever")