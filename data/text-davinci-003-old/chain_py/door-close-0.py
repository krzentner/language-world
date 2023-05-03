
    # Steps:
    #  1. Put gripper left of the door handle
    #  2. Align gripper with door handle
    #  3. Push the door closed
    # We need to be careful about the direction that we're moving the gripper
    # to push the door closed, since the robot's gripper won't be able to push
    # the door open from the closed position.
    # Move the robot's gripper left of the door handle.
    if check("the door handle is right of the robot's gripper and the robot's gripper is not near the door handle"):
        robot.move("gripper to left of door handle")
    # Once it's near the door handle, we need to make sure it's lined up with the
    # handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is forward aligned with door handle"):
        robot.align("gripper with door handle")
    # As long as the robot's gripper is around the door handle, we can just
    # push it until the door is closed.
    if check("the robot's gripper is around door handle"):
        robot.push("toward door to close")