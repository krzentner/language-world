

Solution:

```
# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    #  1. Put gripper above the wall
    #  2. Drop gripper around the top of the wall, above the button
    #  3. Push down on the button from above, over the wall
    # Start by putting the gripper above the wall, so that we don't catch the
    # wall.
    if check("the robot's gripper is not above the wall"):
        robot.put("gripper above wall")
    # We need the gripper to be around the top of the wall, so move it up and
    # around the wall until it is above the button.
    if check("the robot's gripper is not around the top of the wall and the robot's gripper is open"):
        robot.drop("gripper around the top of the wall")
    # As long as the button is still left of the robot's gripper, we can press
    # down on the button from above the wall.
    if check("the button is left of the robot's gripper"):
        robot.push("down on button from above the wall")
```