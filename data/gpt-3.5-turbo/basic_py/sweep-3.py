if check("the robot's gripper is not near the cube"):
        robot.put("gripper near the cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is around the cube and the cube is not horizontally aligned with goal"):
        robot.align("cube to goal")
    if check("the robot's gripper is near the goal"):
        robot.slide("cube to goal")