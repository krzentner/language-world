

Steps:
1. Put gripper above the ball
2. Drop gripper around ball
3. Close gripper around ball
4. Put the ball in position for aiming at the hoop
5. Shoot the ball by making short lift up

```
# basketball: put the ball into into the hoop
# def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above ball")
    #  2. Drop gripper around ball
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.grab("ball")
    #  3. Close gripper around ball
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    #  4. Put the ball in position for aiming at the hoop
    if check("the robot's gripper is not in a position for aiming at the hoop"):
        robot.align("ball with hoop")
    #  5. Shoot the ball by making short lift up
    if check("the robot's gripper is in a position for aiming at the hoop"):
        robot.lift("ball upwards")