
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is around the cube and the robot's gripper is not forward aligned with the cube"):
        robot.align("gripper to the cube")
    if check("the robot's gripper is forward aligned with the cube and the cube is not horizontally aligned with target location"):
        robot.sweep("cube to goal")
    if check("the cube is horizontally aligned with target location"):
        robot.let_go("the cube")