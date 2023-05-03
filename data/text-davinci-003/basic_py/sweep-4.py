
    if check("the robot's gripper is not near the cube and the robot's gripper is not above the cube")
        robot.move("gripper close to cube")
    if check("the robot's gripper is near the cube and the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is above cube and the robot's gripper is not around the cube"):
        robot.grab("gripper around cube")
    if check("the robot's gripper is around cube and the cube is not left of the robot's gripper"):
        robot.sweep("cube to goal")