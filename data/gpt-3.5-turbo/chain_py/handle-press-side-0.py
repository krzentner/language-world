# Steps:
    #  1. Put gripper next to handle
    #  2. Push down on handle from the side
    # We need to move the gripper next to the handle first.
    if check("the robot's gripper is not next to the handle"):
        robot.move("gripper next to handle")
    # Once the gripper is next to the handle, we can just push down on it from
    # the side.
    if check("the robot's gripper is next to the handle"):
        robot.push("down on handle from the side")