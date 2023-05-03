    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not around the handle"):
        robot.grab("handle")
    if check("the robot's gripper is not forward aligned with the handle"):
        robot.align("gripper to handle")
    if check("the robot's gripper is forward aligned with the handle"):
        robot.push("down on handle from side")