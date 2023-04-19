

Steps:
1. Put the gripper in front of plate
2. Push plate back into the target location

if check("the robot's gripper is not in front of plate"):
    robot.move_gripper("in front of plate")
if check("the robot's gripper is in front of plate"):
    robot.move_gripper("near the target location")