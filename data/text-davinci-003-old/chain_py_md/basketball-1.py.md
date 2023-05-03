

Steps:
1. Put gripper above the basketball
2. Grab the basketball with the gripper
3. Move the basketball directly above the hoop
4. Drop the basketball into the hoop

if check("the robot's gripper is not above the basketball"):
    robot.put("gripper above basketball")
if check("the robot's gripper is above the basketball but not near it and the robot's gripper is open"):
    robot.grab("basketball")
if check("the robot's gripper is near the basketball and the basketball is not directly above the hoop"):
    robot.line_up("basketball above the hoop")
if check("the robot's gripper is near the basketball and the basketball is directly above the hoop"):
    robot.drop("basketball into the hoop")