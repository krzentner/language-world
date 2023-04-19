if check("the plate is not on the table and the robot's gripper is not near the plate"):
        robot.move("gripper to plate position")
    if check("the robot's gripper is near the plate and the robot's gripper is not above the plate"):
        robot.move("gripper above the plate")
    if check("the robot's gripper is above the plate and the robot's gripper is not holding the plate"):
        robot.grab("plate")
    if check("the robot's gripper is holding the plate and the plate is not aligned with the target location"):
        robot.move("plate to target location")
    if check("the plate is aligned with the target location"):
        robot.slide("plate into the target location")