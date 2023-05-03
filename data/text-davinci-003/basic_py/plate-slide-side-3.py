
    if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is near the plate and the gripper is not forward aligned with the plate"):
        robot.move("the gripper over the plate")
    if check("the robot's gripper is forward aligned with the plate and the plate is not sideways aligned with the goal"):
        robot.slide("the plate to the goal")
    if check("the plate is sideways aligned with the goal"):
        robot.slide("the plate into the goal")