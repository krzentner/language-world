# door-lock: turn the dial on the door
# def door_lock(robot):
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to the right of the dial")
    if check("the robot's gripper is near the dial and the robot's gripper is not aligned with the dial"):
        robot.align("gripper to the dial")
    if check("the robot's gripper is aligned with the dial and the dial is not locked"):
        robot.turn("the dial to lock the door")