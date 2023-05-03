

Steps: 
1. Set the robot's gripper above the basketball 
2. Drop the gripper around the basketball 
3. Close the gripper around the basketball 
4. Line up the basketball with the hoop 
5. Release the basketball, shooting it into the hoop 

```
# basketball: put the ball into into the hoop
# def basketball(robot):
    # Steps:
    #  1. Set the robot's gripper above the basketball 
    if check("the robot's gripper is not above the basketball"):
        robot.move_gripper("above the basketball")
    #  2. Drop the gripper around the basketball 
    if check("the robot's gripper is not around the basketball"):
        robot.move_gripper("near the basketball", close_gripper=True)
    #  3. Close the gripper around the basketball
    if check("the robot's gripper is not closed"):
        robot.move_gripper("closed") 
    #  4. Line up the basketball with the hoop 
    if check("the basketball is not horizontally aligned with the hoop"):
        robot.move_gripper("horizontally aligned with hoop")
    #  5. Release the basketball, shooting it into the hoop
    if check("the basketball is horizontally aligned with the hoop"):
        robot.move_gripper("above the basketball", open_gripper=True)

```