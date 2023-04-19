if check("the robot's gripper is not above the cube"):
    robot.move("gripper above cube")
if check("the robot's gripper is not around the cube and the robot's gripper is open"):
    robot.grab("cube")
if check("the robot's gripper is vertically aligned with the target location and the cube is not below the gripper"):
    robot.move("gripper to target location")
if check("the robot's gripper is above the target location and the gripper is closed"):
    robot.release("cube at target location")