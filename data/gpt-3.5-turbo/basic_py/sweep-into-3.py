if check("the robot's gripper is not above the cube"):
        robot.put("gripper above the cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around the cube")
    if check("the robot's gripper is vertical and aligned with the cube and the robot's gripper is open"):
        robot.close("gripper around the cube")
    if check("the robot's gripper is near the target location"):
        robot.move("gripper to the target location")
    if check("the robot's gripper is above the target location and the robot's gripper is closed"):
        robot.drop("the cube at the target location")