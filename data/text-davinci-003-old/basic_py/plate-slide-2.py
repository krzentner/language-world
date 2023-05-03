
    if check("the robot's gripper is not above plate and plate is not in front of robot's gripper"):
        robot.put("gripper above plate")
    if check("plate is below the robot's gripper and plate is not near the target location"):
        robot.slide("plate near target location")
    if check("plate is near target location"):
        robot.put("plate at target location")