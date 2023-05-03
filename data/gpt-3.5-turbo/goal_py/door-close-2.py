# Steps:
    #  1. Put gripper around door handle
    #  2. Push the door closed
    # If the gripper isn't around the door handle, move it there.
    if check("the robot's gripper is not around door handle"):
        robot.move_gripper("around the door handle")
    # If the gripper is around the door handle, push the door closed.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("almost vertically aligned with the door handle")