# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Push the door closed
    # If the gripper is not around the door handle, move it there.
    if check("the robot's gripper is not around door handle"):
        robot.grab("door handle")
    # If the door is not vertically aligned with the robot's gripper, nudge it
    # until it is.
    if check("the robot's gripper is around door handle and the door is not vertically aligned with the robot's gripper"):
        robot.move("door handle into place")
    # If the door is vertically aligned and the gripper is still around the
    # handle, push the door closed.
    if check("the robot's gripper is around door handle and the door is vertically aligned with the robot's gripper"):
        robot.push("door closed")