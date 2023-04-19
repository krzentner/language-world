# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    #  1. Put the gripper roughly on the door handle
    #  2. Push the door closed to the target location
    # If the gripper is not near the door handle, move the gripper to it.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the gripper is near the door handle and not on it, move the gripper
    # onto the door handle.
    if check("the robot's gripper is near the door handle but not on it"):
        robot.move_gripper("around the door handle")
    # Once the gripper is on the door handle, we can push the door closed by
    # moving the gripper to the target location.
    if check("the robot's gripper is around the door handle"):
        robot.move_gripper("almost vertically aligned with the target location")
    # If the gripper is almost vertically aligned with the target location, we
    # can push the door closed.
    if check("the robot's gripper is almost vertically aligned with the target location"):
        robot.move_gripper("near the target location")