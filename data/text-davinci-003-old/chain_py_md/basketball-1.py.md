

Steps:
1. Put gripper above the basketball
2. Drop gripper around the basketball
3. Close gripper around the basketball
4. Lift the basketball up to the hoop
5. Move the basketball left or right to line up with the hoop
6. Push the basketball into the hoop

if check("the robot's gripper is not above the basketball"):
    robot.put("gripper above basketball")
if check("the robot's gripper is not around the basketball and the robot's gripper is open"):
    robot.drop("gripper around basketball")
if check("the robot's gripper is near the basketball and the robot's gripper is open"):
    robot.close("gripper around basketball")
if check("the robot's gripper is above the basketball and the robot's gripper is closed"):
    robot.lift("basketball up to the hoop")
if check("the basketball is not left or right aligned with the hoop"):
    robot.move("basketball left or right to line up with hoop")
if check("the basketball is left or right aligned with the hoop"):
    robot.push("basketball into hoop")