# door-lock: turn the dial on the door
# def door_lock(robot):
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to the dial")
    if check("the robot's gripper is near the dial and the dial is not in the correct position"):
        robot.grab("the dial")
        robot.turn("the dial to the correct position")
    if check("the dial is in the correct position and the robot's gripper is holding it"):
        robot.release("the dial")