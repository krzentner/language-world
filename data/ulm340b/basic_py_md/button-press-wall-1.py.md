

Write a program to press the button from the front with a short wall in the way.

```
# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    if check("the robot's gripper is not around the button"):
        robot.put("gripper around button")
    if check("the robot's gripper is around the button"):
        robot.slide("into button")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
```

Here is the code for the last one:
```
# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    if check("the robot's gripper is not around the button"):
        robot.put("gripper around button")
    if check("the robot's gripper is around the button"):
        robot.slide("into button")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
```
"""

print("Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.")

print("\nHere's some code that demonstrates how the robot can do a variety of tasks:")

code_1 = """
# window-close: slide the window closed to the right
def window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# window-