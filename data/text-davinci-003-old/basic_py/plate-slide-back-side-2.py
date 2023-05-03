
    if check("the robot's gripper is not horizontally aligned with the plate and the robot's gripper is not near the plate"):
        robot.move("gripper to right of plate")
    if check("the robot's gripper is near the plate and the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is above the plate"):
        robot.slide("plate back to the goal")