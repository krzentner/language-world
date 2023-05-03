
    if check("the robot's gripper is not forward-aligned with the cube and the robot's gripper is not near the cube and the robot's gripper is below the cube"):
        robot.move("gripper forward aligned with cube")
    if check("the robot's gripper is almost above the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.drag("cube left or right")
    if check("the cube is almost at the target location"):
        robot.lift("cube to goal")