

Steps:
1. Put gripper above basketball
2. Drop gripper around basketball
3. Close gripper around basketball
4. Position robot in line with hoop and basketball
5. Release basketball upwards towards hoop

```
# basketball: put the ball into into the hoop
# def basketball(robot):
    # Steps:
    #  1. Put gripper above basketball
    if check("the robot's gripper is not above basketball"):
        robot.put("gripper above basketball")
    #  2. Drop gripper around basketball
    if check("the robot's gripper is not around basketball and the robot's gripper is open"):
        robot.drop("gripper around basketball")
    #  3. Close gripper around basketball
    if check("the robot's gripper is near basketball and the robot's gripper is open"):
        robot.close("gripper around basketball")
    #  4. Position robot in line with hoop and basketball
    if check("the robot is not in line with the hoop and the basketball"):
        robot.align("robot to hoop and basketball")
    #  5. Release basketball upwards towards hoop
    if check("the robot is in line with the hoop and the basketball"):
        robot.release("basketball up towards hoop")
```