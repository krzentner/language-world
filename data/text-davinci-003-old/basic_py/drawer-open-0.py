
    if check("the robot's gripper is not above the drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is not around drawer handle and the robot's gripper is open"):
        robot.drop("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("drawer open")