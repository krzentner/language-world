if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is around cube and the robot's gripper is not over the goal"):
        robot.move("with cube to the goal")
    if check("the robot's gripper is over the goal"):
        robot.drop("cube")