# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not near the dial"):
        robot.reach("to the dial")
    if check("the robot's gripper is near the dial"):
        robot.grab("the dial")
    if check("the dial is not at the 12 o'clock position"):
        robot.turn("dial to 12 o'clock position")
    if check("the dial is at the 12 o'clock position"):
        robot.turn("dial to 3 o'clock position")
    if check("the dial is at the 3 o'clock position"):
        robot.turn("dial to 6 o'clock position")
    if check("the dial is at the 6 o'clock position"):
        robot.release("the dial")