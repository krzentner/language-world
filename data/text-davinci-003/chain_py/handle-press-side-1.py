
    # Steps:
    #  1. Put gripper near the handle
    #  2. Line up the gripper as viewed from the side
    #  3. Push down the handle
    # First, we need to put the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper to handle")
    # Once the gripper is near the handle, we should line up the gripper as
    # seen from the side to make sure it can push down on the handle.
    if check("the robot's gripper is near the handle and the robot's gripper is not horizontally aligned with the handle"):
        robot.align("gripper to handle")
    # Finally, push down on the handle.
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.push("down on handle")