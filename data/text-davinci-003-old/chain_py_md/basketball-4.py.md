

Steps:
1. Put the gripper above the basketball
2. Grab the basketball with the gripper
3. Line up the basketball with the hoop
4. Throw the basketball into the hoop

if check("the robot's gripper is not above the basketball"):
    robot.put("gripper above basketball")

if check("the robot's gripper is not around the basketball and the robot's gripper is open"):
    robot.grab("basketball")

if check("the basketball is not aligned with the hoop and the robot's gripper is closed"):
    robot.align("basketball with hoop")

if check("the basketball is aligned with the hoop"):
    robot.throw("basketball into hoop")