if check("the robot's gripper is not near the cube and the robot's gripper is not aligned with the cube"):
        robot.move("gripper above cube")
    if check("the robot's gripper is near the cube and the robot's gripper is not around the cube"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is around the cube and the cube is not aligned with the goal"):
        robot.align("cube to goal")
    if check("the cube is aligned with the goal and the robot's gripper is holding the cube"):
        robot.move("the cube to the goal")