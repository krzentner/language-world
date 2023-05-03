# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    # 1. Put gripper around the dial handle
    # 2. Turn the dial till the door is locked
    # First, put the gripper around the dial handle
    if check("the robot's gripper is not around the dial handle"):
        robot.move_gripper("around the dial handle")
    # We need to turn the dial to lock the door
    if check("the robot's gripper is around the dial handle"):
        robot.move_gripper("turning the dial until the door is locked")