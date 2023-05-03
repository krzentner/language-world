
    if check("the robot's gripper is not vertical aligned with the drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with the drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("drawer close")