if check("the robot's gripper is not above the cube"):
        robot.move("gripper above the cube")
    if check("the robot's gripper is not around the cube and the gripper is open"):
        robot.drop("gripper around the cube")
    if check("the robot's gripper is near the cube and the gripper is open"):
        robot.close("gripper around the cube")
    if check("the robot's gripper is above the target location and the gripper is closed"):
        robot.move("cube to the target location")