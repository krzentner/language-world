

Then the solution:

```
# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    #  1. Put gripper above wall
    #  2. Drop gripper over wall
    #  3. Move gripper right of the button
    #  4. Push down on the button from the top
    # Put the gripper roughly above the wall.
    if check("the robot's gripper is not above wall"):
        robot.place("gripper above wall")
    # Move the gripper down and right to get over the wall.
    if check("the robot's gripper is not over wall and the robot's gripper is below wall"):
        robot.drop("gripper over wall")
    # Move the gripper over to the right of button.
    if check("the robot's gripper is not right of the button"):
        robot.move("gripper to right of button")
    # Finally, push down on the button from the top.
    if check("the robot's gripper is right of the button"):
        robot.push("down on button")
```