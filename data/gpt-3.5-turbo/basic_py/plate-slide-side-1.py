if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the plate is not aligned with the goal and the robot's gripper is around plate"):
        robot.move("plate sideways towards goal")
    if check("the plate is aligned with the goal and the robot's gripper is around plate"):
        robot.slide("plate into goal")