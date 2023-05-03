Here is a program to perform the `button-press-topdown-wall` task:

```
# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move("gripper above button")
    if check("the robot's gripper is not over the wall"):
        robot.move("gripper to the side of the wall")
    if check("the robot's gripper is over the wall"):
        robot.move("gripper down to the button")
        robot.push("down on button")
```

The program first checks if the gripper is not already vertically aligned with the button, and if so, moves it to the correct position. Then it checks if the gripper is not over the wall, and if not, moves it to the side of the wall. Finally, when the gripper is over the wall, the program moves it down to the button and pushes the button down.