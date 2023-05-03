# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    #  1. Put gripper around the door handle
    #  2. Push the door closed to the target location
    # If the gripper is not around the door handle, put it around the door handle.
    if check("the robot's gripper is not around the door handle and the robot's gripper is open"):
        robot.move_gripper("around the door handle", close_gripper=True)
    # If the gripper is around the door handle, push the door closed towards the target location.
    if check("the robot's gripper is around the door handle and the door is not at the target location"):
        robot.move_gripper("towards the target location")