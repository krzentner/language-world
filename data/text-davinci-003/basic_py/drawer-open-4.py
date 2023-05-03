
    if check("the robot's gripper is not above drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is almost horizontally aligned with the drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is horizontally aligned with the drawer handle"):
        robot.pull("drawer open")