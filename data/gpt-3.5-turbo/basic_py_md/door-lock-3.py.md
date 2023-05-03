# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not near the dial and the door is closed"):
        robot.move("gripper to dial")
    if check("the robot's gripper is near the dial"):
        robot.grab("dial")
    if check("the dial is not in the 'locked' position"):
        robot.turn("dial to lock position")