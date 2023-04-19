    # Steps:
    #  1. Align the gripper with the handle from the side
    #  2. Push down on the handle
    # Put the gripper in front of the handle from the side.
    if check("the robot's gripper is not aligned with the handle from the side"):
        robot.move("gripper to handle from the side")
    # Once the gripper is aligned with the handle from the side, push down on the
    # handle.
    if check("the robot's gripper is aligned with the handle from the side"):
        robot.push("down on handle")