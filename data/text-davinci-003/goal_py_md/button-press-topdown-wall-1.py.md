

Steps:
1. Put gripper above the wall and move it forward until the gripper is aligned with the button as seen from above
2. Push down the wall to move it away from the button, until the button is visible
3. Push down on the button from the top

if check("the robot's gripper is not above the wall"):
    robot.move_gripper("above the wall")
if check("the robot's gripper is not aligned with the button as seen from above"):
    robot.move_gripper("forward aligned with the wall")
if check("the wall is blocking the button"):
    robot.move_gripper("tilting the wall away from the button",close_gripper=True)
if check("the wall is removed from the button"):
    robot.move_gripper("near the button")