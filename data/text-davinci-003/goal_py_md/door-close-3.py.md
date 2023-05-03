

# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper left of the door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # First, move the gripper to the left of the door handle.
    if check("the robot's gripper is not left of the door handle"):
        robot.move_gripper("left of the door handle")
    # Once the gripper is close to the door handle, we can start pushing
    # against the handle to close the door.
    if check("the robot's gripper is left of the door handle and the robot's gripper is not near the door handle"):
        robot.move_gripper("right of the door handle")
    # When the door handle is close enough, push harder to close the door.
    if check("the robot's gripper is near the door handle and the door is not closed"):
        robot.move_gripper("forward aligned with the door handle")