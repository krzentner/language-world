

The Steps for the program are:
1. Put gripper rotating the wall 
2. Put the gripper just above the button 
3. Slide the wall to the left, avoiding pushing the button down
4. Put the gripper above the button 
5. Push down on the button from the top 

```
# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Put gripper rotating the wall 
    #  2. Put the gripper just above the button 
    #  3. Slide the wall to the left, avoiding pushing the button down
    #  4. Put the gripper above the button
    #  5. Push down on the button from the top 
    # First, put the gripper near the wall and start rotating it.
    if check("the robot's gripper is not near the wall"):
        robot.move_gripper("near the wall", close_gripper=True)
    # Once the wall is rotating, move the gripper just above the button.
    if check("the wall is rotating and the robot's gripper is not just above the button"):
        robot.move_gripper("just above the button")
    # Now we should rotate the wall to the left and avoid pushing the button
    # down.
    if check("the robot's gripper is just above the button and the wall is away from the button"):
        robot.move_gripper("left of the button", close_gripper=False)
    # When the wall is lined up, move the gripper to the button.
    if check("the robot's gripper is left of the button and the wall is very near the button"):
        robot.move_gripper("above the button")
    # Now that the gripper is above the button, just push the button down.
    if check("the robot's gripper is above the button"):
        robot.move_gripper("near the button")
```