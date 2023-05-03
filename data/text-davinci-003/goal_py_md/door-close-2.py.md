

# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper right of the door handle
    #  2. Put gripper around the door handle
    #  3. Push the door closed
    # First, put the gripper on the right side of the door handle.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("right of the door handle")
    # Once the gripper is to the right, drop the gripper around the door handle.
    if check("the robot's gripper is not around the door handle"):
        robot.move_gripper("around the door handle", close_gripper=True)
    # If the gripper is around the door handle, we can push the door closed.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("above the door handle")