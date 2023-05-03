
    if check("the robot's gripper is not near the plate"):
        robot.put("gripper near plate")
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.grab("plate")
    if check("plate is not to the right of the robot's gripper"):
        robot.align("plate to the right of the robot's gripper")
    if check("plate is to the right of the robot's gripper"):
        robot.slide("plate right and back")