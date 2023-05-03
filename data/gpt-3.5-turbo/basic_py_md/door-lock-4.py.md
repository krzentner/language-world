# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not in front of the dial"):
        robot.move("gripper to right of dial")
    if check("the robot's gripper is in front of the dial and the robot's gripper is not around the dial"):
        robot.put("gripper around dial")
    if check("the robot's gripper is around the dial and the dial is not locked"):
        robot.turn("dial to the right until locked")