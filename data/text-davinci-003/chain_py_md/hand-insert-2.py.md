

Steps:
1. Put the gripper above the puck
2. Grab the puck with the gripper
3. Move the puck towards the target location
4. Release the puck at the target location

if check("the robot's gripper is not above the puck"):
     robot.put("gripper above puck")

if check("the robot's gripper is above the puck and the robot's gripper is open"):
    robot.grab("puck")

if check("the robot's gripper is above puck and the robot's gripper is closed"):
    robot.move("puck to target location")

if check("the robot's gripper is near target location and the robot's gripper is closed"):
    robot.release("puck at target location")