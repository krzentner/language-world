

The robot needs to push a button from the front, but the button is blocked by a short wall.

The steps required to complete this task would be:

1. Put gripper forward of the wall at the same level as the button
2. Move gripper towards the wall and lower it to the level of the button
3. Push the button from the side

```
# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Put gripper in front of the wall directly above the button
    #  2. Move the gripper towards the wall and lower it to the level of the button
    #  3. Push the button from the side
    # Put the gripper forward of the wall at the same level as the button
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # Move the gripper towards the wall and lower it to the level of the button
    if check("the robot's gripper is not aligned with the button"):
        robot.move_gripper("towards the wall")
    # Now that the gripper is aligned with the button, close the gripper around
    # it and push it from the side.
    if check("the robot's gripper is aligned with the button"):
        robot.move_gripper("near the button", close_gripper=True)
        robot.move_gripper("left of the button")
```