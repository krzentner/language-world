if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is not around plate"):
        robot.grab("plate")
    if check("the plate is not aligned with the goal location"):
        robot.move("plate to goal location")
    if check("the plate is aligned with the goal location and not pushed back"):
        robot.slide("the plate back sideways into the goal location")