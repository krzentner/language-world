if check("the robot's gripper is not near the cube"):
        robot.move("gripper above cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is around the cube and the cube is not at the target location"):
        robot.move("sideways with cube towards target location")
    if check("the robot's gripper is at the target location and the cube is in the gripper"):
        robot.place("cube at target location")