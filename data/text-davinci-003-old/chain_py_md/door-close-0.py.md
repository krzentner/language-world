

Steps:
1. Put gripper around the door handle
2. Push the door closed

    if check("the robot's gripper is not around door handle and the robot's gripper is open"):
        robot.grab("door handle")
    if check("the robot's gripper is around door handle"):
        robot.push("door closed")