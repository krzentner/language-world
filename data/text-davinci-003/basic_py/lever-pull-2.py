
    if check("the robot's gripper is not above the lever"):
        robot.grab("lever near to its handle")
    if check("the lever is down and the robot's gripper is close to the lever"):
        robot.rotate("lever up")

# door-close: push the door close
def door_close(robot):
    if check("the robot's gripper is forward aligned with door handle and the robot's gripper is not around door handle"):
        robot.move("gripper around door handle")
    if check("the robot's gripper is around door handle and door is open"):
        robot.push("door closed")