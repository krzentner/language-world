if check("the plate is not in the robot's gripper"):
        robot.grab("the plate")
    if check("the robot's gripper is not above the target location"):
        robot.put("the gripper above the target location")
    if check("the robot's gripper is above the target location and the plate is not aligned with it"):
        robot.move("the plate into alignment with the target location")
    if check("the plate is aligned with the target location"):
        robot.slide("the plate into the target location")