
    # Steps:
    #  1. Line gripper with bottom of lever
    #  2. Pull the lever
    # Because this is a lever, the robot needs to grab it with its gripper from
    # the bottom.
    if check("the robot's gripper is not vertical aligned with, and not overlapping the lever"):
        robot.move_gripper("vertically aligned with the lever")
    # Once the gripper has grabbed the lever, it can just move it up to rotate
    # the lever.
    if check("the robot's gripper is vertically aligned with the lever and the robot's gripper is not overlapping the lever"):
        robot.move_gripper("upward aligned with the lever")