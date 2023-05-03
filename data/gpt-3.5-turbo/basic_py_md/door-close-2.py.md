# door-close: push the door closed to the target location
def door_close(robot):
    if check("the robot's gripper is not almost vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is closed"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.push("door closed")