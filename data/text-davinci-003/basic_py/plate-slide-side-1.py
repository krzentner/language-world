
    if check("the plate is not horizontal aligned with the robot's gripper"):
        robot.align("plate horizontal to gripper")
    if check("the plate is not near the target"):
        robot.slide("plate to goal increasing speed over time")
    if check("the plate is below target"):
        robot.push("plate to goal")