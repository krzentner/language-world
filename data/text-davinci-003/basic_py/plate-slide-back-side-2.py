
    if check("the robot's gripper is not above the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.drop("the gripper around the plate")
    if check("the robot's gripper is around the plate and the robot's gripper is open"):
        robot.push("the plate backward until it is aligned with the goal")
    if check("the plate is aligned with the goal"):
        robot.slide("the plate right until it is in the goal")