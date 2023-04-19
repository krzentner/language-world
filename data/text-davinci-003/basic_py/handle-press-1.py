
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper near the handle")
    if check("the robot's gripper is near handle and the robot's gripper is not vertically aligned with the handle"):
        robot.align("gripper with the handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.push("down on the handle")