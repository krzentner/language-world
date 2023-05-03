# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    #   1. Put gripper roughly around the door handle
    #   2. Push the door closed
    # If the gripper is not near the door handle, move it to the handle.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the gripper is near the door handle, push the door closed.
    if check("the robot's gripper is around the door handle"):
        robot.move_gripper("towards the target location")