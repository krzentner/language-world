
    if check("the robot's gripper is not forward aligned with the platform and the robot's gripper is not below the platform"):
        robot.place("gripper above and forward of the platform")
    
    if check("the robot's gripper is forward aligned with the platform and the robot's gripper is open"):
        robot.put("gripper below platform")
    if check("the robot's gripper is below the platform"):
        robot.push("plate back sideways to goal")