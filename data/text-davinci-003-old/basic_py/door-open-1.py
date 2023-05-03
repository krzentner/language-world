
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")

# door-close: push the door closed
# def door_close(robot):
    if check("the robot's gripper is below door handle"):
        robot.lift("gripper to right of the door handle")
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")
    if check("the robot's gripper is in front of the door handle"):
        robot.push("door closed harder")