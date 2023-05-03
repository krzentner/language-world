# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    #  1. Put gripper around the door handle
    #  2. Push the door closed
    # If the gripper is not around the door handle, move it to the door handle.
    if check("the robot's gripper is not around door handle"):
        robot.move_gripper("around the door handle")
    # If the door is almost closed, move the gripper a little further away to
    # reduce the chance of bumping it.
    if check("the door is almost closed"):
        robot.move_gripper("left of the door handle")
    # If the gripper is around the door handle, push the door closed.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("almost vertically aligned with the door handle")