if check("the robot's gripper is not above the cube and the robot's gripper is not vertically aligned with the cube"):
        robot.put("the gripper above the cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around cube"):
        robot.grab("the cube")
    if check("the robot's gripper is around the cube and the robot's gripper is not near the target location"):
        robot.move("the gripper to the target location")
    if check("the robot's gripper is near the target location"):
        robot.release("the cube at target location")