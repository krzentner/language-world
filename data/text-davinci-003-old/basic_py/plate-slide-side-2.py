
    if check("the robot's gripper is not above plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is not sideways aligned with the plate and the robot's gripper is open"):
        robot.move("gripper sideways above plate")
    if check("the robot's gripper is sideways aligned with the plate"):
        robot.slide("plate to goal")
    if check("the robot's gripper is above the plate and the target is not in front of the robot"):
        robot.push("plate to goal")