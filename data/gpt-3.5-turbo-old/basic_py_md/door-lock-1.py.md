# door-lock: turn the dial on the door
# def door_lock(robot):
    if check("the robot's gripper is not near the door lock"):
        robot.move("gripper to the door lock")
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.drop("gripper around the dial")
    if check("the robot's gripper is near the dial and the robot's gripper is open"):
        robot.close("gripper around the dial")
    if check("the robot's gripper is around the dial"):
        robot.turn("the dial to lock the door")