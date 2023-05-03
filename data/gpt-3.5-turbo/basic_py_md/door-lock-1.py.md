# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not near the dial"):
        robot.reach("to door dial")
    if check("the robot's gripper is near the dial and the robot's gripper is not around dial"):
        robot.grab("door dial")
    if check("the dial is not pointing to the locked position"):
        robot.turn("the dial to the locked position")
    if check("the dial is pointing to the locked position and the robot's gripper is around the dial"):
        robot.release("the dial")