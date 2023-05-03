if check("the robot's gripper is not near the cube"):
        robot.grab("the cube")
    if check("the robot's gripper is not aligned with the direction of motion"):
        robot.rotate("gripper to correct orientation")
    if check("the robot's gripper is aligned with the direction of motion and the robot's gripper is not at goal position"):
        robot.move("the gripper towards the goal")
    if check("the robot's gripper is at the goal position and the cube is in the correct position"):
        robot.drop("the cube at the goal position")