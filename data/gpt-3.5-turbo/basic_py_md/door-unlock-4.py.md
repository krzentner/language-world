# door-unlock: turn the dial on the door
def door_unlock(robot):
    if check("the robot's gripper is not near the door dial"):
        robot.reach("door dial")
    if check("the robot's gripper is near the door dial and the robot's gripper is not around the door dial"):
        robot.grab("door dial")
    if check("the robot's gripper is around the door dial and dial is not turned to the right"):
        robot.turn("dial to the right")
    if check("dial is turned to the right"):
        robot.release("door dial")