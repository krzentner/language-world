if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.lift("cube")
    if check("the robot's gripper is above the target location and the cube is not at the target location"):
        robot.move_manipulator("towards target location")
    if check("the robot's gripper is above the target location and the cube is at the target location"):
        robot.place("cube at target location")