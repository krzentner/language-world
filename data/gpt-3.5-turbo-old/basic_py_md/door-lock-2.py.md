# door-lock: turn the dial on the door
# def door_lock(robot):
    if check("the robot's gripper is not in front of the dial"):
        robot.move("gripper in front of the dial")
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.drop("gripper around the dial")
    if check("the robot's gripper is near the dial and the robot's gripper is open"):
        robot.close("gripper around the dial")
    if check("the robot's gripper is around the dial"):
        robot.turn("dial to the left until it clicks")
        robot.move("gripper away from the dial")