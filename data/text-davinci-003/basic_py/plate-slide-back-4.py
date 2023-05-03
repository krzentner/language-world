
    if check("the robot's gripper is not near plate and the plate is not below the robot's gripper"):
        robot.put("the gripper above the plate")
    if check("the plate is below the robot's gripper and the gripper is not around the plate"):
        robot.grasp("plate")
    if check("the gripper is around the plate and the plate is not aligned to goal"):
        robot.slide("plate to goal")
    if check("the plate is aligned with the goal and the plate is not in goal"):
        robot.slide("plate into goal")