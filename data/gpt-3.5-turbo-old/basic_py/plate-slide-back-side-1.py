if check("the robot's gripper is not vertically aligned with the plate and the plate is not at the edge of the table"):
        robot.move("gripper above plate")
    if check("the plate is at the edge of the table and the robot's gripper is not near the plate"):
        robot.move("gripper to the side of the plate")
    if check("the robot's gripper is near the plate and the gripper is not holding the plate"):
        robot.grab("plate")
    if check("the robot's gripper is holding the plate and the target location is not within reach"):
        robot.move("gripper to the target location")
    if check("the target location is within reach of the robot's gripper and the robot's gripper is holding the plate"):
        robot.slide("plate towards the target location")