

if check("the robot's gripper is not above plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is above plate and the robot's gripper is not near plate"):
        robot.move("gripper near plate")
    if check("the robot's gripper is near plate and the robot's gripper is not around plate"):
        robot.grab("gripper around plate")
    if check("the robot's gripper is around plate and the robot's gripper is not gripping firmly"):
        robot.tighten("gripper to grip plate")
    if check("the robot's gripper is holding plate firmly"):
        robot.slide("plate to the goal")