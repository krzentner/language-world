
    if check("the robot's gripper is not near the plate and the robot's gripper is not forward aligned with the plate"):
        robot.move("gripper above right side of the plate")
    if check("the robot's gripper is near the plate and the robot's gripper is not below the plate"):
        robot.dive("gripper below plate")
    if check("the robot's gripper is below the plate and the plate is not left of the robot's gripper"):
        robot.slide("plate rightward")
    if check("the plate is left of the robot's gripper"):
        robot.push("plate to goal")