

if check("the robot's gripper is not near drawer handle"):
    robot.put("gripper around drawer handle")
if check("the robot's gripper is around drawer handle and the drawer is open"):
    robot.push("drawer close")