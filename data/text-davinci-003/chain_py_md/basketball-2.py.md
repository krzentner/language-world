

Steps:
1. Put the gripper above the basketball. 
2. Grab the basketball with the gripper. 
3. Line the basketball up with the hoop.
4. Lift the basketball and align it with the hoop. 
5. Release the basketball and push it into the hoop.

```
# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put the gripper above the basketball
    #  2. Grab the basketball with the gripper
    #  3. Line the basketball up with the hoop
    #  4. Lift the basketball and align it with the hoop
    #  5. Release the basketball and push it into the hoop
    if check("the robot's gripper is not above the basketball"):
        robot.put("gripper above basketball")
    if check("the robot's gripper is not around basketball and the robot's gripper is open"):
        robot.grab("basketball")
    if check("the basketball is not horizontally aligned with the hoop"):
        robot.align("basketball to hoop")
    if check("the basketball is horizontally aligned with the hoop and the robot's gripper is closed"):
        robot.lift("basketball")
    if check("the basketball is above the hoop and the robot's gripper is closed"):
        robot.release("basketball")
    if check("the robot's gripper is above basketball and the robot's gripper is open"):
        robot.push("basketball into hoop")
```