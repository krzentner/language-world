# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Push the door closed
    # First, put the gripper around the door handle.
    if check("the robot's gripper is not around door handle"):
        robot.grab("door handle")
    # If the gripper is around the door handle, we can push the door closed.
    if check("the robot's gripper is around door handle"):
        robot.push("door closed to target location")