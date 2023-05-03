

The steps for putting the ball into the hoop are as follows:
1. Put the gripper above the ball
2. Drop the gripper around the ball
3. Line up the robot's gripper vertically with the hoop
4. Push the ball in with the robot's gripper

```
# basketball: put the ball into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Drop the gripper around the ball
    #  3. Line up the robot's gripper vertically with the hoop
    #  4. Push the ball in with the robot's gripper
    # 
    # First, put the gripper roughly above the ball.
    if check("the robot's gripper is not above the ball."):
        robot.put("gripper above ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.drop("gripper around the ball")
    # If the robot's gripper is near the ball and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the ball and the robot's gripper is open"):
        robot.close("gripper around the ball")
    # We closed the gripper, and the ball is still near the gripper, so maybe we
    # grabbed it.
    # Line up the robot's gripper vertically with the hoop.
    if check("the robot's gripper is above the ball and the robot's gripper is closed"):
        robot.align("gripper vertically with the hoop")
    # Once the robot's gripper is lined up with the hoop, push the ball in with 
    # the robot's gripper.
    if check("the robot's gripper is vertically aligned with the hoop"):
        robot.push("ball into the hoop")