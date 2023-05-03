# door-unlock: turn the dial on the door
def door_unlock(robot):
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to the right of the dial")
    if check("the robot's gripper is near the dial and gripper is not around the dial"):
        robot.put("gripper around dial")
    if check("the robot's gripper is around the dial"):
        robot.turn("dial clockwise")
        robot.turn("dial clockwise")
        robot.turn("dial clockwise")