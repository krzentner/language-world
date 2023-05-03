
    if check("the robot's gripper is not almost vertically aligned with puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.grab("puck")
    if check("the puck is not close to the goal"):
        robot.slide("puck to goal while avoiding wall")
    if check("the puck is close to the goal"):
        robot.drop("puck at goal")