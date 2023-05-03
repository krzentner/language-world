

Steps:
1. Put gripper above hammer
2. Align gripper with hammer and nail
3. Move gripper down to nail
4. Strike the nail with hammer

if check("the robot's gripper is not above hammer"):
    robot.put("gripper above hammer")
if check("the robot's gripper is not horizontally aligned with hammer and nail"):
    robot.align("gripper with hammer and nail")
if check("the robot's gripper is not near the nail and the robot's gripper is open"):
    robot.move("gripper down to nail")
if check("the robot's gripper is near the nail and the robot's gripper is closed"):
    robot.strike("nail with hammer")