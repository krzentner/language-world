    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the handle is not left of the robot's gripper"):
        robot.grab("handle from the side")
    if check("the handle is grabbed and the robot's gripper is not aligned with the hole"):
        robot.align("handle to hole")
    if check("the robot's gripper is aligned with the hole"):
        robot.pull("handle up from the side")