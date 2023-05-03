if check("the robot's gripper is not near the handle"):
        robot.grab("handle")
    if check("the handle is not almost vertically aligned with the robot's gripper"):
        robot.put("gripper above handle")
    if check("the handle is almost vertically aligned with the robot's gripper and the robot's gripper is not around handle"):
        robot.put("gripper around handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("up on handle from the side")