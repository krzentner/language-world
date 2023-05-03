
    if check("the robot's gripper is not near cube"):
        robot.move("gripper to cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.grab("cube")
    if check("the robot's gripper is near cube and the robot's gripper is closed"):
        robot.sweep("cube to goal")