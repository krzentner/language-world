

Steps:
1. Put the gripper slightly above the ball
2. Move the gripper around the ball
3. Close the gripper around the ball
4. Hoist the ball up to right beneath the hoop
5. Push the ball forward into the hoop

The code is going to look like this:

```
# basketball: put the ball into into the hoop
# def basketball(robot):
    # Steps:
    #  1. Put the gripper slightly above the ball
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    #  2. Move the gripper around the ball
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.move_gripper("near the ball", close_gripper=True)
    #  3. Close the gripper around the ball
    if check("the robot's gripper is closed"):
        robot.move_gripper("above the hoop")
    #  4. Hoist the ball up to right beneath the hoop
    if check("the robot's gripper is not vertically aligned with the hoop"):
            robot.move_gripper("vertically aligned with the hoop")
    #  5. Push the ball forward into the hoop
    if check("the robot's gripper is vertically aligned with the hoop"):
        robot.move_gripper("horizontally aligned with the hoop")
```