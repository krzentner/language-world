
    if check("the plate is not left of the robot's gripper and the plate is not forward aligned with the robot's gripper"):
        robot.grab("plate")
    if check("the robot's gripper is not near the plate"):
        robot.move("gripper to the plate")
    if check("the robot's gripper is near the plate"):
        robot.slide("the plate to the goal")