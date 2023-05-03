
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Push down on the handle
    # We need to line up the gripper as seen from the side.
    # We want to be careful when lining up the gripper, so we should check if
    # the handle is right of the gripper and not below it, since that's the
    # direction we're trying to line up in.
    if check("the handle is right of the robot's gripper and the handle is not below the robot's gripper"):
        robot.move("gripper to side of handle")
    # Once the gripper is lined up from the side, push it down.
    if check("the handle is left of the robot's gripper and the handle is below the robot's gripper"):
        robot.push("down on handle")