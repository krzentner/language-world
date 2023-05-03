# door-close: push the door closed to the target location
def door_close(robot):
    if check("the robot's gripper is not around the door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle and the door is not fully closed"):
        robot.push("door closed")