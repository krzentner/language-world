# door-unlock: turn the dial on the door
# def door_unlock(robot):
    if check("the robot's gripper is not on the dial"):
        robot.move("gripper to the dial")
    if check("the robot's gripper is on the dial and the dial is not in the correct position"):
        robot.grab("the dial")
        robot.rotate("the dial to the correct position")
        robot.release("the dial")
    if check("the dial is in the correct position"):
        robot.push("the door open")