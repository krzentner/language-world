

Steps:
1. Put gripper in front of the button
2. Drop gripper slightly above the top of the short wall
3. Push down through the wall to push the button

```
# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Put gripper in front of the button
    #  2. Drop gripper slightly above the top of the short wall
    #  3. Push down through the wall to push the button
    # Put the gripper directly in front of the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button")
    # Drop the gripper slightly above the top of the wall.
    if check("the robot's gripper is not above wall"):
        robot.move_gripper("above the wall", close_gripper=True)
    # Push down through the wall to push the button.
    if check("the robot's gripper is above the wall"):
        robot.move_gripper("near the button")