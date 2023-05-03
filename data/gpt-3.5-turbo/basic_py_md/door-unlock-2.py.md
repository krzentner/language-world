# door-unlock: turn the dial on the door
def door_unlock(robot):
    if check("the robot's gripper is not near the dial"):
        robot.reach("to the door dial")
        robot.grab("the door dial")
    if check("the robot's gripper is holding the dial and the dial is not aligned with the unlock position"):
        robot.rotate("dial to the unlock position") 
    if check("the dial is aligned with the unlock position"):
        robot.release("the dial")
        robot.pull("door open")