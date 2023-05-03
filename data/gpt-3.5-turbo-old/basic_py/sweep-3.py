if check("the robot's gripper is not above or near the cube"):
        robot.move("gripper above the cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around the cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around the cube")
    if check("the robot's gripper is above the cube and the robot's gripper is closed and the robot is not at the target location"):
        robot.move("sideways towards the target location while holding the cube")
    if check("the robot has reached the target location"):
        robot.drop("the cube at the target location")