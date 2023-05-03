# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper near the door handle
    #  2. Move gripper towards door to start pushing
    #  3. Push the door closed
    # If the robot's gripper is not vertically aligned with the door handle,
    # move the gripper near the handle.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the gripper is near the door handle, move it towards the door to start
    # pushing.
    if check("the robot's gripper is near the door handle and the robot's gripper is not in front of the door handle"):
        robot.move_gripper("in front of the door handle")
    # Once the gripper is in front of the door handle, push the door close to
    # the target location.
    if check("the robot's gripper is in front of the door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
        robot.move_gripper("near the target location")