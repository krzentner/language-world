if check("the plate is not in front of the robot's gripper and the robot's gripper is not above the plate"):
        robot.move("gripper above plate")
    if check("the robot's gripper is above the plate and the plate is not behind the robot's gripper"):
        robot.grab("plate")
    if check("the plate is behind the robot's gripper"):
        robot.slide("plate back to target location")