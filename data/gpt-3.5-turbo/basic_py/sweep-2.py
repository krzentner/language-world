if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move("gripper above cube")
    if check("the gripper is not around the cube"):
        robot.grab("cube")
    if check("the robot's gripper is not above the goal location"):
        robot.move("gripper above goal location")
    if check("the robot's gripper is forward aligned with the goal location and not next to it"):
        robot.move("gripper horizontally to the goal location")
    if check("the robot's gripper is next to the goal location"):
        robot.move("gripper into goal location to place cube")
    if check("the robot's gripper is in the goal location and holds the cube"):
        robot.release("cube")