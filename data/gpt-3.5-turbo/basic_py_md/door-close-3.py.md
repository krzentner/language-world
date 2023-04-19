# door-close: push the door closed to the target location
# def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is back-aligned with door handle"):
        robot.push("door closed")