# door-unlock: turn the dial on the door
# def door_unlock(robot):
if check("the robot is not facing the dial or is too far from the dial"):
    robot.turn("to face the dial")
if check("the robot's gripper is not near the dial"):
    robot.move("closer to the dial")
if check("the robot's gripper is near the dial"):
    robot.grab("the dial")
if check("the dial is not in the correct starting position"):
    robot.turn("the dial to the correct starting position")
if check("the dial is not unlocked"):
    robot.turn("the dial to the right until the dial is unlocked")