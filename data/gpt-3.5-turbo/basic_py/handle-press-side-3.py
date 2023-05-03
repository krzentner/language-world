if check("the robot's gripper is not vertically aligned with handle"):
        robot.move("gripper to side of handle")
    if check("the robot's gripper is beside handle and the robot's gripper is open"):
        robot.grab("handle")
    if check("the robot's gripper is around handle and the robot's gripper is not above the handle"):
        robot.move("gripper above handle")
    if check("the robot's gripper is above handle and the handle is not pressed down"):
        robot.push("down on handle")