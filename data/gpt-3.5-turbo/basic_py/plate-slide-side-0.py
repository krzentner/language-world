if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the grippers are open and the robot's gripper is not around plate"):
        robot.grab("plate")
    if check("the robot's gripper is around plate and the plate is not aligned with the goal location"):
        robot.move("plate to goal location")
    if check("the plate is aligned with goal location"):
        robot.push("plate side to side")