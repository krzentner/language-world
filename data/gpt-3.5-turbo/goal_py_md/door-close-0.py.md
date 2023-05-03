# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper almost vertically above door handle
    #  2. Drop gripper around door handle
    #  3. Push the door closed
    # If the gripper is not almost vertically above the door handle, move it to
    # the right location.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    # If the gripper isn't around the door handle yet, drop it around the door
    # handle.
    if check("the robot's gripper is not around door handle and the robot's gripper is almost vertically aligned with the door handle"):
        robot.move_gripper("around the door handle")
    # If the gripper is around the door handle, push the door closed to the
    # target location.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("horizontally aligned with the target location")