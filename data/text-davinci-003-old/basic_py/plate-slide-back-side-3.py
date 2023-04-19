
    if check("the robot's gripper is not near the plate"):
        robot.move("gripper near plate")
    if check("the robot's gripper is near the plate and the plate is not to the left of the robot's gripper"):
        robot.grab("plate")
    if check("the robot's gripper is near the plate and the plate is to the left of the robot's gripper"):
        robot.slide("plate sideways")
    if check("the plate is almost in the goal and the robot's gripper is almost vertically aligned with the plate"):
        robot.push("plate into goal")