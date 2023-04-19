

Steps:
  1. Put gripper left of the button
  2. Push the wall away with the gripper
  3. Line the gripper up with the button
  4. Push down on the button from the front

If the robot's gripper is not left of the button, it should move it there.
We’re working around the wall, so make sure the robot’s gripper is in front of the wall.

```
# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Put gripper left of the button
    #  2. Push the wall away with the gripper
    #  3. Line the gripper up with the button
    #  4. Push down on the button from the front
    # If the robot's gripper is not left of the button, it should move it there.
    if check("the robot's gripper is not left of the button"):
        robot.move_gripper("left of the button and in front of the wall")
    # We’re working around the wall, so make sure the robot’s gripper is in front of the wall.
    if check("the robot's gripper is in front of the wall and the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Once the gripper is lined up with the button, we can push the button down.
    if check("the robot's gripper is forward aligned with the button"):
        robot.move_gripper("near the button")
```